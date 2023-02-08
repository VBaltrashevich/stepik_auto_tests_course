from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link="http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
  browser = webdriver.Chrome()
  browser.get(link)
  image = browser.find_element(By.TAG_NAME, "img")
  x = image.get_attribute("valuex")
  y = calc(x)
  answer=browser.find_element(By.ID, "answer")
  answer.send_keys(y)
  browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
  browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
  browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()