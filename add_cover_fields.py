import os
import re
from pathlib import Path
from PIL import Image

def create_thumbnail(image_path, size=(200, 200)):
    """Create a thumbnail of the image if it doesn't exist."""
    try:
        thumb_path = str(image_path).replace('.', '_thumb.')
        if os.path.exists(thumb_path):
            return thumb_path
            
        with Image.open(image_path) as img:
            # Convert to RGB if necessary (for PNG with transparency)
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Create thumbnail
            img.thumbnail(size, Image.Resampling.LANCZOS)
            
            # Save thumbnail
            img.save(thumb_path, 'JPEG', quality=85)
            print(f"Created thumbnail: {thumb_path}")
        return thumb_path
    except Exception as e:
        print(f"Error creating thumbnail for {image_path}: {e}")
        return None

def add_cover_field(file_path):
    """Add Cover field with thumbnail path if file has an image but no Cover field."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has a Cover field
        if re.search(r'^Cover:', content, re.MULTILINE):
            return
        
        # Look for markdown image syntax
        image_match = re.search(r'!\[.*?\]\((.*?)\)', content)
        if not image_match:
            return
        
        # Get the image path
        image_path = image_match.group(1)
        
        # Create thumbnail if needed
        thumb_path = create_thumbnail(image_path)
        if not thumb_path:
            return
        
        # Add Cover field after the title
        title_match = re.search(r'^title:.*$', content, re.MULTILINE)
        if not title_match:
            return
        
        insert_pos = title_match.end()
        new_content = content[:insert_pos] + f'\nCover: {thumb_path}\n' + content[insert_pos:]
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Added Cover field to: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_directory(directory):
    """Process all markdown files in the directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                add_cover_field(file_path)

if __name__ == "__main__":
    # Process the content directory
    content_dir = "content"
    print(f"Processing markdown files in {content_dir}")
    process_directory(content_dir)
    print("Cover field addition complete!") 