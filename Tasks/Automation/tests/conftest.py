import pytest


@pytest.fixture(scope='class')
def bookstore(request):
    driver = request.getfixturevalue('get_chrome')
    driver.get('https://demoqa.com/books')
    yield driver
