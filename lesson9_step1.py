from selenium import webdriver
import time,math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector('.btn-primary').click()
    browser.switch_to.alert.accept()
    x=browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_css_selector('.btn-primary').click()

finally:
    time.sleep(14)
    browser.quit()

