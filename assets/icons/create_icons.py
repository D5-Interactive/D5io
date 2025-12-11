from PIL import Image, ImageDraw
import os

# Create simple SVG icons and save as PNG for now (browsers support PNG more universally)
icons = {
    'logo.png': (64, 64, '#3faa56'),
    'home.png': (32, 32, '#b8d9c1'),
    'products.png': (32, 32, '#b8d9c1'),
    'about.png': (32, 32, '#b8d9c1'),
    'contact.png': (32, 32, '#b8d9c1'),
    'menu.png': (32, 32, '#e8f5eb'),
}

for filename, (width, height, color) in icons.items():
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Convert hex to RGB
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    
    if 'logo' in filename:
        # Draw a leaf-like shape
        draw.ellipse([8, 8, 56, 56], fill=(r, g, b, 255))
        draw.ellipse([20, 16, 48, 52], fill=(r, g, b, 255))
    elif 'home' in filename:
        # Draw a house
        draw.polygon([(16, 8), (28, 16), (4, 16)], fill=(r, g, b, 255))
        draw.rectangle([8, 16, 24, 28], fill=(r, g, b, 255))
    elif 'products' in filename:
        # Draw a box
        draw.rectangle([8, 10, 24, 22], outline=(r, g, b, 255), width=2)
        draw.rectangle([8, 12, 24, 14], fill=(r, g, b, 255))
    elif 'about' in filename:
        # Draw an info circle
        draw.ellipse([6, 6, 26, 26], outline=(r, g, b, 255), width=2)
        draw.ellipse([14, 10, 18, 14], fill=(r, g, b, 255))
        draw.rectangle([14, 16, 18, 24], fill=(r, g, b, 255))
    elif 'contact' in filename:
        # Draw an envelope
        draw.rectangle([4, 10, 28, 22], outline=(r, g, b, 255), width=2)
        draw.polygon([(4, 10), (16, 18), (28, 10)], outline=(r, g, b, 255), width=2)
    elif 'menu' in filename:
        # Draw hamburger menu
        for y in [8, 16, 24]:
            draw.rectangle([6, y, 26, y+2], fill=(r, g, b, 255))
    
    img.save(filename)
    print(f"Created {filename}")

