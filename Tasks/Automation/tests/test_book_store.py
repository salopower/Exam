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
        book = Book(publisher='No Starch Press')
        books_table = BooksTable()
        books = books_table.search_books_in_table(book.publisher)
        assert isinstance(books, dict)

    def test_filter_table(self, bookstore):
        BooksTable().filter_book_by_filter_name('publisher')
