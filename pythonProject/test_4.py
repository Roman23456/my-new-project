from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответы")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
import math
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/find_xpath_form")


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    first_name = browser.find_element(By.XPATH, "//input[@id='answer']")
    first_name.send_keys()


    # # Находим кнопку "Submit" с помощью XPath по ее тексту
    # submit_button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    # submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файл