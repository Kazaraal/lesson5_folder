import booking.constants as const
import os
from selenium import webdriver

# Create a class (this is object-oriented)
class Booking(webdriver.Chrome):
    def __init__(self, driver_path="$PATH", teardown=False):
        self.driver_path = driver_path
        self.teardown =  teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
