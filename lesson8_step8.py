from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("dsf@gmail.com")

    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file_answer = browser.find_element(By.ID, "file")
    file_answer.send_keys(file_path)
    
    
  
        # Нажимаем на кнопку Submit
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    # Ждем появления результата
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()