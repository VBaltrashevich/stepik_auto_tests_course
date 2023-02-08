# пример из книжки
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver
driver.get("http://www.python.org")
time.sleep(5)
assert 'Python' in driver.title
# elem = driver.find_element_by_name("q")
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
elem = driver.find_element(By.CSS_SELECTOR, ".search-field")

# elem = driver.find_element("q")
# elem = driver.find_element(by.)
elem.send_keys("pycon")
time.sleep(5)
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
# print(driver.page_source)
driver.close()

