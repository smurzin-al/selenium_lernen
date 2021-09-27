from selenium import webdriver
import time,math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'https://vk.com/'
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    browser.find_element_by_css_selector('#index_email').send_keys('war7@bk.ru')
    browser.find_element_by_css_selector('#index_pass').send_keys('Wa013')
    browser.find_element_by_css_selector('#index_login_button').click()

    messanger = browser.find_elements_by_css_selector(' span.left_label.inl_bl')
    for el in messanger:
        if el.text == 'Мессенджер':
            el.click()
    dialogs = browser.find_element_by_css_selector('#im_dialogs_search')
    dialogs.send_keys('Избранное')
    talks = browser.find_elements_by_css_selector('span._im_dialog_link')
    for el in talks:
        if el.text == 'Избранное':
            el.click()
            break

    editor = browser.find_element_by_css_selector('.im_editable')
    editor.click()
    editor.send_keys('gggggg'+'\n')
    browser.find_element_by_css_selector('.im_editable').click()

finally:
    time.sleep(20)
    browser.quit()

