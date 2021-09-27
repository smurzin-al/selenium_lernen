from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element_by_css_selector('.nowrap#num1').text)
    num2 = int(browser.find_element_by_css_selector('#num2').text)
    answer = num1 + num2
    select = Select(browser.find_element_by_css_selector(".custom-select"))
    select.select_by_value(str(answer))
    browser.find_element_by_css_selector(".btn-default").click()


finally:
    time.sleep(5)
    browser.quit()

