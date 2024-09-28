# Download, extract and move geckodriver & chromedriver to working folder
# Chromedriver
# https://googlechromelabs.github.io/chrome-for-testing/
# Export path to chromedriver to PATH (export PATH=$PATH:/home/ken/Desktop/DevOps_Online_Training/github/to_github/chromedriver)
# Geckodriver
# https://github.com/mozilla/geckodriver/releases
# Export path to geckodriver to PATH (export PATH=$PATH:/home/ken/Desktop/DevOps_Online_Training/github/to_github/geckodriver)
# Remove the snap installer version of firefox (https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz)
# Update, upgrade and install firefox using apt 
#
# Activate said environment (source env/bin/activate)
# Install selenium (pip install selenium)

from selenium import webdriver

# Import time
import time

# Let the user provide the link they want to open
website = input("Please provide the website you want to open:\n")
# Let the user choose between Chrome and Firefox
chromeOfirefox = input("Choose either 'chrome' or 'firefox':\n")

# The webdriver.Chrome function
# This open the provided link in Chrome
def open_with_chrome(website):
    # Initialize the chrome driver
    chrome_driver = webdriver.Chrome()
    # And call the website using the driver variable
    chrome_driver.get(website)

# Call the function
# open_with_chrome(website)

# The webdriver.Firefox function
# This open the provided link in Firefox
def open_with_firefox(website):
    # Initialize the chrome driver
    firefox_driver = webdriver.Firefox()
    # And call the website using the driver variable
    firefox_driver.get(website)
    # Delay the browser on screen for specified time
    time.sleep(20)

# Call the function
# open_with_firefox(website)

# Add the logic
if chromeOfirefox == "chrome":
    open_with_chrome(website)
elif chromeOfirefox == "firefox":
    open_with_firefox(website)
else:
    print("Choose either 'chrome' or 'firefox'")

# website = https://ubuntu.com/




# https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.24.0-linux64.tar.gz


# https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz