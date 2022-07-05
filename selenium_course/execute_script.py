'''
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
'''

import os

current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)
file_path = os.path.join(current_dir, 'Text.txt')
