from tkinter import *
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image
import PIL as pill
from main import *
import cv2 as cv2
import os
import timeit

window = ctk.CTk()
window.title("!FullTuru Face Recognition")
window.geometry("770x500")
window.resizable(False, False)
bg = PhotoImage(file = "frontend/background.png")
bg_label = Label(window, image = bg)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

get_var_folder = StringVar()
get_var_image = StringVar()

def open_folder():
  folder_path = filedialog.askdirectory(initialdir = "/", title = "Select folder")
  get_var_folder.set(folder_path)

def open_image(): 
  image_path = filedialog.askopenfilename(initialdir = "/", title = "Select image", filetype = (("jpg files", "*.jpg"), ("all files", "*.*")))
  get_var_image.set(image_path)
  print(image_path)
  print(get_var_image)
  img = Image.open(image_path)
  img = ImageTk.PhotoImage(img.resize((256, 256)))
  my_label = Label(image = img)
  my_label.image = img
  my_label.place(x = 300, y = 145)

def main():
  start = timeit.default_timer()
  eigenFace, mean, eigenVec, himpunan = dataset_processing(get_var_folder.get())
  hasil, persentase, treshold, min = image_processing(get_var_image.get(), mean, eigenFace, eigenVec, himpunan)
  if  min<treshold:
    img = pill.Image.fromarray(hasil)
    img = img.resize((256, 256))
    img = ImageTk.PhotoImage(img)
    my_label = Label(window, image = img)
    my_label.image = img
    my_label.place(x = 630, y = 145)
    persentage_label = Label(window, text = "Persentase : "+str(persentase)+"%", font = ("Arial", 11))
    persentage_label.place(x = 630, y = 460)
  else:
    error_tabel = Label(window, text = "Tidak ada wajah yang cocok", font = ("Arial", 11))
    error_tabel.place(x = 600, y = 160)
  stop = timeit.default_timer()
  Time = round(stop - start, 3)


  time_label = Label(window, text = "Execution time: " + str(Time) + " s", font = ("Arial", 11))
  time_label.place(x = 630, y = 420)

button_folder = ctk.CTkButton(window, text = "Choose Folder", command = open_folder, cursor="hand2")
button_folder.place(x = 36, y = 200)

button_image = ctk.CTkButton(window, text = "Choose Image", command = open_image, cursor="hand2")
button_image.place(x = 36, y = 275)

button_scan = ctk.CTkButton(window, text = "SCAN", command = main, cursor="hand2")
button_scan.place(x = 36, y = 125)

window.mainloop()