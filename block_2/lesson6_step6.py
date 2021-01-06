from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value").text
    res = calc(x_element)

    input_x = browser.find_element_by_id("answer")
    input_x.send_keys(res)

    # browser.execute_script("window.scrollBy(0, 150);")

    option1 = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    time.sleep(1)
    option2 = browser.find_element_by_css_selector('[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()