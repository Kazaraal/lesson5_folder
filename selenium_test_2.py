from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the website and maximise the window
chrome_driver.get("https://booking.com")
time.sleep(2)
chrome_driver.maximize_window()
time.sleep(2)
try:
    # Accept the cookies
    accept_cookies = chrome_driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies.click()
except:
    pass

# Open currency options
currency_options_button = chrome_driver.find_element(By.XPATH, "//*[@id='b2indexPage']/div[2]/div/div/header/div/nav[1]/div[2]/span[1]/button/span") 
currency_options_button.click()
time.sleep(3)
# Choose GBP from the options
gbp_currency = chrome_driver.find_element(By.XPATH, "//*[@id='header_currency_picker']/div/div/div[2]/div/div[3]/div/div/div/ul[1]/li[1]/button/div/div[1]")
gbp_currency.click()
# Delay here
time.sleep(10)