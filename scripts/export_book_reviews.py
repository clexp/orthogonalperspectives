#!/usr/bin/env python3
"""
Export book reviews from Pelican format to Django-compatible format
"""

import os
import json
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

def convert_to_django_format(metadata, content, filename):
    """Convert Pelican format to Django-compatible format"""
    
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
    
    # Extract author from metadata or content
    author = metadata.get('Author', 'Unknown')
    
    # Create description from summary or first few lines
    description = metadata.get('Summary', '')
    if not description and content:
        # Use first paragraph as description
        first_para = content.split('\n\n')[0] if '\n\n' in content else content[:200]
        description = first_para[:200] + '...' if len(first_para) > 200 else first_para
    
    # Extract rating if available
    rating = None
    if 'Rating' in metadata:
        try:
            rating = int(metadata['Rating'])
        except:
            rating = None
    
    # Build Django-compatible data
    book_data = {
        'title': title,
        'author': author,
        'review_date': date_formatted,
        'description': description,
        'content': content,
        'rating': rating,
        'source_file': filename
    }
    
    return book_data

def export_book_reviews():
    """Export all book reviews to Django-compatible format"""
    
    # Create export directory
    export_dir = Path('export_book_reviews')
    export_dir.mkdir(exist_ok=True)
    
    # Source directory
    source_dir = Path('content/Literature')
    
    if not source_dir.exists():
        print(f"Source directory {source_dir} not found!")
        return
    
    exported_count = 0
    all_books = []
    
    for md_file in source_dir.glob('*.md'):
        print(f"Processing: {md_file.name}")
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse Pelican format
            metadata, body_content = parse_pelican_frontmatter(content)
            
            # Convert to Django format
            book_data = convert_to_django_format(metadata, body_content, md_file.name)
            all_books.append(book_data)
            
            # Write individual JSON file
            json_file = export_dir / f"{md_file.stem}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(book_data, f, indent=2, ensure_ascii=False)
            
            exported_count += 1
            print(f"  ✓ Exported: {json_file}")
            
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
    
    # Write combined JSON file
    combined_file = export_dir / 'all_books.json'
    with open(combined_file, 'w', encoding='utf-8') as f:
        json.dump(all_books, f, indent=2, ensure_ascii=False)
    
    print(f"\nExport complete! {exported_count} books exported to {export_dir}/")
    print(f"Combined file: {combined_file}")
    print(f"\nNext steps:")
    print(f"1. Get the Django schema from books.clexp.net")
    print(f"2. Create a Django management command to import the JSON data")
    print(f"3. Run the import command on your Django site")
    print(f"4. Remove the Literature category from this Pelican site")

if __name__ == "__main__":
    export_book_reviews() 