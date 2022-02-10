from tkinter import *
from tkinter import messagebox as mb
from main_window import Window
from PIL import Image, ImageTk
import os


class DiaryWindow(Window):
    def __init__(self):
        super().__init__()
    
    def set_diary_menu(self):
        self.mainmenu = Menu(self.root)
        self.root.configure(menu=self.mainmenu)
        
        self.filemenu = Menu(self.mainmenu, tearoff=0)
        self.filemenu.add_command(label="Экспорт записей", command=self.export)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Выход", command=self.exit)
        self.mainmenu.add_cascade(label="Дневник", menu=self.filemenu)
        
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
app.set_diary_menu()
app.run()
