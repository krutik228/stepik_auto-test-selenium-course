from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #  Считаем функцию, для ввода в капчу
    y = calc(browser.find_element_by_id("input_value").text)

    #  Отправляем ответ
    input1 = browser.find_element_by_id("answer").send_keys(y)

    #  Ищем чекбокс, кликаем на него
    browser.find_element_by_id("robotCheckbox").click()

    #  Ищем радиоботтон, кликаем на него
    browser.find_element_by_id("robotsRule").click()

    #  Кнопка отправки анкеты
    browser.find_element_by_css_selector(".btn.btn-default").click()

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
