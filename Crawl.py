from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url='https://www.adamchoi.co.uk/overs/detailed'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

s=Service(r"C:\Users\asus\Documents\Projects\Basic_Selenium_Spider\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=s, options=options)
driver.get(url)

records=driver.find_elements(By.XPATH,'//td')
time.sleep(5)
for r in records:
    print(r.text)

