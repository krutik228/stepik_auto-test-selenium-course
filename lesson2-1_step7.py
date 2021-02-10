from selenium import webdriver
import time,math

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #  Ищем картинку, берём у неё атрибут "valuex", подставляем его в функцию и считаем
    y = calc(browser.find_element_by_id("treasure").get_attribute("valuex"))
    #  Вставляем полученный ответ в поле ввода
    browser.find_element_by_id("answer").send_keys(y)

    #  Отмечаем чекбоксы
    for selector in ('#robotCheckbox', '#robotsRule', '.btn.btn-default'):
        browser.find_element_by_css_selector(selector).click()

    #  Ответ для степика в консоль
    print(browser.switch_to.alert.text)

finally:
    time.sleep(5)
    browser.quit()