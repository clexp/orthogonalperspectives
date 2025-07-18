#!/usr/bin/env python3
"""
Create default images for different categories.
This script sets up a system of default images that can be used
when specific cover images are not available.
"""

import os
import shutil
from pathlib import Path

def create_default_images():
    """Create default images for different categories."""
    
    # Define the images directory
    images_dir = Path("content/images")
    
    # Create default images directory
    defaults_dir = images_dir / "defaults"
    defaults_dir.mkdir(exist_ok=True)
    
    # Define category-specific default images
    category_defaults = {
        "Machine Learning": "ml_default.png",
        "Maths": "maths_default.png", 
        "Literature": "literature_default.png",
        "Programming": "programming_default.png",
        "Python": "python_default.png",
        "Reflections": "reflections_default.png",
        "Podcasts": "podcasts_default.png",
        "Project": "project_default.png"
    }
    
    # Create a generic default image (copy existing apple-touch-icon)
    generic_default = images_dir / "apple-touch-icon_thumb.png"
    if generic_default.exists():
        shutil.copy2(generic_default, defaults_dir / "generic_default.png")
        print(f"✅ Created generic default image")
    
    # Create category-specific defaults (for now, copy the generic)
    for category, filename in category_defaults.items():
        if generic_default.exists():
            shutil.copy2(generic_default, defaults_dir / filename)
            print(f"✅ Created default for {category}: {filename}")
    
    print(f"\n📁 Default images created in: {defaults_dir}")
    print("💡 You can replace these with category-specific images later")

if __name__ == "__main__":
    create_default_images() 