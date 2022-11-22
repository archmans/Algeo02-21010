from tkinter import *
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image
import PIL as upil
from operation import *
import numpy as np
from img_processing import *
from covarian import *
from step3EigenAlgo import *
from Mean import *
from AlgoritmaEigen import *
import cv2 as cv2
import os

window = ctk.CTk()
window.title("Face Recognition")
window.geometry("770x500")
window.resizable(False, False)

get_var_folder = StringVar()
get_var_image = StringVar()
closest_var = StringVar()

def open_folder():
  folder_path = filedialog.askdirectory(initialdir = "/", title = "Select folder")
  get_var_folder.set(folder_path)
  print(folder_path)
  print(get_var_folder)

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

def proses():
  folderr = get_var_folder.get()
  foto = get_var_image.get()
  print(folderr)
  print(foto)
  fotoo = []
  for filename in os.listdir(folderr):
    fotoo.append(filename)
  #mengambil himpunan gambar
  t = np.array(resize_image(get_image(folderr), (256, 256)))
  print("\nHimpunan Gambar :\n")
  print(t)
  print(t.shape)

  #mencari nilai mean
  mean = Mean(t)
  print("\nMean :\n ")
  print(mean)
  print(mean.shape)

  #mencari selisih
  selisih = []
  for i in range(len(t)):
      selisih.append(KurangMatriks(t[i], mean))
  selisih = abs(np.array(selisih))
  print("\nSelisih :\n")
  print(selisih)
  print(selisih.shape)

  selisihGabungan = concatAllImage(selisih)

  #mencari covarian
  cov = matrix_covarian(selisihGabungan)
  print("\nCovarian :\n")
  print(cov)
  print(cov.shape)

  #mencari eigen
  EigenVal, EigenVec = EigenDariQR(cov)
  print("\nVector Eigen :\n")
  print(EigenVec)
  print(EigenVec.shape)

  #mencari eigen face
  eigenFace = []
  for i in range(len(selisih)):
      eigenFace.append(KaliMatriks(EigenVec, selisih[i]))
  eigenFace = np.array(eigenFace)

  phototest=cv2.resize(cv2.imread(foto, cv2.IMREAD_GRAYSCALE), (256, 256))
  substest=KurangMatriks(phototest,mean)
  tempresult=KaliMatriks(EigenVec,substest)
  lock = []
  for i in range(len(eigenFace)):
      eigenFace[i]=eigenFace[i]-tempresult
      lock.append(np.linalg.norm(eigenFace[i]))
  temp = np.empty((256,256))
  min=lock[0]
  temp=eigenFace[0]
  target = 0
  for i in range(len(lock)):
      if min>lock[i]:
          min=lock[i]
          temp=eigenFace[i]
          target=i

          closest_var = os.path.join(folderr, fotoo[target])
          img2 = upil.Image.open(closest_var)
          img2 = img2.resize((256, 256))
          img2 = ImageTk.PhotoImage(img2)
          my_label2 = Label(window, image = img2)
          my_label2.image = img2
          my_label2.place(x = 630, y = 145)

  print("\nEigen Face :\n")
  print(temp)
  print(temp.shape)
  # cv2.imshow('image',t[target])
  # cv2.waitKey(0)
  # closest_var = os.path.join(folderr, t[target])
  # print(closest_var)
  # img2 = PIL.Image.open(closest_var)
  # img2 = img2.resize((256, 256))
  # img2 = ImageTk.PhotoImage(img2)
  # my_label2 = Label(WINDOW, image = img2)
  # my_label2.image = img2
  # my_label2.place(x = 300, y = 145)
  # cv2.destroyAllWindows()

button_folder = ctk.CTkButton(window, text = "Choose Folder", command = open_folder, cursor="hand2")
button_folder.place(x = 36, y = 200)

button_image = ctk.CTkButton(window, text = "Choose Image", command = open_image, cursor="hand2")
button_image.place(x = 36, y = 275)

button_scan = ctk.CTkButton(window, text = "SCAN", command = proses, cursor="hand2")
button_scan.place(x = 36, y = 125)

window.mainloop()



