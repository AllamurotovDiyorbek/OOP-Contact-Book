from rich.console import Console
import json
class Contact_book:
      def __init__(self):
            self.console=Console()
      def print_menyu(self):
            self.console.print('[bold italic green]',
            ' 1. add_contact(contact) – yangi kontakt qo‘shish \n',
            '2. remove_contact(name) – ism bo‘yicha kontaktni o‘chirish \n',
            '3. update_contact(name, new_contact) – kontakt ma’lumotlarini yangilash \n',
            '4. list_contacts() – barcha kontaktlarni chiqarish \n',
            '5. search_contact(name) – ism bo‘yicha qidirish \n',
            '6. save_to_file() – kontaktlarni JSON faylga yozish \n',
            '7. load_from_file() – fayldan kontaktlarni o‘qib olish'
            )
      def add_contact(self):
            name=input("Name: ")
            phone=input("Phone: ")
            email=input("Email: ")
      def remove_contact(self):
            pass
      def update_contact(self):
            pass
      def list_contacts(self):
            pass
      def search_contact(self):
            pass
      def save_to_file(self):
            pass
      def load_from_file(self):
            pass
      def run(self):
            pass