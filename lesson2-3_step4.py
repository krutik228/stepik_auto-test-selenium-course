from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #  Переходим на всплывающее окно
    browser.find_element_by_css_selector(".btn.btn-primary").click()
    #  Принимаем всплывающее окно
    browser.switch_to.alert.accept()
    #  Берем x, считаем, вставляем, сабмитим
    y = int(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(calc(y))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()