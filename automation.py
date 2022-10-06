from selenium import webdriver 
browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/training-ground')
input1Path = "input[id='ipt1']"
#build locator BY.css selector or x path
from selenium.webdriver.common.by import By
element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element.send_keys("el amor")