from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as mb
from main_window import Window


class WriteWindow(Window):
    def __init__(self):
        super().__init__()
        self.root.geometry('410x350+{}+{}'.format(self.WIDTH, self.HEIGHT))
        self.root.resizable(False, False)
        self.root.config(bg="#f5f5dc")        
        self.image = "img/test2.png"
        self.root.title("Write new book.")
        
        self.data = ""
        
        self.photo_label = Label(self.root, bg="#f5f5dc", width=145, height=100)
        self.photo_label.place(x=5, y=5)
        
        self.photo_img = Image.open(self.image)
        self.tk_photo_img = ImageTk.PhotoImage(self.photo_img)
        self.photo_label.config(image=self.tk_photo_img)
        
        self.author_lab = Label(self.root, bg="#f5f5dc", text="Author:")
        self.author_lab.place(x=170, y=10)
        
        self.name_lab = Label(self.root, bg="#f5f5dc", text="Book's name:")
        self.name_lab.place(x=170, y=40)        
        
        self.year_lab = Label(self.root, bg="#f5f5dc", text="Year of publishing:")
        self.year_lab.place(x=170, y=70)
        
        self.rating_lab = Label(self.root, bg="#f5f5dc", text="Book's rating:")
        self.rating_lab.place(x=170, y=100)
        
        self.feedback_lab = Label(self.root, bg="#f5f5dc", text="FEEDBACK")
        self.feedback_lab.place(x=210, y=130)
        
        self.author_entry = Entry(self.root, width=20)
        self.author_entry.place(x=220, y=11)
        
        self.name_entry = Entry(self.root, width=20)
        self.name_entry.place(x=250, y=41)
        
        self.year_entry = Entry(self.root, width=20)
        self.year_entry.place(x=280, y=71)
        
        self.r_var = IntVar()
        self.r_var.set(0)
        
        self.r1 = Radiobutton(self.root, text="1", variable=self.r_var, value=1, bg="#f5f5dc")
        self.r1.place(x=250, y=100)
        
        self.r2 = Radiobutton(self.root, text="2", variable=self.r_var, value=2, bg="#f5f5dc")
        self.r2.place(x=280, y=100)        
        
        self.r3 = Radiobutton(self.root, text="3", variable=self.r_var, value=3, bg="#f5f5dc")
        self.r3.place(x=310, y=100)  
        
        self.r4 = Radiobutton(self.root, text="4", variable=self.r_var, value=4, bg="#f5f5dc")
        self.r4.place(x=340, y=100)   
        
        self.r5 = Radiobutton(self.root, text="5", variable=self.r_var, value=5, bg="#f5f5dc")
        self.r5.place(x=370, y=100)  
        
        self.text = Text(self.root, width=35, height=10)
        self.text.place(x=105, y=150)
        
        self.save_btn = Button(self.root, text="Save", width=5, height=2, activebackground="#f5f5dc", bg="#f5f5dc", command=self.save)
        self.save_btn.place(x=30, y=200)
        
    def save(self):
        author = self.author_entry.get()
        name = self.name_entry.get()
        year = self.year_entry.get()
        rating = self.r_var.get()
        feedback = self.text.get(1.0, END)
        if (len(author) == 0) or (len(name) == 0) or (len(year) == 0) or\
           (rating == 0) or (len(feedback) == 1):
            mb.showerror("Внимание!", "Вы должны заполнить все поля.")
        else:
            data = author + '+' + name + '+' + year + '+' + str(rating) + '+' + feedback
            self.data = data
            self.root.destroy()
            self.return_data()
    
    def return_data(self):
        return self.data
            
        
w = WriteWindow()
w.set_icon()
w.run()
print(w.return_data())
            
