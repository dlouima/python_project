from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "Your email address"
ACCOUNT_PASSWORD = "password"
chrome_driver = "/Your_path_here/chromedriver"
driver = webdriver.Chrome(chrome_driver)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys('Your phone number')

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()

next_step_1 = driver.find_element_by_id('ember551')
next_step_1.click()