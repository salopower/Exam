from selene.api import *
from Tasks.Automation.src.pages.BookStorePage import BookStorePage
from Tasks.Automation.src.components.books_table import BooksTable
from Tasks.Automation.src.domain.book import Book


class TestBookStore:

    def test_check_main_header(self, bookstore):
        assert BookStorePage().check_main_header('Book Store')

    def test_search_item(self, bookstore):
        git_book = Book(title='Git Pocket Guide')
        BookStorePage().enter_request(git_book.title)

    def test_get_books_from_table(self, bookstore):
        book = Book(publisher="O'Reilly Media")
        books_table = BooksTable()
        books = books_table.search_books_in_table(book.publisher)
        for book in books:
            print(f'\n{book}')

        assert isinstance(books, list)

    def test_filter_table(self, bookstore):
        BooksTable().filter_book_by_filter_name('Publisher')

    def test_get_publisher(self, bookstore):
        books_table = BooksTable()
        publishers = books_table.get_unique_values('Git Pocket Guide', 'author')
        print(f'\n{publishers}')

    def test_get_author_and_publisher(self, bookstore):
        books_table = BooksTable()
        unique_values = books_table.get_author_and_publisher('No Starch Press')
        print(unique_values)

    def test_search_books_by_prompt(self, bookstore):
        books_table = BooksTable()
        books = books_table.search_books("No Starch Press")
        for book_title, book_info in books.items():
            print(f'\n{book_title}')
            for key, value in book_info.items():
                print(f'{key}: {value}')
        assert len(books) > 0
