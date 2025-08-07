#!/usr/bin/env python3
"""
Generate search index for Pelican site
"""

import json
import os
import re
from pathlib import Path

def clean_text(text):
    """Clean text for search indexing"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def generate_search_index(content_path, output_path):
    """Generate search index from content"""
    
    search_data = []
    content_dir = Path(content_path)
    
    # Process all markdown files
    for md_file in content_dir.rglob('*.md'):
        if md_file.name.startswith('.'):
            continue
            
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse frontmatter and content
            lines = content.split('\n')
            metadata = {}
            body_start = 0
            
            for i, line in enumerate(lines):
                if line.strip() == '':
                    body_start = i + 1
                    break
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()
            
            body_content = '\n'.join(lines[body_start:])
            
            # Extract title and create URL
            title = metadata.get('Title', md_file.stem)
            category = md_file.parent.name if md_file.parent.name != 'pages' else 'pages'
            
            # Create URL based on file structure
            if category == 'pages':
                url = f"/pages/{md_file.stem}.html"
            else:
                url = f"/{md_file.stem}.html"
            
            # Clean content for search
            search_content = clean_text(body_content)
            
            search_data.append({
                'title': title,
                'url': url,
                'content': search_content[:500],  # Limit content length
                'category': category,
                'tags': metadata.get('Tags', '').split() if metadata.get('Tags') else []
            })
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    # Write search index
    output_file = Path(output_path) / 'search_index.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(search_data, f, indent=2, ensure_ascii=False)
    
    print(f"Generated search index with {len(search_data)} articles")
    return output_file

if __name__ == "__main__":
    generate_search_index('content', 'output') 