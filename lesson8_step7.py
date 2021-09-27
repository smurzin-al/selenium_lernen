from selenium import webdriver
import time,os



try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("[name='firstname']").send_keys('firstname')
    browser.find_element_by_css_selector("[name='lastname']").send_keys('lastname')
    browser.find_element_by_css_selector("[name='email']").send_keys('email@email.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_css_selector('#file').send_keys(file_path)
    browser.find_element_by_css_selector('.btn-primary').click()
finally:
    time.sleep(15)
    browser.quit()

