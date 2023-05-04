# -*- coding: utf-8 -*-

#PrintWindowにてウィンドウ画像の取得を試みる

#https://stackoverflow.com/questions/19695214/python-screenshot-of-inactive-window-printwindow-win32gui
#元ネタは２系だが↓をしてimportを変えたら動きました
#pip install pywin32
#pip install win32gui
#pip install Image


#取れなかったもの（真っ黒になる）
#   chrome
#   Windows Media Player
#   電卓
#   Snes9X
#   SNESGT

#取れたもの
#   PCastTV3
#   ペイント
#   VLC
#   NNNesterJ
#   VirtuaNES

#基準がわからないがGPU使っているようなものは取れない?
#PrintWindowは窓が隠れていても取得できるので便利だが ゲーム系はだめそう。。。


from win32 import win32gui
from PIL import Image
import win32ui
from ctypes import windll
import re
import os



def callback(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        # if title != "Notepad":
        #     return
        cls = win32gui.GetClassName(hwnd)
        name = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '', title) #ファイル名に使えない文字を除去

        print(f"title:{title}  class:{cls}")
        if title != "":
            capture(hwnd, f"{cls}.png")


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


    
if __name__ == '__main__':
    win32gui.EnumWindows(callback, None)

