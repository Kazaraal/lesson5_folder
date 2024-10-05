from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the chrome driver
chrome_driver = webdriver.Chrome()

# Let the user provide the link they want to open
website = input("Please provide the website you want to open:\n")

# Open the website
chrome_driver.get(website)

# Print the title
print(chrome_driver.title)

# Search for the search area
search = chrome_driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# Close the browser
chrome_driver.quit()

# https://www.techwithtim.net/