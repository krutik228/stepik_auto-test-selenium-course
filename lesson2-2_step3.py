from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #  Находим два числа суммы
    num1, num2 = (browser.find_element_by_id(name).text for name in ["num1", "num2"])
    #  Открываем селект
    select = Select(browser.find_element_by_tag_name("select"))
    #  Складываем числа и выбираем полученный ответ в селекте
    select.select_by_value(str(eval(f"{num1}+{num2}")))
    #  Сабмитим
    browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(5)
    browser.quit()


