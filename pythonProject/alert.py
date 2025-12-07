import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from datetime import datetime, timezone
# загрузить файл

# Взаимодействие с сообщением в котором есть только кнопка ОК
driver = webdriver.Chrome()
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)  # Откроется браузер
driver.maximize_window()  # откроется на весь экран
time.sleep(3)

# click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
# click_alert_button.click()
# print("click_alert_button")
# time.sleep(3)
#
# driver.switch_to.alert.accept()# switch_to позволяет обращаться к всплывающим уведомлениям делать переключения между окнами


# Взаимодействие с сообщением в котором есть только кнопка ОК  и отмена
click_alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
click_alert_button.click()
print("click_alert_button")
time.sleep(3)

# driver.switch_to.alert.accept() # Подтверждение
driver.switch_to.alert.dismiss() # Отмена