from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    # Открываем первую страницу для проверки (она должна работать)
    browser.get("http://suninjuly.github.io/registration1.html")

    # Находим все необходимые поля по их уникальному атрибуту 'placeholder'
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']") # <-- Этот элемент НЕ существует на registration2.html
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")

    # Заполняем поля
    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("ipetrov@example.com")

    # Находим кнопку Submit по ее тексту
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    # Проверяем, что тест прошел успешно на первой странице
    # (Обычно здесь был бы код для проверки результата)

    # Теперь переходим на вторую страницу, где есть баг (нет поля "Last name")
    browser.get("http://suninjuly.github.io/registration2.html")

    # Используем те же самые селекторы
    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    # Следующая строка вызовет NoSuchElementException, так как элемента с placeholder='Input your last name' на этой странице нет!
    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")

    # Заполняем поля
    first_name.send_keys("Ivan")
    last_name.send_keys("Petrov")
    email.send_keys("ipetrov@example.com")

    # Находим кнопку Submit по ее тексту
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # Успеваем скопировать код за 30 секунд
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла