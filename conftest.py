import pytest
from selene.support.shared import config, browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='package', name='demoqa', autouse=True)
def set_browser_for_demoqa():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-setuid-sandbox")
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options)
    config.base_url = 'https://demoqa.com/'
    config.driver = driver
    yield driver
    browser.quit()
