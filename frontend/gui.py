from tkinter import *
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image

window = ctk.CTk()
window.title("Face Recognition")
window.geometry("770x500")
window.resizable(False, False)

get_var_folder = StringVar()
get_var_image = StringVar()

def open_folder():
  folder_path = filedialog.askdirectory(initialdir = "/", title = "Select folder")
  get_var_folder.set(folder_path)

def open_image(): 
  image_path = filedialog.askopenfilename(title = "Select image", filetype = (("jpg files", "*.jpg"), ("all files", "*.*")))
  get_var_image.set(image_path)
  img = Image.open(image_path)
  img = ImageTk.PhotoImage(img.resize((256, 256), Image.ANTIALIAS))
  my_label = Label(image = img)
  my_label.image = img
  my_label.place(x = 300, y = 145)

button_folder = ctk.CTkButton(window, text = "Choose Folder", command = open_folder, cursor="hand2")
button_folder.place(x = 36, y = 200)

button_image = ctk.CTkButton(window, text = "Choose Image", command = open_image, cursor="hand2")
button_image.place(x = 36, y = 275)

button_scan = ctk.CTkButton(window, text = "SCAN", command = open_image, cursor="hand2")
button_scan.place(x = 36, y = 125)

window.mainloop()



