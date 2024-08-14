#!/opt/homebrew/bin/python3
import tkinter as tk
from tkinter import ttk

import os


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

root = tk.Tk()
root.title("corne keyboard viewer")
root.geometry("1920x1080")
# Load image from disk.

image = tk.PhotoImage(file=f"{dname}/output.png")
# Display it within a label.
label = ttk.Label(image=image)
label.pack()
root.bind("<space>", lambda e: root.destroy())
root.bind("<Return>", lambda e: root.destroy())
root.mainloop()
