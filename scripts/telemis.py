# import required library
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get chrome driver
chrome_service = ChromeService(r"..\drivers\chromedriver.exe")


# add options for the driver
options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

# assign options to the driver
driver = webdriver.Chrome(service=chrome_service, options=options)

# open web page
driver.get("https://be-test22:8443/site/")
time.sleep(1)

# login = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
# login.click()
# time.sleep(1)

# signup = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign up')]")
# signup.click()
# time.sleep(1)

# signup = driver.find_element(By.XPATH, "//button[contains(text(), 'Register with an email')]")
# signup.click()
# time.sleep(1)
