# TESTING SELENIUM ON WEBSITE
# This test Selenium on https://trytestingthis.netlify.app/

# We will use the chrome_driver
from selenium import webdriver
# Import the By from Selenium
from selenium.webdriver.common.by import By
# Import Select
from selenium.webdriver.support.ui import Select
# We will need to control time
import time

# Make a variable of the website
website = "https://trytestingthis.netlify.app/"

# Make a variable of the Chrome driver
chrome_driver = webdriver.Chrome()

# Other variables needed
# The first name
fname = "Simon"
# The last name
lname = "Templar"

# Get the website
chrome_driver.get(website)

# Inputing the first name in the form
first_name = chrome_driver.find_element(By.ID, "fname")
first_name.send_keys(fname)

# Inputing the first name in the form
last_name = chrome_driver.find_element(By.ID, "lname")
last_name.send_keys(lname)

# Choose the gender
male_gender = chrome_driver.find_element(By.ID, "male")
male_gender.click()

# Choose options
# This is a single-select dropdown
dropdown = chrome_driver.find_element(By.XPATH, "//select[@id='option']")
dd = Select(dropdown)

dd.select_by_index(1)
time.sleep(3)

dd.select_by_value("option 2")
time.sleep(3)

dd.select_by_visible_text("Option 3")
time.sleep(3)
time.sleep(3)


# This is a multi-select dropdown option

dd_demo = chrome_driver.find_elements(By.NAME, "Optionwithcheck")

dd_multi = Select(dd_demo)

dd_multi.select_by_index(0)
time.sleep(3)

dd_multi.select_by_value("option 1")
time.sleep(3)

dd_multi.select_by_visible_text("Option 2")
# Delay page for a bit
time.sleep(10)

# //select[@id='owc']//option[@value='option'][normalize-space()='Option'] 
# //select[@id='owc']//option[@value='option 1'][normalize-space()='Option 1']
