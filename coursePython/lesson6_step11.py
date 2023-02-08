from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
#    link = "http://suninjuly.github.io/registration1.html"    # успешно
#    link = "http://suninjuly.github.io/registration2.html"    # не ошибка, а предупреждение

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    input1.send_keys("Vladimir")
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input1.send_keys("Baltrashevich")
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    input1.send_keys("vbaltr@bug.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла