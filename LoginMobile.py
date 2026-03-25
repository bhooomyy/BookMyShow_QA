'''
Created on 08-Apr-2022

@author: BHOOMI
'''
from selenium import webdriver 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

user_name = "8866436585" 


driver_service = Service(executable_path="F:/4TH YEAR SEM8/eclips-workspace/BookMyShowMovie/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
#wait = WebDriverWait(driver, 30)
driver.maximize_window()

# for opening the desired city
x="ahmedabad"
driver.get("https://in.bookmyshow.com/"+x)

driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()

driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
element = driver.find_element(By.XPATH, "//*[@id='mobileNo']") 
element.send_keys(user_name) 
driver.find_element(By.XPATH, "//*[text()='Continue']").click()

#otp1input = input()
#otp1input = int(otp1input)
#otp1 = driver.find_element(By.CLASS_NAME, "sc-cmTdod.iYSxQN")
#otp1.send_keys(otp1input)

#otp=[]
#for x in range(1,7):
#    x=input()
#    otp.append(int(x))

input_otp = input()
otp = input_otp.split()
for i in range(len(otp)):
    otp[i] = int(otp[i])
    
for i in range(1,7):    
    element=driver.find_element(By.CLASS_NAME, "sc-cmTdod.iYSxQN")
    element.send_keys(otp[i-1])

#element.send_keys(Keys.RETURN) 
#element.close()