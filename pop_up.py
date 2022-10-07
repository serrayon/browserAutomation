from operator import mod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

class PopUp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_login(self):
        driver = self.driver
        try:
            driver.get('https://footlocker.com/')
            driver.maximize_window()
        except Exception as ex:
            print(ex)
        else:
            wait = WebDriverWait(driver,10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/header/nav[1]/div/div[2]/button')))
            element.click()
            time.sleep(5)
        
            modal_element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="SignIn_email_uid"]')))
            modal_element.click()
            modal_element.send_keys('serrayon81@gmail.com')
            time.sleep(4)
            
            modal_password = driver.find_element(By.XPATH, '//*[@id="SignIn_password_password"]')
            modal_password.click()
            time.sleep(2)
            modal_password.send_keys('1234Pass!')
            time.sleep(3)

            sign_in_element = driver.find_element(By.XPATH,'//*[@id="SignIn"]/ul/li[3]/button')
            sign_in_element.click()
            time.sleep(3)
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()



