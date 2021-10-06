import unittest
from selenium import webdriver
import time


def test_page(links):
    try:
        link = links
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('div .first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('div .first_block .second')
        input2.send_keys('Ivanov')
        input3 = browser.find_element_by_css_selector('div .first_block .third')
        input3.send_keys('1111')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(1)
        browser.quit()


class TestForm(unittest.TestCase):
    def test_form1(self):
        test_page("http://suninjuly.github.io/registration1.html")

    def test_form2(self):
        test_page("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()
