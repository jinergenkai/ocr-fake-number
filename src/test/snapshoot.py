import ctypes
import win32gui
from ctypes import wintypes

# Load user32 DLL
user32 = ctypes.WinDLL('user32.dll')

# Define FindWindow and PrintWindow functions
FindWindow = user32.FindWindowW
FindWindow.restype = wintypes.HWND
FindWindow.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]

PrintWindow = user32.PrintWindow
PrintWindow.restype = wintypes.BOOL
PrintWindow.argtypes = [wintypes.HWND, wintypes.HDC, wintypes.UINT]

# Get window handle
window_title = "Task Manager"
# window_class = "Task Manager"
# hwnd = FindWindow(window_class, window_title)
hwnd = FindWindow(None, window_title)

# Capture window screenshot
if hwnd:
    rect = win32gui.GetWindowRect(hwnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    hdc = user32.GetDC(hwnd)
    bmp = win32gui.CreateCompatibleBitmap(hdc, width, height)
    memdc = user32.CreateCompatibleDC(hdc)
    # user32.SelectObject(memdc, bmp)
    # PrintWindow(hwnd, memdc, 0)
    # bmpinfo = win32gui.GetBitmapBits(bmp)
    # user32.ReleaseDC(hwnd, hdc)
    # user32.DeleteDC(memdc)
    # win32gui.DeleteObject(bmp)

    # # Write bitmap to file
    # with open("./window.bmp", "wb") as f:
    #     f.write(bmpinfo)
else:
    print("Window not found.")
