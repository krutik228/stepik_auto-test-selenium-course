from selenium import webdriver
import time, os

link = "http://suninjuly.github.io/file_input.html"

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser = webdriver.Chrome()
    browser.get(link)

    inputs = ['Nikita', 'Krutikov', 'test@gmail.com', file_path]

    for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
        element.send_keys(value)

    browser.find_element_by_css_selector(".btn.btn-primary").click()
finally:
    time.sleep(5)
    browser.quit()
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))