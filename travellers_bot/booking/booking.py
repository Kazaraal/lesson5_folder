import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a class (this is object-oriented)
class Booking(webdriver.Chrome):
    def __init__(self, driver_path="$PATH", teardown=False):
        self.driver_path = driver_path
        self.teardown =  teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_elements(By.XPATH("(//span[@class='e4adce92df'][normalize-space()='Register'])[1]"))
        currency_element.click()
        print("In change currency")