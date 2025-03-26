import os
import re

DEFAULT_IMAGE = '/images/apple-touch-icon_thumb.png'
DEFAULT_FULL_IMAGE = '/images/apple-touch-icon.png'

def process_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # First standardize any existing 'cover:' or 'thumbnail:' to 'Cover:'
    content = re.sub(r'^(cover|thumbnail):\s*', 'Cover: ', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # Check if file already has a Cover field
    if 'Cover:' in content:
        return
    
    # Check if file already has an image in content
    if '![' in content or '](' in content:
        return
    
    # Add Cover field after the metadata section
    metadata_end = content.find('\n\n')
    if metadata_end == -1:
        metadata_end = content.find('\n')
    
    new_content = content[:metadata_end] + f'\nCover: {DEFAULT_IMAGE}\n' + content[metadata_end:]
    
    # Find the second heading
    headings = list(re.finditer(r'^# .*$', new_content, re.MULTILINE))
    if len(headings) >= 2:
        second_heading_pos = headings[1].start()
        new_content = new_content[:second_heading_pos] + f'\n\n![Default cover image]({DEFAULT_FULL_IMAGE})\n\n' + new_content[second_heading_pos:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and not file.startswith('SUMMARY'):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path)

if __name__ == '__main__':
    content_dir = 'content'
    process_directory(content_dir) 