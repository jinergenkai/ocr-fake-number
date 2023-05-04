import win32gui
import win32ui
import win32con
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

# Xác định id của cửa sổ bạn muốn stream
hwnd = win32gui.FindWindow(None, "Tên của cửa sổ muốn stream")

# Tính toán kích thước của cửa sổ
left, top, right, bottom = win32gui.GetClientRect(hwnd)
width, height = right - left, bottom - top

# Tạo một màn hình DC để lưu trữ nội dung của cửa sổ
hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()

# Tạo một bitmap để lưu trữ nội dung của cửa sổ
saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
saveDC.SelectObject(saveBitMap)

# Đưa nội dung của cửa sổ vào bitmap
result = win32gui.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)

# Chuyển đổi bitmap thành một mảng numpy và sau đó thành một đối tượng hình ảnh Image
im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

# Hiển thị hình ảnh bằng Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
photo = ImageTk.PhotoImage(im)
canvas.create_image(0, 0, anchor='nw', image=photo)
root.mainloop()
