from PIL import Image, ImageDraw

def create_icon(size, filename):
    img = Image.new('RGB', (size, size), color='#ec4899')
    d = ImageDraw.Draw(img)
    # Draw a simple text or shape
    d.text((size//2-20, size//2-10), "HN", fill=(255, 255, 255))
    img.save(f"frontend/public/icons/{filename}")
    print(f"Created {filename}")

if __name__ == "__main__":
    create_icon(192, "icon-192x192.png")
    create_icon(512, "icon-512x512.png")
