from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
first_name = 'Tony'
last_name = 'Montana'
email = 'tony_montana@montana.com'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'Text.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys(first_name)
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys(last_name)
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys(email)
    element = browser.find_element(By.NAME, 'file')
    element.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла