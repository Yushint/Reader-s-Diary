# -*- coding: utf-8 -*-
import sqlite3 as sql
import os


class DatabaseHandler:
    def __init__(self, name):
        if self.check_files(name) == True:
            os.remove(name)
        self.conn = sql.connect(name)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY,
        name TEXT, author TEXT, year INT, rating INT, feedback TEXT); """)
        self.conn.commit()
        
    def check_files(self, name):
        self.directory = os.getcwd()
        self.local_files = os.listdir(self.directory)
        return True if name in self.local_files else False
    
    def get_book(self, _id):
        pass
    
    def get_all_books(self):
        pass    
    
    def insert_book(self, _id):
        pass
    
    def delete_book(self, _id):
        pass
    
    def delete_all_books(self):
        pass
    
    def check_book(self, id_):
        pass
    
