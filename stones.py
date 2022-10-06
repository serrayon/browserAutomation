from selenium import webdriver 
from selenium.webdriver.common.by import By

# Test Setup
driver = webdriver.Chrome()
driver.get('https://techstepacademy.com/trial-of-the-stones')
# Riddle of Stone
input1Path = "input[id='r1Input']"
element = driver.find_element(By.CSS_SELECTOR, input1Path)
input1Element = driver.find_element(By.CSS_SELECTOR, input1Path)
input1Element.send_keys("rock")

# Riddle of Stone button
btn_1_Path = "button[id='r1Btn']"
btn_element = driver.find_element(By.CSS_SELECTOR, btn_1_Path)
btn1_Element = driver.find_element(By.CSS_SELECTOR, btn_1_Path)
btn1_Element.click()


"""""
# Riddle of Stone retrieve answer
bamboo_path = "div[id='passwordBanner'] >4"
bamboo_element = driver.find_element(By.CSS_SELECTOR, bamboo_path)

answer_1 = driver.find_element(By.CSS_SELECTOR, bamboo_path)
password = answer_1
text = driver.find_element(By.CSS_SELECTOR, bamboo_path).text
bamboo_element.send_keys(text)
"""""
input_2_Path = "input[id='r2Input']"
element_2 = driver.find_element(By.CSS_SELECTOR, input_2_Path)
input2Element = driver.find_element(By.CSS_SELECTOR,input_2_Path)
input2Element.send_keys('bamboo')

btn2_Path = "button#r2Butn"
btn2_element =  driver.find_element(By.CSS_SELECTOR, btn2_Path)

btn2_element.click()

# Two Merchants
input3_Path = "input[id='r3Input']"
input3_element = driver.find_element(By.CSS_SELECTOR, input3_Path)
input3_element.send_keys('Jessica')

btn3_Path = "button#r3Butn"
btn3_element =  driver.find_element(By.CSS_SELECTOR, btn3_Path)
btn3_element.click()

btn4_Path = "button[id='checkButn']"
btn4_element =  driver.find_element(By.CSS_SELECTOR, btn4_Path)
btn4_element.click()

msg_Path = "div[id='trialCompleteBanner'] >h4"
complete_msg = driver.find_element(By.CSS_SELECTOR,msg_Path)
# Run Script
assert complete_msg.text == 'Trial Complete'