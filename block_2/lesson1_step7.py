from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure").get_attribute("valuex")
    y = calc(x_element)

    input_x = browser.find_element_by_id("answer")
    input_x.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    time.sleep(3)
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()