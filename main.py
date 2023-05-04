from win32 import win32gui
import win32ui
from ctypes import windll
import tkinter as tk
from PIL import ImageTk, Image
import os
import pytesseract
import re

# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'


def GetImage(name):
	hwnd = win32gui.FindWindow(name, None)

	if hwnd != 0:
		capture(hwnd, f"{name}.png")


def capture(hwnd, filename, size=(1920, 1080)):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    print(right, left, top, bot)

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, size[0], size[1])

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer('RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)


    if result == 1:
        # print(f"save {filename}")
        im.save(filename)
    else:
        print("PrintWindow failed")
    return im


    

# hide menubar
# root.overrideredirect(True)
image_path = "Notepad.png"

# canvas vs photo phai la bien toan cuc
canvas = None
photo = None

def update_image():
    global image_path, canvas, photo

    GetImage("Notepad")
    img = Image.open(image_path)
    # Chuyển đổi hình ảnh thành đối tượng PhotoImage của tkinter
    photo = ImageTk.PhotoImage(img)

    custom_config = r'tessedit_char_whitelist=0123456789'

    text = pytesseract.image_to_string(img)
    # text = ''.join(re.findall(r'\d', text))
    
    numbers = ''
    print(text)
    for char in text:
        if char.isdigit():
            numbers += char
    text = numbers

    # canvas.delete("all")
    
    # font = ('Arial', 50)
    # canvas.create_text(100, 100, text=text, font=font)

    canvas.delete("all")
    canvas.create_image(0, 0, anchor='nw', image=photo)

    
    canvas.after(100, update_image)




root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

update_image()


root.mainloop()

