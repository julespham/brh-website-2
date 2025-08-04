#!/usr/bin/env python3
"""
Build script for Boston Robot Hackers website.
Uses template-based architecture with themes.
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader
from pygments.formatters import HtmlFormatter


class WebsiteBuilder:
    def __init__(self):
        self.root_dir = Path("..")  # Build script is now in build/ subdirectory
        self.templates_dir = self.root_dir / "templates"
        self.themes_dir = self.root_dir / "themes"
        self.config_dir = self.root_dir / "config"
        self.content_dir = self.root_dir / "content"
        self.dist_dir = self.root_dir / "output"
        
        # Create dist directory if it doesn't exist
        self.dist_dir.mkdir(exist_ok=True)
        
        # Load configurations
        self.site_config = self.load_site_config()
        self.theme_config = self.load_theme_config()
        self.active_theme = self.load_active_theme()
        
        # Set up Jinja2 environment
        theme_name = self.theme_config['active_theme']
        template_paths = [
            str(self.templates_dir / theme_name),  # Theme-specific templates first
            str(self.templates_dir / "base"),      # Fallback to base templates
            str(self.themes_dir / theme_name)      # Theme includes (head.html, etc.)
        ]
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_paths)
        )
    
    def load_site_config(self) -> Dict[str, Any]:
        """Load site configuration."""
        config_file = self.config_dir / "site.json"
        if config_file.exists():
            return json.loads(config_file.read_text())
        return {}
    
    def load_theme_config(self) -> Dict[str, Any]:
        """Load theme configuration."""
        config_file = self.themes_dir / "config.json"
        if config_file.exists():
            return json.loads(config_file.read_text())
        return {"active_theme": "tailwind"}
    
    def load_active_theme(self) -> Dict[str, Any]:
        """Load the active theme configuration."""
        theme_name = self.theme_config.get('active_theme', 'tailwind')
        theme_file = self.themes_dir / theme_name / "theme.json"
        
        if theme_file.exists():
            theme_data = json.loads(theme_file.read_text())
            # Flatten the classes into the main theme object
            if 'classes' in theme_data:
                theme_data.update(theme_data['classes'])
            return theme_data
        return {}
    
    def setup_markdown_processor(self):
        """Set up markdown processor with syntax highlighting."""
        return markdown.Markdown(
            extensions=[
                'codehilite',
                'fenced_code',
                'tables',
                'toc'
            ],
            extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'use_pygments': True,
                    'noclasses': False,
                }
            }
        )
    
    def generate_pygments_css(self, theme='default'):
        """Generate Pygments CSS for syntax highlighting."""
        formatter = HtmlFormatter(style=theme, cssclass='highlight')
        css_content = formatter.get_style_defs('.highlight')
        
        css_file = self.dist_dir / 'syntax.css'
        css_file.write_text(css_content)
        print(f"Generated syntax highlighting CSS: {css_file}")
    
    def process_markdown_file(self, file_path: Path, md_processor) -> Dict[str, Any]:
        """Process a single markdown file and return structured data."""
        try:
            # Parse front matter and content
            post = frontmatter.load(file_path)
            
            # Process markdown content
            html_content = md_processor.convert(post.content)
            
            # Extract metadata
            metadata = post.metadata
            
            # Parse date from filename if not in front matter
            if 'date' not in metadata:
                # Assume filename format: YYYY-MM-DD-title.md
                date_str = file_path.stem[:10]  # First 10 chars should be date
                try:
                    metadata['date'] = datetime.strptime(date_str, '%Y-%m-%d').date().isoformat()
                except ValueError:
                    metadata['date'] = datetime.now().date().isoformat()
            elif isinstance(metadata['date'], datetime):
                metadata['date'] = metadata['date'].isoformat()
            elif hasattr(metadata['date'], 'isoformat'):
                metadata['date'] = metadata['date'].isoformat()
            
            # Ensure required fields have defaults
            return {
                'id': file_path.stem,
                'title': metadata.get('title', 'Untitled'),
                'date': metadata.get('date'),
                'image': metadata.get('image', ''),  # URL to 512x512 square image (scaled with CSS as needed)
                'text': metadata.get('text', metadata.get('emoji', 'NEWS')),  # Simple text overlay
                'excerpt': metadata.get('excerpt', ''),
                'content': html_content,
                'metadata': metadata
            }
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def format_date(self, date_str: str) -> str:
        """Format date string for display."""
        if isinstance(date_str, str):
            try:
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                return date_obj.strftime('%B %d, %Y')
            except ValueError:
                return date_str
        return str(date_str)
    
    def render_news_cards(self, posts: List[Dict[str, Any]]) -> str:
        """Render news cards using the template."""
        template = self.jinja_env.get_template('news-card.html')
        
        cards_html = []
        for post in posts:
            # Use basic image classes
            image_classes = self.active_theme['news_image_classes']
            
            card_html = template.render(
                title=post['title'],
                excerpt=post['excerpt'],
                text=post['text'],
                image=post['image'],
                formatted_date=self.format_date(post['date']),
                theme=self.active_theme,
                image_classes=image_classes
            )
            cards_html.append(card_html)
        
        return '\n'.join(cards_html)
    
    def build_hero_content(self) -> Dict[str, Any]:
        """Build hero content from markdown file."""
        hero_file = self.content_dir / 'hero.md'
        if not hero_file.exists():
            print(f"Warning: {hero_file} not found, using defaults")
            return {
                'hero_title': 'Boston Robot Hackers',
                'hero_subtitle': 'Building the future, one robot at a time.'
            }
        
        # Set up markdown processor
        md_processor = self.setup_markdown_processor()
        
        # Process hero markdown file
        hero_data = self.process_markdown_file(hero_file, md_processor)
        if hero_data:
            return {
                'hero_title': hero_data['title'],
                'hero_subtitle': hero_data['metadata'].get('subtitle', ''),
                'hero_content': hero_data['content']
            }
        
        return {
            'hero_title': 'Boston Robot Hackers',
            'hero_subtitle': 'Building the future, one robot at a time.'
        }

    def build_whatsnew(self) -> str:
        """Build the What's New section from markdown files."""
        whatsnew_dir = self.content_dir / 'news'
        if not whatsnew_dir.exists():
            print(f"Warning: {whatsnew_dir} directory not found")
            return ""
        
        # Set up markdown processor
        md_processor = self.setup_markdown_processor()
        
        # Process all markdown files
        posts = []
        for md_file in whatsnew_dir.glob('*.md'):
            post_data = self.process_markdown_file(md_file, md_processor)
            if post_data:
                posts.append(post_data)
        
        # Sort by date (newest first) 
        posts.sort(key=lambda x: x['date'], reverse=True)
        
        # Render news cards
        news_html = self.render_news_cards(posts)
        
        # Save JSON for potential future use
        output_file = self.dist_dir / 'whatsnew.json'
        with open(output_file, 'w') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        
        print(f"Generated {len(posts)} posts")
        return news_html
    
    def build_index(self):
        """Build the main index.html file."""
        # Generate news content
        news_content = self.build_whatsnew()
        
        # Generate hero content
        hero_content = self.build_hero_content()
        
        # Load and render the main template
        template = self.jinja_env.get_template('index.html')
        
        # Render the template with all data
        html_content = template.render(
            site=self.site_config,
            theme=self.active_theme,
            news_content=news_content,
            hero=hero_content
        )
        
        # Write the generated HTML
        output_file = self.dist_dir / 'index.html'
        output_file.write_text(html_content)
        
        print(f"Generated {output_file}")
    
    def copy_assets(self):
        """Copy static assets to output directory."""
        # Copy images
        images_src = self.root_dir / "images"
        images_dest = self.dist_dir / "images"
        if images_src.exists():
            if images_dest.exists():
                shutil.rmtree(images_dest)
            shutil.copytree(images_src, images_dest)
            print(f"Copied images to {images_dest}")
        
        # Copy scripts
        scripts_src = self.root_dir / "scripts"  
        scripts_dest = self.dist_dir / "scripts"
        if scripts_src.exists():
            if scripts_dest.exists():
                shutil.rmtree(scripts_dest)
            shutil.copytree(scripts_src, scripts_dest)
            print(f"Copied scripts to {scripts_dest}")
    
    def build(self):
        """Main build function."""
        print("Building Boston Robot Hackers website...")
        print(f"Using theme: {self.theme_config.get('active_theme', 'tailwind')}")
        
        # Copy static assets
        self.copy_assets()
        
        # Generate syntax highlighting CSS
        self.generate_pygments_css('default')
        
        # Build the main page
        self.build_index()
        
        print("Build complete!")


def main():
    """Main entry point."""
    builder = WebsiteBuilder()
    builder.build()


if __name__ == '__main__':
    main()