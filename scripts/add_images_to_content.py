import os
import re
from pathlib import Path

def add_image_to_content(file_path):
    """Add full-size image to markdown content if it has a Cover field."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file has a Cover field
        cover_match = re.search(r'Cover:\s*(/images/.*?\.(jpg|jpeg|png|gif))', content)
        if not cover_match:
            return
        
        # Get the full-size image path (remove _thumb if present)
        cover_path = cover_match.group(1)
        full_image_path = cover_path.replace('_thumb.', '.')
        
        # Check if image is already in content
        if f'![{full_image_path}]' in content:
            return
        
        # Find the first heading after metadata
        first_heading = re.search(r'^#\s+.*$', content, re.MULTILINE)
        if not first_heading:
            return
        
        # Insert the image after the first heading
        insert_pos = first_heading.end()
        new_content = content[:insert_pos] + f'\n\n![{full_image_path}]({full_image_path})\n\n' + content[insert_pos:]
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added image to: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory):
    """Process all markdown files in the directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                add_image_to_content(file_path)

if __name__ == "__main__":
    # Process the content directory
    content_dir = "content"
    print(f"Processing markdown files in {content_dir}")
    process_directory(content_dir)
    print("Image addition complete!") 