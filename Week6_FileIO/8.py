import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    images.append(arg)
    
for img_path in images:
    img = Image.open(img_path)
    img.show()
    img.save(f"new_image{img_path}")
    