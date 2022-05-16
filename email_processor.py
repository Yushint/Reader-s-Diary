# -*- coding= utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from tkinter import messagebox as mb

class EmailHandler:
    """ Класс отвечает за отправку сообщений с почтового сервера
        приложения.
    """
    def __init__(self, addr_to, title, text):
        """ Конструктор. Определение внутренних полей."""
        self.addr_from = "reader-s-diary@yandex.ru"
        self.password = "readersdiarypassword"
        self.addr_to = addr_to
        self.title = title
        self.text = text
        
    def define_message(self):
        """ Заполнение оболочки сообщения с помощью функциональности
            библиотеки email.mime. 
        """
        self.message = MIMEMultipart()
        self.message['From'] = self.addr_from
        self.message['Subject'] = self.title
        self.message.attach(MIMEText(self.text, 'plain'))
        try:
            self.server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        except Exception:
            mb.showinfo("Внимание!", "Письмо не отправлено. Проверьте подключение к интернету.")
            return None
        self.server.set_debuglevel(0)
        self.server.login(self.addr_from, self.password)

    def send_message(self):
        """ Отправление сообщения по протоколу smtp."""
        self.message['To'] = self.addr_to
        self.server.send_message(self.message)
        self.server.quit()
