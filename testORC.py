import pytesseract
from PIL import Image

# Load image
img = Image.open('Notepad.png')

custom_config = r'tessedit_char_whitelist=0123456789'
text = pytesseract.image_to_string(img, config=custom_config)

# Print the text
print(text)
