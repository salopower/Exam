from selene.api import *
from typing import Dict
from selenium.webdriver.remote.webelement import WebElement
from Tasks.Automation.src.pages.BookStorePage import BookStorePage


class BooksTable(BookStorePage):
    def __init__(self):
        super().__init__()
        self.filter_field_name = None
        self.table = s(by.xpath("//div[@class='ReactTable -striped -highlight']"))
        self.table_items = ss(by.xpath("//div[@class='rt-tr-group']"))
        self.table_items_title = ss(by.xpath("//span[@class='mr-2']//a"))
        self.table_items_author = ss(by.xpath("//div[@class='rt-tr-group']/descendant::div[@class='rt-td'][3]"))
        self.table_items_publisher = ss(by.xpath("//div[@class='rt-tr-group']/descendant::div[@class='rt-td'][3]"))

    def search_books_in_table(self, prompt: str):
        self.enter_request(prompt)
        book_titles = []
        for book in self.table_items_title:
            book_titles.append(book.text)
        if not book_titles:
            raise Exception("No books found")
        return book_titles

    def filter_book_by_filter_name(self, filter_name: str):
        self.filter_field_name = s(by.xpath(f"// div[contains(text(), '{filter_name}')]")).click()
