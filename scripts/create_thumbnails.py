try:
    from PIL import Image
except ImportError:
    from pillow import Image
import os
from pathlib import Path

def create_thumbnail(image_path, size=(200, 200)):
    """Create a thumbnail of the image with the specified size."""
    try:
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
            
            # Create thumbnail filename
            thumb_path = str(image_path).replace('.', '_thumb.')
            
            # Save thumbnail
            img.save(thumb_path, 'JPEG', quality=85)
            print(f"Created thumbnail: {thumb_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_directory(directory):
    """Process all images in the directory and its subdirectories."""
    # Supported image formats
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
    
    # Walk through directory
    for root, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in image_extensions:
                image_path = os.path.join(root, file)
                create_thumbnail(image_path)

if __name__ == "__main__":
    # Process the images directory
    images_dir = "content/images"
    print(f"Processing images in {images_dir}")
    process_directory(images_dir)
    print("Thumbnail creation complete!") 