from win32 import win32gui
import win32ui
from ctypes import windll
from PIL import ImageTk, Image

def GetImage(name):
    hwnd = win32gui.FindWindow(name, None)
    # print("getimage")
    if hwnd != 0:
        capture(hwnd, f"{name}.bmp")
        return True
    return False


def capture(hwnd, filename, size=(400, 400)):
    # left, top, right, bot = win32gui.GetWindowRect(hwnd)
    # w = right - left
    # h = bot - top

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