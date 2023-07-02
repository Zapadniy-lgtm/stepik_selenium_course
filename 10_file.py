from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

current_dir = os.path.abspath(os.path.dirname(__file__)) 
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("firstname")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("lastname")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email")
    
    input4 = browser.find_element(By.NAME, "file")
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

    
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

