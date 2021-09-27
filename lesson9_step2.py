from selenium import webdriver
import time,math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_css_selector('.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x=browser.find_element_by_css_selector('#input_value').text
    y = calc(x)
    browser.find_element_by_css_selector('#answer').send_keys(y)
    browser.find_element_by_css_selector('.btn-primary').click()



finally:
    time.sleep(10)
    browser.quit()

