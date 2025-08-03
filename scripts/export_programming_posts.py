#!/usr/bin/env python3
"""
Export programming posts from Pelican format to Zola format
"""

import os
import re
from pathlib import Path
from datetime import datetime

def parse_pelican_frontmatter(content):
    """Parse Pelican frontmatter and return metadata"""
    lines = content.split('\n')
    metadata = {}
    content_start = 0
    
    for i, line in enumerate(lines):
        if line.strip() == '':
            content_start = i + 1
            break
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            metadata[key] = value
    
    return metadata, '\n'.join(lines[content_start:])

def convert_to_zola_format(metadata, content, filename):
    """Convert Pelican format to Zola format"""
    
    # Extract title from filename if not in metadata
    title = metadata.get('Title', filename.replace('.md', '').replace('_', ' ').title())
    
    # Convert date format
    date_str = metadata.get('Date', '')
    if date_str:
        try:
            # Parse various date formats
            if '-' in date_str:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            else:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            date_formatted = date_obj.strftime('%Y-%m-%d')
        except:
            date_formatted = '2025-01-01'  # Default date
    else:
        date_formatted = '2025-01-01'
    
    # Convert tags
    tags = []
    if 'Tags' in metadata:
        tag_str = metadata.get('Tags', '')
        if tag_str:
            # Parse tags (remove # and split)
            tags = [tag.strip('#').strip() for tag in tag_str.split(',') if tag.strip()]
    
    # Add category as tag
    if 'Category' in metadata:
        category = metadata.get('Category', '').lower()
        if category and category not in tags:
            tags.append(category)
    
    # Create description from summary or first few lines
    description = metadata.get('Summary', '')
    if not description and content:
        # Use first paragraph as description
        first_para = content.split('\n\n')[0] if '\n\n' in content else content[:200]
        description = first_para[:200] + '...' if len(first_para) > 200 else first_para
    
    # Build Zola frontmatter
    zola_frontmatter = f"""+++
title = "{title}"
date = "{date_formatted}"
description = "{description}"
tags = {tags}
categories = ["technical"]
+++

"""
    
    return zola_frontmatter + content

def export_programming_posts():
    """Export all programming posts to Zola format"""
    
    # Create export directory
    export_dir = Path('export_programming_posts')
    export_dir.mkdir(exist_ok=True)
    
    # Source directory
    source_dir = Path('content/Programming')
    
    if not source_dir.exists():
        print(f"Source directory {source_dir} not found!")
        return
    
    exported_count = 0
    
    for md_file in source_dir.glob('*.md'):
        print(f"Processing: {md_file.name}")
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse Pelican format
            metadata, body_content = parse_pelican_frontmatter(content)
            
            # Convert to Zola format
            zola_content = convert_to_zola_format(metadata, body_content, md_file.stem)
            
            # Write to export directory
            export_file = export_dir / md_file.name
            with open(export_file, 'w', encoding='utf-8') as f:
                f.write(zola_content)
            
            exported_count += 1
            print(f"  ✓ Exported: {export_file}")
            
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
    
    print(f"\nExport complete! {exported_count} posts exported to {export_dir}/")
    print(f"\nNext steps:")
    print(f"1. Review the exported posts in {export_dir}/")
    print(f"2. Copy them to your Zola site")
    print(f"3. Remove the Programming category from this Pelican site")

if __name__ == "__main__":
    export_programming_posts() 