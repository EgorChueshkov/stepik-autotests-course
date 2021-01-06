from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input_x = browser.find_element_by_id("answer")
    input_x.send_keys(y)
    time.sleep(3)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    time.sleep(3)
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()