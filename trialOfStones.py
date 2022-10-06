from lib2to3.pgen2 import driver


# Our Test 
from selenium import webdriver 
from selenium.webdriver.common.by import By

# Test Setup
broswer = webdriver.Chrome()
driver.get('https://techstepacademy.com/trial-of-the-stones')


# Riddle of stone
stone_Path = "r1Input"
stone_input = driver.find_element(By.CSS_SELECTOR,stone_Path)

stone_path_btn = "button[id='r1Btn']"
stone_answer_butn = driver.find_element(By.CSS_SELECTOR,stone_path_btn)
result_path = "div[id=['passwordBanner > h4']"
stone_result = driver.find_element_by(By.CSS_SELECTOR,result_path)
# Riddle of Secrets
secrets_path = "input[id='r2Input']"
secrets_input = driver.find_element_by(By.CSS_SELECTOR,secrets_path)
secrets_answer_path = "button#r2Butn"
secrets_answer_butn = driver.find_element_by(By.CSS_SELECTOR,secrets_answer_path) 
# Two Merchants
# Simple way
merchant_Path = "//p[text()='3000'] /../span"
richest_merchant_name = driver.find_element_by(By.XPATH,merchant_Path).text

merchant_input_path = 'input=id"r3Input"]'
merchant_input = driver.find_element_by(By.CSS_SELECTOR,merchant_input_path)

merch_ans_path = "button[id='r3Butn']"
merchant_answer_butn = driver.find_element_by(By.CSS_SELECTOR,merch_ans_path)

check_Path = "button[name='checkButn']"
check_butn = driver.find_element_by(By.CSS_SELECTOR,check_Path)

msg_Path = "div[id='trialCompleteBanner h4']"
complete_msg = driver.find_element_by(By.CSS_SELECTOR,msg_Path)
# Run Script

stone_result.send_keys('rock')
stone_answer_butn.click()
password = stone_result.text

secrets_input.send_keys(password)
secrets_answer_butn.cllick()

merchant_input.send_keys(richest_merchant_name)
merchant_answer_butn.click()

check_butn.click()
assert complete_msg.text == 'Trial Complete'

'''
element = browser.find_element(By.CSS_SELECTOR, input1Path)
input1Element = browser.find_element(By.CSS_SELECTOR, input1Path)'''
