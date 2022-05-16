# -*- coding: utf-8 -*-
import sqlite3 as sql
import os


class DatabaseHandler:
    def __init__(self, name:str):
        """ Конструктор, создаёт базу данных с именем name и таблицу books. Также
            создаёт html-файл справки, если таблица создаётся впервые."""
        self.name = name
        self.curr_id = None
        if self.check_files("token.bin") == True:
            self.reconnect()
        else:
            
            os.remove(self.name) if self.check_files(self.name) == True else None
            f = open("token.bin", 'w+')
            f.close()
            self.id_counter = 0
            f = open("id.txt", "w+")
            f.write(str(self.id_counter))
            f.close()
            self.conn = sql.connect(self.name)
            self.cur = self.conn.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY,
            author TEXT, name TEXT, year INT, rating INT, feedback TEXT); """)
            self.conn.commit()
        
    def check_files(self, name:str) -> bool:
        """ Проверяет, существует ли файл с именем name. Если да, то
            выводит True. Иначе - False."""
        self.directory = os.getcwd()
        self.local_files = os.listdir(self.directory)
        return True if name in self.local_files else False
    
    def add_book(self, book_list:list):
        """ Принимает список кортежей, содержащих информацию о книге в формате 
            базы данных. Добавляет эти данные в таблицу books.
        """
        try:
            self.cur.executemany(""" INSERT INTO books VALUES (?,?,?,?,?,?)""", book_list)
            self.conn.commit()
            self.id_counter += 1
            f = open("id.txt", "w")
            f.write(str(self.id_counter))
            f.close()            
        except Exception:
            pass
    
    def get_book(self, id_:int) -> tuple:
        """ Возвращает кортеж данных о книге с текущим self.curr_id.
        """
        sql = f"SELECT * FROM books WHERE book_id = '{id_}'"
        self.cur.execute(sql)
        self.conn.commit()
        self.curr_id = None
        return self.cur.fetchone()
    
    def get_all_books(self) -> list:
        """ Возвращает список кортежей, содержащих информацию о всех книгах в
            таблице данных books.
        """
        sql = """SELECT * from books"""
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.fetchall()
    
    def delete_book(self, id_:int):
        """ Удаляет из таблицы книгу с текущим параметром self.curr_id.
        """
        sql = f"DELETE FROM books WHERE book_id = '{id_}'"
        self.cur.execute(sql)
        self.conn.commit()      
    
    def check_book(self, id_:int) -> bool:
        """ Проверяет, содержится ли книга с заданным id_ в таблице. Если да,
            то выводит True. Иначе - False.
        """
        sql = f"SELECT book_id FROM books WHERE book_id = '{id_}'"
        self.cur.execute(sql)
        self.conn.commit()
        return True if len(self.cur.fetchall()) > 0 else False
    
    def reconnect(self):
        """ Переподключается к базе данных.
        """
        self.conn = sql.connect(self.name)
        self.cur = self.conn.cursor()
        f = open("id.txt", "r")
        s = int(f.read())
        self.id_counter = s
    
    def get_id(self, info_list:list):
        """ Принимает на вход список, содержащий автора и название книги. Проверяет, 
            существует ли книга с такими параметрами в таблице books. Если да, 
            то обновляет self.curr_id на id этой книги. Иначе возвращает None.
            Этот метод всегда вызывается первым при выборе книг из виджета Listbox.
        """
        sql = f"""SELECT book_id FROM books WHERE author = ? and name = ?"""
        self.cur.execute(sql, info_list)
        self.conn.commit()
        id_list = self.cur.fetchall()
        if len(id_list) > 0:
            self.curr_id = id_list[0][0]
            return self.curr_id
        else:
            self.curr = None
    
    def close(self):
        self.cur.close()
        self.conn.close()
         
