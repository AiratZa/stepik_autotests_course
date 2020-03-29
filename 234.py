from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/alert_accept.html")

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element_by_id("input_value").text)
    ans = calc(x)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(ans)


    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
