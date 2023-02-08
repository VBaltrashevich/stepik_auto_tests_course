from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link="http://suninjuly.github.io/selects1.html"
#link="http://suninjuly.github.io/selects2.html"

try:
  browser = webdriver.Chrome()
  browser.get(link)
  x = browser.find_element(By.ID, "num1").text
  y = browser.find_element(By.ID, "num2").text
  z = str(str(int(x)+int(y)))
  select = Select(browser.find_element(By.TAG_NAME, "select"))
  select.select_by_value(z)
  browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()