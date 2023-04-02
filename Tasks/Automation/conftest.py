import pytest


@pytest.fixture(scope='class', autouse=True)
def get_chrome(request):
    driver = request.getfixturevalue('demoqa')
    yield driver
    driver.quit()
