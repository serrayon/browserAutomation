from selenium import webdriver

# Helps with recording, not required
opts = webdriver.ChromeOptions()
opts.add_argument('--disable-gpu')
browser1 = webdriver.Chrome(chrome_options=opts)
browser2 = webdriver.Chrome(chrome_options=opts)


browser1.get('http://techstepacademy.com/training-ground')
browser2.get('https://www.erowid.org/')


#browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
#browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
#browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')
#browser1.execute_script('window.open("http://techstepacademy.com/training-ground","_blank");')