from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

window = Tk() 
window.title("Face Recognition")
window.geometry("770x500")
bg = PhotoImage(file = "C:/Users/acer/Documents/GitHub/Algeo02-21010/doc/bg.png")
bg_image = Label(window, image = bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)
window.resizable(False, False)

def open_folder():
  global folder_path
  filename = filedialog.askdirectory()
  label_folder = Label(window, text = filename, font = ("Arial", 12), bg = "white", fg = "black", width = 15, height = 1, anchor = "w")
  label_folder.place(x = 250, y = 200)

def open_image():
  global image_path
  filename = filedialog.askopenfilename(title = "Select image", filetype = (("jpg files", "*.jpg"), ("all files", "*.*")))
  label_image = Label(window, text = filename, font = ("Arial", 5), bg = "white", fg = "black", height = 1, anchor = "w")
  img = Image.open(filename)
  img = img.resize((165, 220), Image.ANTIALIAS)
  label_image.place(x = 36, y = 305)
  img = ImageTk.PhotoImage(img)
  my_label = Label(image = img)
  my_label.image = img
  my_label.place(x = 235, y = 150)

button_label = Button(window, text = "Choose Folder", command = open_folder, font = ("Arial Bold", 14), fg = "#925FF0", bg = "white", activebackground = "white", activeforeground = "white", bd = 0)
button_label.place(x = 36, y = 200)

button_image = Button(window, text = "Choose Image", command = open_image, font = ("Arial Bold", 14), fg = "#925FF0", bg = "white", activebackground = "white", activeforeground = "white", bd = 0)
button_image.place(x = 36, y = 275)

window.mainloop()