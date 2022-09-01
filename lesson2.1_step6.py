import math
from tkinter import Y
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure" )
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)
    button = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    button.click()
    button2 = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    button2.click()
    button3 = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button3.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла