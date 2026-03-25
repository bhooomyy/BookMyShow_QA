'''

@author: BHOOMI
'''
from selenium import webdriver 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pandas.tests.arrays import integer

user_name = "testbhoomi01@gmail.com" 


driver_service = Service(executable_path="F:/4TH YEAR SEM8/eclips-workspace/BookMyShowMovie/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
#wait = WebDriverWait(driver, 30)
driver.maximize_window()

# for opening the desired city
x="ahmedabad"
driver.get("https://in.bookmyshow.com/"+x)

driver.find_element(By.ID,"wzrk-cancel").click()

driver.find_element(By.CLASS_NAME,"sc-chbbiW.bQENkS").click()
driver.find_element(By.XPATH, "//*[text()='Continue with Email']").click()
element = driver.find_element(By.XPATH, "//*[@id='emailId']") 
element.send_keys(user_name) 
driver.find_element(By.XPATH, "//*[text()='Continue']").click()

input_otp = input()
otp = input_otp.split()

for i in range(len(otp)):
    otp[i] = int(otp[i])
    
for i in range(1,7):    
    element=driver.find_element(By.CLASS_NAME, "sc-cmTdod.iYSxQN")
    element.send_keys(otp[i-1])

#element.send_keys(Keys.RETURN) 
#element.close()
