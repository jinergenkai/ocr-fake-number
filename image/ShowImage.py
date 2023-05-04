from PIL import Image
import os

# Get list of image files in current directory
files = [file for file in os.listdir() if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]

print(len(files))
# Loop through files and show images
for file in files:
    with Image.open(file) as img:
        img.show()