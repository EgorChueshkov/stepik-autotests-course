from selenium import webdriver
import math
import time
import pyperclip


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('button').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    res = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(res)

    browser.find_element_by_css_selector('button.btn').click()

    


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()