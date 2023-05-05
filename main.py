
import tkinter as tk
from PIL import ImageTk, Image
import pytesseract
import re

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
from src.getwindow import *
from src.config import *

canvas = None
photo = None


def getNumbers(text):
    numbers = ''
    for char in text:
        if char.isdigit():
            numbers += char 
    return numbers if numbers != '' else None

def update_image():
    global image_path, canvas, photo

    if GetImage(image_name) == False:
        return
    img = Image.open(image_name + ".bmp")
    photo = ImageTk.PhotoImage(img)

    custom_config = r'tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(img, config=custom_config)
    text = getNumbers(text)

    canvas.delete("all")
    
    # font = ('Arial', 50)
    # canvas.create_text(100, 100, text=text, font=font)

    canvas.create_image(0, 0, anchor='nw', image=photo)

    
    canvas.after(delay, update_image)


root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
update_image()

root.wm_attributes("-topmost", onTop)
root.overrideredirect(hideMenuBar)

root.mainloop()

