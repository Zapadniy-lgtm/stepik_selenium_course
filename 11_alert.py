from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))                 
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

