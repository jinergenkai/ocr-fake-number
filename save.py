from win32 import win32gui
import win32ui
from ctypes import windll
import tkinter as tk
from PIL import ImageTk, Image
import os



def GetImage(name):
	hwnd = win32gui.FindWindow(name, None)

	if hwnd != 0:
		capture(hwnd, f"{name}.png")


def capture(hwnd, filename):
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    print(result)

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
        print(f"save {filename}")
        im.save(filename)
    else:
        print("PrintWindow failed")
    return im


    

# hide menubar
# root.overrideredirect(True)
image_path = "Notepad.png"
canvas = None
photo = None

def update_image():
    global image_path, canvas, photo

    GetImage("Notepad")
    img = Image.open(image_path)
    # Chuyển đổi hình ảnh thành đối tượng PhotoImage của tkinter
    photo = ImageTk.PhotoImage(img)

    canvas.delete("all")
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.after(100, update_image)


root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

update_image()


root.mainloop()

