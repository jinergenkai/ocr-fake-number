import tkinter as tk
from PIL import ImageTk, Image
import os

# Tạo một cửa sổ tkinter
root = tk.Tk()

# hide menubar
# root.overrideredirect(True)

# Tìm tất cả các tệp hình ảnh trong thư mục hiện tại
image_paths = [os.path.join('.', f) for f in os.listdir('.') if f.endswith('.png') or f.endswith('.jpg')]

# Hiển thị mỗi hình ảnh trong một nhãn tkinter
for image_path in image_paths:
    # Load hình ảnh sử dụng thư viện Pillow
    img = Image.open(image_path)

    # Chuyển đổi hình ảnh thành đối tượng PhotoImage của tkinter
    photo = ImageTk.PhotoImage(img)

    # Hiển thị hình ảnh trong một nhãn tkinter
    label = tk.Label(root, image=photo)
    label.pack()

# Chạy vòng lặp chính của cửa sổ tkinter
root.mainloop()
