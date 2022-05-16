import unittest
from email_processor import EmailHandler

class EmailTest(unittest.TestCase):
    def setUp(self):
        self.email_handler = EmailHandler("reader-s-diary@yandex.ru", "Title", "test")
    
    def test_message_defining(self):
        """ Тестируем метод, отправляющий электронное сообщение. Исключение выбрасывается при отсутствии подключения к интернету.
        """
        with self.subTest(case=None):
            self.assertRaises(Exception, self.email_handler.define_message)
            
if __name__ == "__main__":
    unittest.main()