from win32 import win32gui
import win32ui
from ctypes import windll
from PIL import ImageTk, Image
from src.config import image_name, width, height


hwnd = win32gui.FindWindow(image_name, None)

def GetImage(image_name):
    if hwnd != 0:
        return capture(hwnd, f"{image_name}.bmp", (width, height))
    return False


def capture(hwnd, filename, size=(400, 400)):

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

    if result == 1:
        im.save(filename)
        return True
    else:
        return False