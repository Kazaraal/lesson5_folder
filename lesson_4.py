# # Download, extract and move geckodriver & chromedriver to working folder
# # Chromedriver
# # https://googlechromelabs.github.io/chrome-for-testing/
# # Export path to chromedriver to PATH (export PATH=$PATH:/home/ken/Desktop/DevOps_Online_Training/github/to_github/chromedriver)
# # Geckodriver
# # https://github.com/mozilla/geckodriver/releases
# # Export path to geckodriver to PATH (export PATH=$PATH:/home/ken/Desktop/DevOps_Online_Training/github/to_github/geckodriver)
# # Remove the snap installer version of firefox (https://github.com/mozilla/geckodriver/releases/download/v0.35.0/geckodriver-v0.35.0-linux64.tar.gz)
# # Update, upgrade and install firefox using apt 
# #
# # Activate said environment (source env/bin/activate)
# # Install selenium (pip install selenium)

# from selenium import webdriver

# # Import time
# import time

# # Let the user provide the link they want to open
# website = input("Please provide the website you want to open:\n")
# # Let the user choose between Chrome and Firefox
# chromeOfirefox = input("Choose either 'chrome' or 'firefox':\n")

# # The webdriver.Chrome function
# # This open the provided link in Chrome
# def open_with_chrome(website):
#     # Initialize the chrome driver
#     chrome_driver = webdriver.Chrome()
#     # And call the website using the driver variable
#     chrome_driver.get(website)

# # Call the function
# # open_with_chrome(website)

# # The webdriver.Firefox function
# # This open the provided link in Firefox
# def open_with_firefox(website):
#     # Initialize the chrome driver
#     firefox_driver = webdriver.Firefox()
#     # And call the website using the driver variable
#     firefox_driver.get(website)
#     # Delay the browser on screen for specified time
#     time.sleep(20)

# # Call the function
# # open_with_firefox(website)

# # Add the logic
# if chromeOfirefox == "chrome":
#     open_with_chrome(website)
# elif chromeOfirefox == "firefox":
#     open_with_firefox(website)
# else:
#     print("Choose either 'chrome' or 'firefox'")

# website = https://ubuntu.com/
##################################################################################

# 2.
# It's the same link
##################################################################################

# 3.
# Yes
##################################################################################

# # 4. 
# # Open Google Translate web page
# # Write anything in Hebrew in the text area

# # Import Selenium
# from selenium import webdriver
# # Import time
# import time
# # Import By
# from selenium.webdriver.common.by import By

# # Let the user provide the link they want to open
# # website = input("Please provide the website you want to open:\n")
# website = "https://translate.google.com/?sl=auto&tl=es&op=translate"

# # And also provide the words to translate
# # users_words = input("What do you want to translate?\n")
# users_words = "לְשַׁכֵּן"
# # Initialize the chrome driver
# chrome_driver = webdriver.Chrome()

# # The webdriver.Chrome function
# # This open the provided link in Chrome
# def open_with_chrome(website):
#     # And call the website using the driver variable
#     chrome_driver.get(website)
#     time.sleep(5)

#     # This accepts the cookies
#     chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span").click()
#     time.sleep(5)

# # Write something in the receiving box
# def to_translate():
#     # change_language = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button').click()
#     to_translate_location = chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/div/c-wiz/span/span/div/textarea")
#     to_translate_location.send_keys(users_words)
#     # Select the language to translate it to
#     # language_to_translate_to = chrome_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button")
#     # path_to_eng = "//div[@class='qSb8Pe RCaXn KKjvXb']//div[@class='Llmcnf'][normalize-space()='English']"
#     # language_to_translate_to_eng = chrome_driver.find_element(By.XPATH, path_to_eng)
#     # language_to_translate_to_eng.click()
#     time.sleep(5)

# # Call the function
# open_with_chrome(website)
# to_translate()
#############################################################################################

# # 5.
# # Open a Youtube web page
# # Type a name of a song
# # Click on search

# # Import webdriver
# from selenium import webdriver
# # Import By
# from selenium.webdriver.common.by import By
# # Import keys
# from selenium.webdriver.common.keys import Keys
# # Import time
# import time

# # Initialize the webdriver
# chrome_driver = webdriver.Chrome()

# # Get the website
# website = "https://www.youtube.com/"
# song_search = "top rap music"

# chrome_driver.get(website)
# time.sleep(5)

# # This accepts the cookies
# accept_cookies = chrome_driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div").click()
# time.sleep(3)

# # Go to the search area
# path_to_search = "//input[@id='search']"
# search_area = chrome_driver.find_element(By.XPATH, path_to_search)
# # Type in the given text
# search_area.send_keys(song_search)

# # Press enter
# search_area.send_keys(Keys.ENTER)

# time.sleep(10)
#################################################################################
