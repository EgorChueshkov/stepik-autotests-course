from selenium import webdriver
import unittest


class TestInp(unittest.TestCase):
    def test_input1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("email@com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "registration failed")

    def test_input2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("email@com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        correct_message = "Congratulations! You have successfully registered!"
        self.assertEqual(correct_message, welcome_text, "registration failed")

if __name__ == "__main__":
    unittest.main()