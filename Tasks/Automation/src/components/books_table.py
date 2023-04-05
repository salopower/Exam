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
        self.table_items_publisher = ss(by.xpath("//div[@class='rt-td'][4]"))

    # Готові та працюючі методи
    def filter_book_by_filter_name(self, filter_name: str):
        self.filter_field_name = s(by.xpath(f"// div[contains(text(), '{filter_name.title()}')]")).should(
            be.clickable).click()

    @staticmethod
    def get_sort_order():
        sort_element = s(by.xpath('//div[@class="rt-th rt-resizable-header -sort-asc -cursor-pointer"]'))
        sort_class = sort_element.get(query.attribute('class'))
        if '-sort-desc' in sort_class:
            return 'desc'
        elif '-sort-asc' in sort_class:
            return 'asc'
        else:
            return None

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

    # Методи які потрібно переробити
    def search_books(self, prompt: str) -> dict[str, dict[str, list[str]]]:
        self.enter_request(prompt)
        books = {}
        for row in self.table_rows.should(have.size_greater_than_or_equal(1)):
            book_title = row.element(by.xpath("//span[@class='mr-2']//a")).get(query.text)
            author_elements = row.ss(by.xpath("//div[@class='rt-td'][3]")).should(have.size_greater_than_or_equal(1))
            publisher_elements = row.ss(by.xpath("//div[@class='rt-td'][4]")).should(have.size_greater_than_or_equal(1))
            authors = list(set([elem.get(query.text) for elem in author_elements if elem.get(query.text)]))
            publishers = list(set([elem.get(query.text) for elem in publisher_elements if elem.get(query.text)]))
            if book_title and authors and publishers:
                books[book_title] = {'author': authors, 'publisher': publishers}
        return books
