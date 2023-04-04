import json

import requests
from selene.api import *


class BookStorePage(object):
    def __init__(self):
        self.main_header = s(by.xpath("//div[@class='main-header']"))
        self.login_button = s("#login")
        self.search_box = s("#searchBox")

    def check_main_header(self, text):
        return self.main_header.should(have.text(f'{text}'))

    def click_login_button(self):
        self.login_button.click()

    def enter_request(self, prompt):
        self.search_box.set(prompt)
        return self

    def book_list_by_publisher_api(self, publisher: str):
        url = 'https://demoqa.com/BookStore/v1/Books'
        response = requests.get(url)
        result = json.loads(response.text).get('books')
        book_info = {}
        book_list = []
        for i in result:
            for k, v in i.items():
                if k == "title" or k == 'author' or k == 'publisher':
                    book_info[k] = v
            if book_info['publisher'] == publisher:
                book_list.append(book_info)
        return book_list
