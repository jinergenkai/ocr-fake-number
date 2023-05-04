
import tkinter as tk
from PIL import ImageTk, Image
import os
import pytesseract
import re

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
from src.getwindow import *

# hide menubar
# root.overrideredirect(True)
image_path = "Notepad.png"

# canvas vs photo phai la bien toan cuc
canvas = None
photo = None

def update_image():
    global image_path, canvas, photo

    if GetImage("Notepad") == False:
        return
    img = Image.open(image_path)
    # Chuyển đổi hình ảnh thành đối tượng PhotoImage của tkinter
    photo = ImageTk.PhotoImage(img)

    custom_config = r'tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(img, config=custom_config)
    numbers = ''
    for char in text:
        if char.isdigit():
            numbers += char
    text = numbers

    # canvas.delete("all")
    
    # font = ('Arial', 50)
    # canvas.create_text(100, 100, text=text, font=font)

    canvas.delete("all")
    canvas.create_image(0, 0, anchor='nw', image=photo)

    
    canvas.after(10, update_image)


root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()
update_image()
root.mainloop()

