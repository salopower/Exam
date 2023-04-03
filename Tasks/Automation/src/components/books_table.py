from selene.api import *
from typing import Dict, List, Set
from Tasks.Automation.src.pages.BookStorePage import BookStorePage


class BooksTable(BookStorePage):
    def __init__(self):
        super().__init__()
        self.filter_field_name = None
        self.table = s(by.xpath("//div[@class='ReactTable -striped -highlight']"))
        self.table_items = ss(by.xpath("//div[@class='rt-tr-group']"))
        self.table_rows = ss(by.xpath("//div[@role='rowgroup']"))
        self.table_items_title = ss(by.xpath("//span[@class='mr-2']//a"))
        self.table_items_author = ss(by.xpath("//div[@class='rt-td'][3]"))
        #  //div[@class='rt-td'][3]/text()
        self.table_items_publisher = ss(by.xpath("//div[@class='rt-td'][4]"))
        #  //div[@class='rt-td'][4]/text()

    def get_unique_values(self, prompt: str, attribute: str) -> Set[str]:
        self.enter_request(prompt)
        if attribute == 'author':
            elements = self.table_items_author
        elif attribute == 'publisher':
            elements = self.table_items_publisher
        else:
            raise ValueError(f'Invalid attribute value: {attribute}')
        values = (elem.get(query.text) for elem in elements if
                  elem.get(query.text) != '' and elem.get(query.text) != ' ')
        unique_values = set(set(values))
        return unique_values

    def get_author_and_publisher(self, prompt: str) -> Dict[str, Set[str]]:
        author_values = self.get_unique_values(prompt, 'author')
        publisher_values = self.get_unique_values(prompt, 'publisher')
        return {'author': author_values, 'publisher': publisher_values}

    def search_books_in_table(self, prompt: str) -> List[str]:
        self.enter_request(prompt)
        book_titles = []
        for book in self.table_items_title:
            book_titles.append(book.get(query.text))
        if not book_titles:
            raise Exception("No books found")
        return book_titles

    def search_books(self, prompt: str) -> dict[str, dict[str, list[str]]]:
        self.enter_request(prompt)
        books = {}
        for book in self.table_items_title:
            book_title = book.get(query.text)
            authors = (elem.get(query.text) for elem in self.table_items_author if
                       elem.get(query.text) != '' and elem.get(query.text) != ' ')
            author = list(set(authors))
            publishers = (elem.get(query.text) for elem in self.table_items_publisher if
                          elem.get(query.text) != '' and elem.get(query.text) != ' ')
            publisher = list(set(publishers))
            if book_title and author and publisher:
                books[book_title] = {'author': author, 'publisher': publisher}
        return books

    def filter_book_by_filter_name(self, filter_name: str):
        self.filter_field_name = s(by.xpath(f"// div[contains(text(), '{filter_name}')]")).click()
