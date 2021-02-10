from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #  Считаем функцию для капчи
    y = calc(int(browser.find_element_by_id("input_value").text))
    #  Вводим ответ в поле ввода
    browser.find_element_by_id("answer").send_keys(y)
    #  Ищем кнопки, скроллим до них, нажимаем
    for selector in ("#robotCheckbox", "#robotsRule", ".btn.btn-primary"):
        button = browser.find_element_by_css_selector(selector)
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

finally:
    time.sleep(5)
    browser.quit()