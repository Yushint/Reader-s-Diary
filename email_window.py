from main_window import Window
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as mb

class EmailWindow(Window):
    def __init__(self):
        super().__init__()
        
        self.address = ""
        self.root.geometry('410x350+{}+{}'.format(self.WIDTH, self.HEIGHT))
        self.root.resizable(False, False)
        self.root.config(bg="#f5f5dc")        
        self.image = "img/email.png"
        self.root.title("Email export.")   
        
        self.image_label = Label(self.root, bg="#f5f5dc", width=150, height=110)
        self.image_label.place(x=125, y=5)
        
        self.photo_img = Image.open(self.image)
        self.tk_photo_img = ImageTk.PhotoImage(self.photo_img)
        self.image_label.config(image=self.tk_photo_img)
        
        self.export_label = Label(self.root, bg="#f5f5dc",
                                text="DATA EXPORT",
                                font = ("Courier New", 20))
        self.export_label.place(x=115, y=120)
        
        self.address_label = Label(self.root, bg="#f5f5dc",
                                text="Your Address:",
                                font = ("Courier New", 15))
        self.address_label.place(x=125, y=200)  
        
        self.entry = Entry(self.root, width=25)
        self.entry.place(x=125, y=230)
        
        self.export_button = Button(self.root, bg="#f5f5dc", text="Export",
                                    command=self.get_address, width=5, height=2,
                                    activebackground="#f5f5dc")
        self.export_button.place(x=180, y=270)
        
    def get_address(self):
        address = self.entry.get()
        if len(address) == 0:
            mb.showerror("Внимание!", "Заполните поле e-mail адреса.")
        else:
            self.address = address
            self.root.destroy()
    
    def return_address(self):
        return self.address
    
        
a = EmailWindow()
a.run()
print(a.return_address())
        