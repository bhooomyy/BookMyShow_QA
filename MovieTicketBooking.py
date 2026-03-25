'''
@author: BHOOMI
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import datetime, random
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from asyncio.tasks import wait


t1=datetime.datetime.now()
t=t1.strftime("%d")
t=int(t)
x=input("Enter the location: ")
y=input("Enter the name of show, movie, event etc: ")
z=input("The tickets are available for five days including today so, tell us when do you want to go? (Enter the date) ")
z=int(z)
n=input("How many guys are going? ")
n=int(n)
m=input("Enter mall preference. ")
ticket=input("Do you want mobile ticket or pickup from box-office? [m/b] ")
eat=input("The cinema has a variety of eatables, want some?[y/n] ")

#location="ahmedabad"
#showName="RRR"
if eat == "y":
    print("Here is the list of available items")
    print("Just enter the index no. of your favourite snack")
    print("and boom! We'll serve it to you while you watch your favourite movie.")

    print("1) Veg Samosa")
    print("2) Combo2 (Cheese)")
    print("3) Combo3 (Cheese)")
    print("4) Rock N Roll fries peri-peri")
    print("5) Large cheese popcorn")
    print("6) Veg samosa combo")
    print("7) Sweet corn 127gm")
    print("8) Cold coffee 320ml")
    print("9) Combo2 (salted)")
    print("10) Regular cheese popcorn")
    print("11) Small salted popcorn 50gm")
    print("12) Nachos")
    print("13) Large pepsi 810ml")
    print("14) Regular Pepsi 675ml")
    print("15) Small cheese popcorn 50gm")
    print("16) Redbull 330ml")
    print("17) Mega salted popcorn 240gm")
    print("18) Veg dimsum 6Pcs")
    print("19) Paneer tikkar sandwich")
    print("20) Cold Coffee mocha 320ml")
    print("21) Combo3 (salted)")
    print("22) Combo1(cheese)")
    print("23) Regular chat popcorn")
    print("24) Small pepsi 540ml")
    print("25) Veggie mint chutney burger")
    print("26) Crispy paneer burger")
    print("27) Combo2 (Chat)")
    print("28) Snickers twin 80gm")
    print("29) Combo3 (caramel)")
    print("30) Garden fresh veggie foccacia snadwitch")
    print("31) Americano")
    print("32) Green apple lemonade")
    print("33) Rock N Roll Fries moroccan 140gms")
    print("34) Rock N Roll fries smoky BBQ 140gms")
    food = input()
    food = int(food)

email=input("Please enter your email address. ")
pno=input("Please enter your phone number. ")



driver_service = Service(executable_path="F:/4TH YEAR SEM8/eclips-workspace/BookMyShowMovie/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
wait = WebDriverWait(driver, 60)
driver.maximize_window()

# for opening the desired city
driver.get("https://in.bookmyshow.com/"+x)

#driver.implicitly_wait(5)
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='wzrk-cancel']")))
# for eliminating the popup
try:
    driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()
except:
    print("No Pop-Up detected")

driver.find_element(By.CLASS_NAME, "sc-ebFjAB.bqfntN").click()
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sc-ebFjAB.bqfntN")))
show = driver.find_element(By.CLASS_NAME, "sc-jWojfa.eTcNgn") 
#sc-ebFjAB.bqfntN
show.send_keys(y)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sc-ccLTTT.eDIYWP")))
driver.find_element(By.CLASS_NAME,"sc-ccLTTT.eDIYWP").click()
driver.find_element(By.CLASS_NAME,"sc-1vmod7e-2.cgQNto").click()


if z==t:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='showDates']/div/div/li[1]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[1]").click()
    except:
        print("The show is not available on th current date :(")

elif z==t+1:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[2]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[2]").click()
    except:
        print("The show is not available on th current date :(")

elif z==t+2:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[3]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[3]").click()
    except:
        print("The show is not available on th current date :(")

elif z==t+3:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[4]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[4]").click()
    except:
        print("The show is not available on th current date :(")

elif z==t+4:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[5]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[5]").click()
    except:
        print("The show is not available on th current date :(")
elif z==t+5:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[6]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[5]").click()
    except:
        print("The show is not available on th current date :(")
elif z==t+6:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[7]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[5]").click()
    except:
        print("The show is not available on th current date :(")
elif z==t+7:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='showDates']/div/div/li[8]")))
        driver.find_element(By.XPATH, "//*[@id='showDates']/div/div/li[5]").click()
    except:
        print("The show is not available on th current date :(")


wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fltrsearch']")))
select = driver.find_element(By.XPATH,"//*[@id='fltrsearch']")
if m!="none":
    select.send_keys(m)
    driver.find_element(By.XPATH,"//*[@id='venuelist']/li[2]/div[2]/div[2]/div").click()
    select.send_keys(Keys.RETURN)

#try:
#    driver.find_element(By.CSS_SELECTOR,"#venuelist > li:nth-child(4) > div.body > div:nth-child(1) > a").click()
#except:
#    print("Sorry, show is either full or no available :(")
# #venuelist > li:nth-child(4) > div.body > div:nth-child(1) > a
# #venuelist > li:nth-child(1) > div.body > div > a


try:
    driver.find_element(By.XPATH,"//*[@id='btnPopupAccept']").click()
except:
    print("No Acceptance")


# for no. of seats
if n==1:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_1']")))
    driver.find_element(By.ID,"//*[@id='pop_1']").click()
elif n==2:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_2']")))
    driver.find_element(By.XPATH,"//*[@id='pop_2']").click()
elif n==3:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_3']")))
    driver.find_element(By.XPATH,"//*[@id='pop_3']").click()
elif n==4:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_4']")))
    driver.find_element(By.XPATH,"//*[@id='pop_4']").click()
elif n==5:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_5']")))
    driver.find_element(By.XPATH,"//*[@id='pop_5']").click()
elif n==6:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_6']")))
    driver.find_element(By.XPATH,"//*[@id='pop_6']").click()
elif n==7:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_7']")))
    driver.find_element(By.XPATH,"//*[@id='pop_7']").click()
elif n==8:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_8']")))
    driver.find_element(By.XPATH,"//*[@id='pop_8']").click()
elif n==9:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_9']")))
    driver.find_element(By.XPATH,"//*[@id='pop_9']").click()
elif n==10:
    wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='pop_10']")))
    driver.find_element(By.XPATH,"//*[@id='pop_10']").click()

wait.until(EC.element_to_be_clickable((By.ID,"proceed-Qty")))
# for confirming seats
driver.find_element(By.ID,"proceed-Qty").click()

# #venuelist > li:nth-child(4) > div.body > div:nth-child(1) > a

seat=driver.find_elements(By.CSS_SELECTOR,"a._available")
length=len(seat)


while 1:
    r = random.randint(1, length)
    seat[r].click()
    x = driver.find_element(By.ID,"btmcntbook")
    if x.is_displayed():
        x.click()
        break
driver.implicitly_wait(3)

if ticket=="m":
    driver.find_element(By.XPATH,"//*[@id='shmticket'']").click()
else:
    driver.find_element(By.XPATH,"//*[@id='shbox']").click()


if eat == "y":
    if food == 1:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020076-716']").click()
    elif food == 2:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000139-195']").click()
    elif food == 3:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000140-174']").click()
    elif food == 4:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020022-176']").click()
    elif food == 5:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000130-320']").click()
    elif food == 6:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020045-27']").click()
    elif food == 7:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020131-685']").click()
    elif food == 8:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020101-710']").click()
    elif food == 9:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000139-196']").click()
    elif food == 10:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000130-455']").click()
    elif food == 11:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000131-433']]").click()
    elif food == 12:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020006-1749']").click()
    elif food == 13:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020009-192']").click()
    elif food == 14:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020009-631']").click()
    elif food == 15:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000131-423']").click()
    elif food == 16:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020472-274']").click()
    elif food == 17:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000132-35']").click()
    elif food == 18:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020133-720']").click()
    elif food == 19:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020047-1102']").click()
    elif food == 20:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020101-711']").click()
    elif food == 21:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000140-175']").click()
    elif food == 22:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000134-64']").click()
    elif food == 23:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000130-528']").click()
    elif food == 24:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020009-815']").click()
    elif food == 25:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020013-998']").click()
    elif food == 26:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020013-999']").click()
    elif food == 27:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000139-472']").click()
    elif food == 28:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1174632-1466']").click()
    elif food == 29:
        driver.find_element(By.XPATH,"//*[@id='add-btn_2000140-78']").click()
    elif food == 30:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020047-1103']").click()
    elif food == 31:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020080-2297']").click()
    elif food == 32:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020549-260']").click()
    elif food == 33:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020036-1083']").click()
    elif food == 34:
        driver.find_element(By.XPATH,"//*[@id='add-btn_1020036-1085']").click()

driver.find_element(By.XPATH,"//*[@id='prePay']").click()
driver.find_element(By.XPATH,"//*[@id='btnAduPopupAccept']").click()  

wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='txtEmail']")))
driver.find_element(By.XPATH,"//*[@id='txtEmail']").send_keys(email)
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='txtMobile']")))
driver.find_element(By.XPATH,"//*[@id='txtMobile']").send_keys(pno)
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='dContinueContactSec']/a")))
driver.find_element(By.XPATH,"//*[@id='dContinueContactSec']/a").click()
