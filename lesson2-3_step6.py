from selenium import webdriver
import time, math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector(".trollface.btn.btn-primary").click()
    browser.switch_to_window(browser.window_handles[1])
    y = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(calc(y))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()