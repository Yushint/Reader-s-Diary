import unittest
import os
from database import DatabaseHandler


class Test_Database(unittest.TestCase):
    def setUp(self):
        """ Объявляем объект типа DatabaseHandler, который будем тестировать.
        """
        self.database = DatabaseHandler("books.db")
        
    def test_check_files(self):
        """ Тестируем метод проверки файлов.
        """
        cases = (file for file in os.listdir(os.getcwd()))
        for test_case in cases:
            with self.subTest(case=test_case):
                self.assertTrue(self.database.check_files(test_case))
                
    def test_get_id(self):
        """ Тестируем метод получения id книги.
        """
        cases = (["a", "a"], ["A.S.Pushkin", "None"])
        id_counter = 1
        for test_case in cases:
            with self.subTest(case=test_case):
                self.assertEqual(self.database.get_id(test_case), id_counter)
            id_counter += 1
            
    def test_check_book(self):
        """ Тестируем метод проверки наличия книги.
        """
        for _id in range(1, 3):
            with self.subTest(case=_id):
                self.assertTrue(self.database.check_book(_id))
                
    def test_get_book(self):
        """ Тестируем метод возврата сигнатуры книги.
        """
        for _id in range(1, 3):
            with self.subTest(case=_id):
                self.assertIsInstance(self.database.get_book(_id), tuple)
                
    def test_get_all_books(self):
        """ Тестируем метод возврата всех сигнатур.
        """
        with self.subTest(case=None):
            self.assertIsInstance(self.database.get_all_books(), list)
            
    def test_add_book(self):
        """ Тестируем метод добавления книги на предмет вызова исключения. Если текущий test-case провален, то всё в порядке.
        """
        with self.subTest(case=None):
            self.assertRaises(Exception, self.database.add_book, ["author", "book", 1800])
            

if __name__ == "__main__":
    unittest.main()
