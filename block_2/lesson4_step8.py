from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id('book')
    lable_text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    x = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_id('solve').click()


    ###################

    alert = browser.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    answer = alert_text[-1]

    browser.get('https://stepik.org/catalog?auth=login&language=ru')
    time.sleep(5)

    browser.find_element_by_id('id_login_email').send_keys('***')  # здесь вводится e-mail
    browser.find_element_by_id('id_login_password').send_keys('***')  # здесь вводится пароль

    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)
    browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')
    time.sleep(3)

    answer_input = browser.find_element_by_css_selector('textarea')
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(answer)

    button = browser.find_element_by_class_name('submit-submission')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()