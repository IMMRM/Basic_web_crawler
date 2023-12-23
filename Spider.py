from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

urls = [

    'https://www.adamchoi.co.uk/overs/detailed' 
        
        ]
s = Service(r"C:\Users\asus\Documents\Projects\Basic_Selenium_Spider\chromedriver-win64\chromedriver.exe")

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)