from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/redirect_accept.html")

    first_w = browser.current_window_handle

    time.sleep(1)
    button1 = browser.find_element_by_css_selector("button.trollface")
    button1.click()

    # alert = browser.switch_to.alert
    # alert.accept()
    second_w = browser.window_handles[1]
    browser.switch_to.window(second_w)

    x = int(browser.find_element_by_id("input_value").text)
    ans = calc(x)

    input1 = browser.find_element_by_css_selector("input#answer")
    input1.send_keys(ans)


    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()
    alert = browser.switch_to.alert
    ans = alert.text.split(' ')[-1]
    print(ans)
    pyperclip.copy(ans)
finally:
    time.sleep(1)

    browser.quit()
