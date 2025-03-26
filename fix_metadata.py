import os
import re
from datetime import datetime

def add_missing_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get filename without extension for title
    filename = os.path.splitext(os.path.basename(file_path))[0]
    
    # Check if it's a SUMMARY.md file
    is_summary = filename == 'SUMMARY'
    
    # Prepare new metadata
    new_metadata = []
    
    # Add title if missing (for SUMMARY.md files)
    if is_summary and 'title:' not in content:
        new_metadata.append(f'title: {os.path.basename(os.path.dirname(file_path))} Summary')
    
    # Add date if missing (for all files)
    if 'date:' not in content:
        # Try to find date in filename or use current date
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
        if date_match:
            date_str = date_match.group(1)
        else:
            date_str = datetime.now().strftime('%Y-%m-%d')
        new_metadata.append(f'date: {date_str}')
    
    # Fix duplicate status issue
    if 'Status:' in content:
        # Remove any duplicate Status lines
        lines = content.split('\n')
        status_lines = [i for i, line in enumerate(lines) if line.startswith('Status:')]
        if len(status_lines) > 1:
            # Keep only the first Status line
            for i in status_lines[1:]:
                lines[i] = ''
            content = '\n'.join(line for line in lines if line)
    
    if new_metadata:
        # Find where to insert new metadata
        if 'title:' in content:
            # Insert after title
            insert_pos = content.find('title:') + len('title:')
            insert_pos = content.find('\n', insert_pos) + 1
        else:
            # Insert at start
            insert_pos = 0
        
        # Insert new metadata
        new_content = content[:insert_pos] + '\n'.join(new_metadata) + '\n' + content[insert_pos:]
        
        # Ensure there's a blank line after metadata
        if not new_content.startswith('\n\n'):
            new_content = new_content.replace('\n\n', '\n', 1)
            new_content = new_content.replace('\n', '\n\n', 1)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                add_missing_metadata(file_path)

if __name__ == '__main__':
    content_dir = 'content'
    process_directory(content_dir) 