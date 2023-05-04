# importing image object from PIL
from PIL import Image, ImageTk
import time
  
# creating an image object
im = Image.open(r"123.png")
im1 = im.tobytes("xbm", "rgb")
img = Image.frombuffer("L", (4, 4), im1, 'raw', "L", 0, 1)

# img.show()
print(type(img))  
# creating list 
img2 = list(img.getdata())
# print(img.tobitmap())


time.sleep(300)

photo1 = ImageTk.PhotoImage(img)

# # Tạo một cửa sổ Tkinter và hiển thị hình ảnh
# root = tk.Tk()
# label = tk.Label(root, image=photo1)
# label.pack()
# root.mainloop()



# print(img.getprojection())
# # import numpy as np

# # # Tạo một mảng numpy từ mảng giá trị
# # data = np.array(img2, dtype=np.uint8)

# # # Reshape mảng thành kích thước ảnh (2x2x3)
# # data = data.reshape((2, 2, 3))

# # # Tạo ảnh từ mảng giá trị
# imgTK = Image.fromarray(img2, 'RGB')

# # image = Image.frombytes('RGBA', (400, 400), img, 'raw')

# # BytesIO