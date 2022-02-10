# is made by Abramov Ilya (@evoriath), GNU GPL
from tkinter import *
from PIL import Image, ImageTk
import os


class MainWindow:
    def __init__(self):
            self.root = Tk()
            self.WIDTH = self.root.winfo_screenwidth()
            self.HEIGHT = self.root.winfo_screenheight()
            self.WIDTH = self.WIDTH // 2
            self.HEIGHT = self.HEIGHT // 2
            self.WIDTH = self.WIDTH - 200
            self.HEIGHT = self.HEIGHT - 200
            WIDTH, HEIGHT = self.WIDTH, self.HEIGHT
            self.root.geometry('650x350+{}+{}'.format(self.WIDTH, self.HEIGHT))
            self.root.title("Reader's Diary")
            self.root.resizable(False, False)
            self.root.config(bg="#f5f5dc")

    def set_frames(self):
        self.top_frame = Frame(self.root)
        self.bottom_frame = Frame(self.root)
        self.top_frame.pack(side=TOP)
        self.bottom_frame.pack(side=TOP)

    def set_background_image(self):
        self.background_image = Image.open("img/background.jpg")
        self.tk_background_image = ImageTk.PhotoImage(self.background_image)
        self.top_label.config(image=self.tk_background_image)

    def set_labels(self):
        self.top_label = Label(self.top_frame, width=650, height=190, bg="white")
        #self.bottom_canvas = Canvas(self.bottom_frame, bg="#f5f5dc", width=650, height=200)
        self.top_label.pack(side=TOP)
        #self.bottom_canvas.pack(side=BOTTOM)

    def set_enter_button(self):
        self.button = Button(self.bottom_frame, text="Reader's Diary", font=("Courier New", 20), command=self.enter, bg="#f5f5dc", activebackground="#f5f5dc")
        self.button.pack(side=TOP)

    def enter(self):
        self.root.destroy()
        os.system("python diary.py")

    def set_icon(self):
        self.icon_img = Image.open("img/icon.jpg")
        self.icon_img.save("Icon.ico")
        self.root.iconbitmap("Icon.ico")

    def run(self):
        self.root.mainloop()


window = MainWindow()
window.set_frames()
window.set_labels()
window.set_enter_button()
window.set_background_image()
window.set_icon()
window.run()
