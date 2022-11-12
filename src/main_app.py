import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(background='white')

window.title("My First GUI Program")
window.minsize(width=500, height=300)

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=10, fill="x", expand=True)

nama_depan_label = ttk.Label(input_frame, text="Nama Depan")
nama_depan_label.pack(padx=10, fill="x", expand=True)

Nama = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=Nama)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
window.mainloop()