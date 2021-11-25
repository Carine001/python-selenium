# import required library
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

# username
username = driver.find_element(By.ID, "username")
username.send_keys("radio")

# password
password = driver.find_element(By.ID, "password")
password.send_keys("radio")

login = driver.find_element(By.NAME, "login")
login.click()

dicomgate = driver.find_element(By.ID, "mat-expansion-panel-header-6")
dicomgate.click()

selectdicom = driver.find_element(By.LINK_TEXT, "Dicom gate")
selectdicom.click()

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[src^='https://be-test22:9920']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-success"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "id"))).send_keys("test")

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "div[.//span[contains(text(), 'STORE')]]"))).click()

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "//mat-select[name = 'scope']"))).click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "mat-checkbox-2-input"))).click()

# name = driver.find_element(By.NAME, "id")
# password.send_keys("test")

# search = driver.find_element(By.XPATH, "//input[@name='query']")
# search.send_keys("Jean")
# search.send_keys(Keys.RETURN)


# leave the iframe
driver.switch_to.default_content()
time.sleep(3)
driver.quit()
