from selenium import webdriver
import time

link="http://suninjuly.github.io/wait1.html"

try:
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_id("verify").click()
    assert "successful" in browser.find_element_by_id("verify_message").text


finally:
    time.sleep(5)
    browser.quit()
