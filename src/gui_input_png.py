from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

window = Tk()
window.configure(background='white')
window.minsize(width=500, height=300)


def open():
  global my_image
  window.filename = filedialog.askopenfilename(initialdir = "D:", title= "Select a Photo", filetypes = (("png files","*.png"),("all files","*.*")))
  my_label = Label(window, text=window.filename).pack()
  my_image = ImageTk.PhotoImage(Image.open(window.filename))
  my_image_label = Label(image=my_image).pack()



my_button = Button(window, text="Open File", command=open).pack()
window.mainloop() 