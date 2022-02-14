# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from main_window import Window
from PIL import Image, ImageTk
from datetime import datetime as dt


class DiaryWindow(Window):
    def __init__(self):
        super().__init__()
        
        self.center_label = Label(self.root, text="You are welcome.", font=("Courier New", 20), bg="#f5f5dc")
        self.center_label.place(x=190, y=5)
        
        self.date_label = Label(self.root, text=dt.today().strftime(("%d %B %Y,\n %A.")), font=("Courier New", 9, "bold"), bg="#f5f5dc", fg="#b15124")
        self.date_label.place(x=500, y=3)
        
        self.bg_scroll_label = Label(self.root, bg="#f5f5dc", width=185, height=120)
        self.bg_scroll_label.place(x=480, y=200)
        
    def set_background_images(self):
        self.bg_scroll_image = Image.open("img/scroll.png")
        self.tk_bg_scroll_image = ImageTk.PhotoImage(self.bg_scroll_image)
        self.bg_scroll_label.config(image=self.tk_bg_scroll_image)
    
    def set_diary_menu(self):
        self.mainmenu = Menu(self.root)
        self.root.configure(menu=self.mainmenu)
        
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Экспорт записей", command=self.export)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Выход", command=self.exit)
        self.mainmenu.add_cascade(label="Программа", menu=self.filemenu)
        
        self.helpmenu = Menu(self.mainmenu, tearoff=0)
        self.helpmenu.add_command(label="Помощь", command=self.help)
        self.helpmenu.add_command(label="О программе", command=self.about)
        self.mainmenu.add_cascade(label="Справка", menu=self.helpmenu)
    
    def export(self):
        pass
    
    def exit(self):
        self.root.destroy()
    
    def help(self):
        pass
    
    def about(self):
        mb.showinfo("О программе", "Автор программы - Абрамов Илья, студент ФГиИБ.\nПрограмма читательского дневника была создана в рамках индивидуального задания для курса ЯП в МИИГАиК.\nПользоваться дневником по назначению не воспрещается.")
    
    
app = DiaryWindow()
app.set_icon()
app.set_background_images()
app.set_diary_menu()
app.run()
