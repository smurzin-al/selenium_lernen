from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#input_value')
    x= x_element.text
    y = calc(x)
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
