# is made by Abramov Ilya (@evoriath), GNU GPL
from tkinter import *
from PIL import Image, ImageTk
import os


root = Tk()

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
WIDTH = WIDTH // 2
HEIGHT = HEIGHT // 2
WIDTH = WIDTH - 200
HEIGHT = HEIGHT - 200

image = Image.open("img/background.jpg")
tk_image = ImageTk.PhotoImage(image)
label = Label(width=650, height=200, image=tk_image)
label.pack()


root.geometry('650x350+{}+{}'.format(WIDTH, HEIGHT))
root.mainloop()
