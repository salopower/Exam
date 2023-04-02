from selene.api import *


class BookStorePage(object):
    def __init__(self):
        self.main_header = s(by.xpath("//div[@class='main-header']"))
        self.login_button = s("#login")
        self.search_box = s("#searchBox")

    def check_main_header(self, text):
        return self.main_header.should(have.text(f'{text}'))

    def enter_request(self, prompt):
        self.search_box.set(prompt)
        return self

    def click_login_button(self):
        self.login.click()
