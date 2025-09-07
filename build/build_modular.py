#!/usr/bin/env python3
"""
Modular build script for Boston Robot Hackers website.
Split into focused modules for better maintainability.
"""

import json
from pathlib import Path
from typing import Dict, Any

from jinja2 import Environment, FileSystemLoader

from asset_manager import AssetManager
from content_manager import ContentManager, ContentType
from page_builder import PageBuilder


class WebsiteBuilder:
    """Main website builder orchestrating all components."""
    
    def __init__(self):
        # Detect if running from build/ subdirectory or root directory
        current_dir = Path.cwd()
        if current_dir.name == "build":
            self.root_dir = Path("..")
        else:
            self.root_dir = Path(".")
        
        self.templates_dir = self.root_dir / "templates"
        self.config_dir = self.root_dir / "config"
        self.content_dir = self.root_dir / "content"
        self.dist_dir = self.root_dir / "output"
        
        # Create dist directory if it doesn't exist
        self.dist_dir.mkdir(exist_ok=True)
        
        # Load configurations
        self.site_config = self.load_site_config()
        
        # Set up Jinja2 environment
        template_paths = [str(self.templates_dir)]
        self.jinja_env = Environment(loader=FileSystemLoader(template_paths))
        
        # Initialize managers
        self.content_manager = ContentManager(self.content_dir)
        self.page_builder = PageBuilder(self.jinja_env, self.dist_dir, self.site_config)
        self.asset_manager = AssetManager(self.root_dir, self.dist_dir)
        
        # Define content types
        self.content_types = {
            'news': ContentType('news', 'news', output_filename='whatsnew.html', 
                              page_template='pages/whatsnew.html', 
                              detail_template='details/news-detail.html'),
            'projects': ContentType('projects', 'projects',
                                  detail_template='details/project-detail.html'),
            'members': ContentType('members', 'members', sort_key='title', reverse=False,
                                 detail_template='details/member-detail.html'),
        }
    
    def load_site_config(self) -> Dict[str, Any]:
        """Load site configuration."""
        config_file = self.config_dir / "site.json"
        if config_file.exists():
            return json.loads(config_file.read_text())
        return {}
    
    def build_whatsnew(self) -> str:
        """Build the What's New section from markdown files (highlighted only)."""
        posts = self.content_manager.get_all_content(self.content_types['news'])
        highlighted_posts = [post for post in posts if post['metadata'].get('highlight', False)]
        
        news_html = self.page_builder.render_news_cards(highlighted_posts)
        print(f"Generated {len(highlighted_posts)} highlighted posts from {len(posts)} total")
        return news_html
    
    def build_index(self):
        """Build the main index.html file."""
        news_content = self.build_whatsnew()
        hero_content = self.content_manager.build_hero_content()
        
        projects = self.content_manager.get_all_content(self.content_types['projects'])
        projects_content = self.page_builder.render_project_cards_for_home(projects)
        
        output_file = self.page_builder.build_page(
            'pages/index.html', 
            'index.html',
            news_content=news_content,
            hero=hero_content,
            projects_content=projects_content
        )
        
        print(f"Generated {output_file}")
    
    def build_news_page(self):
        """Build the whatsnew.html page with all news items."""
        posts = self.content_manager.get_all_content(self.content_types['news'])
        self.page_builder.build_detail_pages(posts, self.content_types['news'])
        
        news_content = self.page_builder.render_compact_news_cards(posts)
        hero_content = self.content_manager.build_hero_content('whatsnew')
        
        self.page_builder.build_page(
            'pages/whatsnew.html',
            'whatsnew.html',
            hero=hero_content,
            news_content=news_content
        )
        
        print(f"Built whatsnew.html with {len(posts)} posts")
    
    def build_projects_page(self):
        """Build the projects.html page."""
        projects = self.content_manager.get_all_content(self.content_types['projects'])
        self.page_builder.build_detail_pages(projects, self.content_types['projects'])
        
        projects_content = self.page_builder.render_projects_content(projects)
        hero_content = self.content_manager.build_hero_content('projects')
        
        self.page_builder.build_page(
            'pages/projects.html',
            'projects.html',
            hero=hero_content,
            projects_content=projects_content
        )
        
        print(f"Built projects.html with {len(projects)} projects")
    
    def build_members_page(self):
        """Build the members.html page."""
        members = self.content_manager.get_all_content(self.content_types['members'])
        self.page_builder.build_detail_pages(members, self.content_types['members'])
        
        members_content = self.page_builder.render_member_cards(members)
        hero_content = self.content_manager.build_hero_content('members')
        
        self.page_builder.build_page(
            'pages/members.html',
            'members.html',
            hero=hero_content,
            members_content=members_content
        )
        
        print(f"Built members.html with {len(members)} members")
    
    def build_about_page(self):
        """Build the about.html page."""
        about_content = self.content_manager.process_single_content_file('about.md')
        hero_content = self.content_manager.build_hero_content('about')
        
        self.page_builder.build_page(
            'pages/about.html',
            'about.html',
            hero=hero_content,
            about_content=about_content
        )
        
        print("Built about.html")
    
    def build_nextmeeting_page(self):
        """Build the nextmeeting.html page."""
        nextmeeting_file = self.content_dir / 'nextmeeting.md'
        
        if not nextmeeting_file.exists():
            print(f"Warning: {nextmeeting_file} not found")
            nextmeeting_content = "<p>Next meeting content not found.</p>"
            hero_content = {'hero_title': 'Next Meeting', 'hero_subtitle': '', 'hero_content': ''}
        else:
            nextmeeting_data = self.content_manager.process_markdown_file(nextmeeting_file)
            nextmeeting_content = nextmeeting_data['content'] if nextmeeting_data else "<p>Error processing next meeting content.</p>"
            
            if nextmeeting_data:
                hero_content = {
                    'hero_title': nextmeeting_data['title'],
                    'hero_subtitle': nextmeeting_data['metadata'].get('subtitle', ''),
                    'hero_content': ''
                }
            else:
                hero_content = {'hero_title': 'Next Meeting', 'hero_subtitle': '', 'hero_content': ''}
        
        # Build page in subdirectory
        nextmeeting_dir = self.dist_dir / 'nextmeeting'
        nextmeeting_dir.mkdir(exist_ok=True)
        
        template = self.jinja_env.get_template('pages/nextmeeting.html')
        html_content = template.render(
            site=self.site_config,
            hero=hero_content,
            nextmeeting_content=nextmeeting_content
        )
        
        output_file = nextmeeting_dir / 'index.html'
        output_file.write_text(html_content, encoding='utf-8')
        print("Built nextmeeting/index.html")
    
    def build(self):
        """Main build function."""
        print("Building Boston Robot Hackers website...")
        print("Using modular design")
        
        # Clean output directory for fresh build
        self.asset_manager.clean_output_directory()
        
        # Copy static assets
        self.asset_manager.copy_assets()
        self.asset_manager.copy_css_files()
        
        # Generate syntax highlighting CSS
        self.asset_manager.generate_pygments_css('default')
        
        # Build pages
        self.build_index()
        self.build_news_page()
        self.build_projects_page()
        self.build_members_page()
        self.build_about_page()
        self.build_nextmeeting_page()
        
        print("Build complete!")


def main():
    """Main entry point."""
    builder = WebsiteBuilder()
    builder.build()


if __name__ == '__main__':
    main()