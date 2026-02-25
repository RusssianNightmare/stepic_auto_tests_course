from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1_element = browser.find_element(By.ID, "input_value")
    x_1 = num1_element.text
        # Вычисляем значение функции
    y = calc(x_1)
    
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 100);")
    
    checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
    checkbox_robot.click()

    # Выбираем radiobutton "Robots rule!"
    radiobutton_rule = browser.find_element(By.ID, "robotsRule")
    radiobutton_rule.click()

        # Нажимаем на кнопку Submit
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # Ждем появления результата
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()