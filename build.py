#!/usr/bin/env python3
"""
Build script for Boston Robot Hackers website.
Processes markdown files with front matter and generates JSON for the site.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

import frontmatter
import markdown
from pygments.formatters import HtmlFormatter


def setup_markdown_processor():
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


def generate_pygments_css(theme='default'):
    """Generate Pygments CSS for syntax highlighting."""
    formatter = HtmlFormatter(style=theme, cssclass='highlight')
    css_content = formatter.get_style_defs('.highlight')
    
    css_file = Path('generated/syntax.css')
    css_file.write_text(css_content)
    print(f"Generated syntax highlighting CSS: {css_file}")


def process_markdown_file(file_path: Path, md_processor) -> Dict[str, Any]:
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
            'emoji': metadata.get('emoji', 'NEWS'),  # Legacy support
            'card-text': metadata.get('card-text', metadata.get('emoji', 'NEWS')),
            'card-graphic-custom': metadata.get('card-graphic-custom'),
            'card-graphic-builtin': metadata.get('card-graphic-builtin'),
            'excerpt': metadata.get('excerpt', ''),
            'content': html_content,
            'metadata': metadata
        }
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_card_graphic_html(post: Dict[str, Any]) -> str:
    """Generate HTML for card graphic based on front matter."""
    card_text = post.get('card-text', post.get('emoji', 'INFO'))
    
    # Check for custom image
    if post.get('card-graphic-custom'):
        custom_path = post['card-graphic-custom']
        return f'<div class="card-image custom-image" style="background-image: url(\'{custom_path}\')"><span class="card-text">{card_text}</span></div>'
    
    # Check for built-in image
    elif post.get('card-graphic-builtin'):
        builtin_type = post['card-graphic-builtin']
        return f'<div class="card-image builtin-image {builtin_type}"><span class="card-text">{card_text}</span></div>'
    
    # Default to text-only
    else:
        return f'<div class="card-image text-only">{card_text}</div>'


def generate_news_html(posts: List[Dict[str, Any]]) -> str:
    """Generate HTML for news cards."""
    html_cards = []
    
    for post in posts:
        # Format date for display
        date_str = post['date']
        if isinstance(date_str, str):
            try:
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
                formatted_date = date_obj.strftime('%B %d, %Y')
            except ValueError:
                formatted_date = date_str
        else:
            formatted_date = str(date_str)
        
        # Generate card graphic HTML
        card_graphic = generate_card_graphic_html(post)
        
        card_html = f'''
                    <div class="news-card">
                        {card_graphic.replace('card-image', 'news-image')}
                        <div class="news-content">
                            <h4 class="news-title">{post['title']}</h4>
                            <p class="news-text">{post['excerpt']}</p>
                            <div class="news-meta">{formatted_date}</div>
                        </div>
                    </div>'''
        html_cards.append(card_html)
    
    return ''.join(html_cards)


def build_whatsnew():
    """Build the What's New section from markdown files."""
    whatsnew_dir = Path('whatsnew')
    if not whatsnew_dir.exists():
        print(f"Warning: {whatsnew_dir} directory not found")
        return
    
    # Set up markdown processor
    md_processor = setup_markdown_processor()
    
    # Process all markdown files
    posts = []
    for md_file in whatsnew_dir.glob('*.md'):
        post_data = process_markdown_file(md_file, md_processor)
        if post_data:
            posts.append(post_data)
    
    # Sort by date (newest first) 
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate HTML for news cards
    news_html = generate_news_html(posts)
    
    # Update the main HTML file 
    update_html_with_content(news_html)
    
    # Also save JSON for potential future use
    output_file = Path('generated/whatsnew.json')
    output_file.parent.mkdir(exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(posts)} posts and updated HTML")


def update_html_with_content(news_html: str):
    """Update the main HTML file with generated content."""
    html_file = Path('index.html')
    content = html_file.read_text()
    
    # Find the news content placeholder and replace it
    start_marker = '<div class="news-grid" id="whats-new-content">'
    end_marker = '</div>\n                <button class="btn"'
    
    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker, start_pos)
    
    if start_pos != -1 and end_pos != -1:
        # Replace the content between markers
        new_content = (
            content[:start_pos + len(start_marker)] +
            news_html +
            '\n                ' +
            content[end_pos:]
        )
        
        html_file.write_text(new_content)
        print("Updated index.html with generated content")
    else:
        print("Warning: Could not find content markers in index.html")


def main():
    """Main build function."""
    print("Building Boston Robot Hackers website...")
    
    # Generate syntax highlighting CSS
    generate_pygments_css('default')
    
    # Build What's New section
    build_whatsnew()
    
    print("Build complete!")


if __name__ == '__main__':
    main()