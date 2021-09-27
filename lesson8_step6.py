from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    x_value = int(browser.find_element_by_css_selector('#input_value').text)
    y = calc(x_value)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_css_selector('#robotCheckbox').click()
    button = browser.find_element_by_css_selector(".btn-primary")
    browser.find_element_by_css_selector('#robotsRule').click()
    button.click()
finally:
    time.sleep(15)
    browser.quit()

