from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
  return str(int(x) + int(y))


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    res = calc(x, y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(res)
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()