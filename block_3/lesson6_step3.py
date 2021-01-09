import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('digit', ["236895", "236896", "236897", "236898",
                                   "236899", "236903", "236904", "236905"])
def test_world_time(browser, digit):
    link = f"https://stepik.org/lesson/{digit}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    res = str(math.log(int(time.time())))
    browser.find_element_by_css_selector('div.quiz-component > textarea').send_keys(res)
    browser.find_element_by_class_name('submit-submission').click()
    answer = browser.find_element_by_class_name('smart-hints__hint').text
    assert answer == 'Correct!', f'Answer = "{answer}". It is not correct!!!'


