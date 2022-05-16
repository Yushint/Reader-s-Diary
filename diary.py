# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook
from main_window import Window
from PIL import Image, ImageTk
from datetime import datetime as dt
from database import DatabaseHandler
from subprocess import run
from email_processor import EmailHandler


class DiaryWindow(Window):
    def __init__(self, db):
        super().__init__()
        
        self.db = db
        
        self.root.geometry("650x500")
        self.main_tab = Notebook(self.root)
        self.first_tab = Frame(self.main_tab, bg="#f5f5dc")
        self.second_tab = Frame(self.main_tab, bg="#f5f5dc")
        self.main_tab.add(self.first_tab, text="Diary")
        self.main_tab.add(self.second_tab, text="Search")
        self.main_tab.pack(expand=1, fill="both")
        
        self.center_label = Label(self.first_tab, text="You are welcome.", font=("Courier New", 20), bg="#f5f5dc")
        self.center_label.place(x=190, y=5)
        
        self.date_label = Label(self.first_tab, text=dt.today().strftime(("%d %B %Y,\n %A.")), font=("Courier New", 9, "bold"), bg="#f5f5dc", fg="#b15124")
        self.date_label.place(x=500, y=3)
        
        self.my_books_label = Label(self.first_tab, text="My books", font=("Courier New", 15, "bold"), bg="#f5f5dc", fg="#b15124")
        self.my_books_label.place(x=75, y=75)
        
        self.book_box = Listbox(self.first_tab, width=35, height=20, bg="#f5f5c3", selectmode=EXTENDED)
        self.book_box.place(x=5, y=100)
        
        self.scrollbar = Scrollbar(self.first_tab, command=self.book_box.yview)
        self.scrollbar.place(x=212, y=100, height=325)
        self.book_box.config(yscrollcommand=self.scrollbar.set)
        
        self.horizontal_scrollbar = Scrollbar(self.first_tab, orient="horizontal", command=self.book_box.xview)
        self.horizontal_scrollbar.place(x=5, y=425, width=220)
        self.book_box.config(xscrollcommand=self.horizontal_scrollbar.set)
        
        self.erase_button = Button(self.first_tab, bg="#f5f5dc", text="Erase",
                                   command=self.erase_book_box, width=5, height=2, activebackground="#f5f5dc")
        self.erase_button.place(x=235, y=220)
        
        self.check_button = Button(self.first_tab, bg="#f5f5dc", text="Check",
                                   command=self.look, width=5, height=2, activebackground="#f5f5dc")
        self.check_button.place(x=235, y=280)
        
    def set_background_images(self):
        self.bg_tree_label = Label(self.first_tab, bg="#f5f5dc", width=400, height=520)
        self.bg_tree_label.place(x=285, y=35)       
        self.bg_tree_image = Image.open("img/tree_book.png")
        self.tk_bg_tree_image = ImageTk.PhotoImage(self.bg_tree_image)
        self.bg_tree_label.config(image=self.tk_bg_tree_image)
        
        self.bg_write_button = Button(self.first_tab, bg="#f5f5dc", width=40, height=40, activebackground="#f5f5dc")
        self.bg_write_button.place(x=235, y=158)
        self.bg_write_image = Image.open("img/sample1.jpg")
        self.tk_bg_write_image = ImageTk.PhotoImage(self.bg_write_image)
        self.bg_write_button.config(image=self.tk_bg_write_image, command=self.update_book_box)
    
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
    
    def fill_book_box(self):
        self.book_box.delete(0, END)
        books = self.db.get_all_books()
        for book in books:
            author = book[1]
            name = book[2]
            initials = author + ' ' + "<<" + name + ">>"
            self.book_box.insert(END, initials)
        
    
    def erase_book_box(self):
        question = mb.askyesno(title="Удаление", message="Вы точно хотите удалить выбранные записи?")
        if question:
            selected = list(self.book_box.curselection())
            selected.reverse()
            for note in selected:
                temp = self.book_box.get(note).split("<<")           
                author = temp[0].strip()
                temp[1] = temp[1].replace(">>",'')
                name = temp[1]
                info_list = [author, name]
                id_ = self.db.get_id(info_list)
                self.db.delete_book(id_)
                self.book_box.delete(note)
        
    
    def update_book_box(self):
        self.db.reconnect()
        process = run(["python", "write_window.py"], capture_output=True)
        data = process.stdout.decode("utf-8")
        if len(data) == 2:
            pass
        else:
            data = data.split("+")
            try:
                author, name, year, rating, feedback = data[0], data[1], int(data[2]), int(data[3]), data[4]
                id_ = self.db.get_id([author, name])
                if id_ == None:
                    question = mb.askyesno("Сохранение", "Сохранить книгу?")
                    if question:
                        c_id = self.db.id_counter + 1
                        data = [(c_id, author, name, year, rating, feedback)]
                        self.db.add_book(data)
                        self.fill_book_box()
                else:
                    mb.showerror("Внимание!", "Данная книга уже была записана.")
            except ValueError:
                mb.showerror("Внимание!", "Вы ввели неправильные значения в поле года выпуска. Попробуйте ещё раз.")
        
    def look(self):
        pass
    
    def export(self):
        self.book_box.select_set(0, END)
        selection = self.book_box.curselection()
        if len(selection) == 0:
            mb.showerror("Внимание!", "Записей для экспорта не существует.")
            return
        process = run(["python", "email_window.py"], capture_output=True)
        address = process.stdout.decode("utf-8")
        title = "Reader's Diary Application. Data Export."
        text = "Thank you for using the application.\n All your data is here.\n\nBooks:\n"
        books = self.db.get_all_books()
        for book in books:
            author = book[1]
            book_name = book[2]
            data_of_publishing = book[3]
            book_rating = book[4]
            expression = book[5]
            expression = expression.replace("\r","")
            expression = expression.replace("\n","")
            current_text = f"Author: {author}, Title: {book_name},Year of publishing: {data_of_publishing}, Rating: {book_rating}, Expression: {expression}.\n"
            text = text + current_text
        mail = EmailHandler(address, title, text)
        mail.define_message()
        try:
            mail.send_message()
        except Exception:
            mb.showerror("Внимание!", "Что-то пошло не так...")
            return
        mb.showinfo("Внимание!", "Письмо-экспорт успешно отправлено.")
        
    def exit(self):
        self.root.destroy()
    
    def help(self):
        mb.showinfo("Справка", """1. Для записи отзыва нажмите на кнопку с иконкой книжки.\n\n2. Для удаления отзыва выберите его в списке записей и нажмите на кнопку 'Erase'.\n\n3. Для экспорта записей выберите кнопку Меню --> Программа --> Экспорт записей. Учтите, что для экспорта вам необходимы наличие отзывов и интернет-соединение.\n\n 4. Для просмотра отзыва выберите его в списке записей и нажмите на кнопку 'Check'.\n\n5. Для выхода из приложения нажмите на кнопку Меню --> Программа --> Выход. Либо нажмите на красный крестик.\n\n В случае, если вы столкнулись со сложной проблемой, отправьте письмо на следующий почтовый адрес: student.Abramovilja@yandex.ru""")
    def about(self):
        mb.showinfo("О программе", "Автор программы - Абрамов Илья, студент ФГиИБ.\n\nПрограмма читательского дневника была создана в рамках индивидуального задания для курса ЯП в МИИГАиК.\n\nПользоваться дневником по назначению не воспрещается.")
    
db = DatabaseHandler("books.db")
app = DiaryWindow(db)
app.set_icon()
app.set_background_images()
app.set_diary_menu()
app.fill_book_box()
app.run()
