# Vladislav_Farisey.docx
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://rozetka.com.ua/"
browser = selenium.webdriver.Chrome()
browser.maximize_window()
browser.get(link)

serch_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search-form__input]")
# serch_string = browser.find_element(By.CLASS_NAME, "search-form__input ng-pristine”)
serch_string.send_keys("Мебель")
cnopka = browser.find_element(By.CSS_SELECTOR, "button[class*=button_color_green]").click()
time.sleep(2)
proverka = browser.find_element(By.CSS_SELECTOR, "h1[class*=portal__heading]").text
proverka1 = "Мебель"
if  proverka == proverka1:
    print("Тест прошел успешно")
else:
     print("Тест проверку не прошел")

Assert proverka == proverka1,f"Тест не пройден, вот что удалось найти вместо мебели -{proverka}"
time.sleep(2)
browser.quit()