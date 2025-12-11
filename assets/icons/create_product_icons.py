from PIL import Image, ImageDraw
import os

# Create product icons
icons = {
    'shield.png': (48, 48, '#3faa56'),  # For CHIMERA
    'robot.png': (48, 48, '#4dff7c'),    # For AI Assistant
    'lightning.png': (48, 48, '#3faa56'), # For API Gateway
    'rocket.png': (48, 48, '#4dff7c'),   # For Cloud Platform
    'lock.png': (48, 48, '#3faa56'),     # For Security Framework
}

for filename, (width, height, color) in icons.items():
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Convert hex to RGB
    r = int(color[1:3], 16)
    g = int(color[3:5], 16)
    b = int(color[5:7], 16)
    
    if 'shield' in filename:
        # Draw a shield
        draw.polygon([(24, 4), (40, 12), (40, 32), (24, 44), (8, 32), (8, 12)], fill=(r, g, b, 255))
    elif 'robot' in filename:
        # Draw a robot head
        draw.rectangle([12, 16, 36, 40], fill=(r, g, b, 255))
        draw.ellipse([16, 22, 22, 28], fill=(255, 255, 255, 255))
        draw.ellipse([26, 22, 32, 28], fill=(255, 255, 255, 255))
        draw.rectangle([18, 32, 30, 34], fill=(255, 255, 255, 255))
    elif 'lightning' in filename:
        # Draw a lightning bolt
        draw.polygon([(28, 4), (18, 24), (26, 24), (20, 44), (32, 20), (24, 20)], fill=(r, g, b, 255))
    elif 'rocket' in filename:
        # Draw a rocket
        draw.polygon([(24, 4), (32, 16), (16, 16)], fill=(r, g, b, 255))
        draw.rectangle([20, 16, 28, 36], fill=(r, g, b, 255))
        draw.polygon([(20, 36), (14, 44), (20, 40)], fill=(r, g, b, 255))
        draw.polygon([(28, 36), (34, 44), (28, 40)], fill=(r, g, b, 255))
    elif 'lock' in filename:
        # Draw a lock
        draw.arc([16, 8, 32, 24], 0, 180, fill=(r, g, b, 255), width=3)
        draw.rectangle([12, 20, 36, 40], fill=(r, g, b, 255))
        draw.ellipse([22, 26, 26, 30], fill=(255, 255, 255, 255))
    
    img.save(filename)
    print(f"Created {filename}")

