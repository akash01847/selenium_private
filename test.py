from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = "student"
password = "Password123"

mydriver = webdriver.Chrome()
# search = input("Enter your query: ")
# mydriver.get(search)
mydriver.get("https://practicetestautomation.com/practice-test-login/")

items = mydriver.find_elements(By.XPATH, '//li')
for item in items:
    print(item.text)

mydriver.find_element(By.XPATH,'//input[@name="username"]').send_keys(username)
# mydriver.find_element(By.ID['password']).clear()
mydriver.find_element(By.XPATH,'//input[@name="password"]').send_keys(password)
time.sleep(3)
mydriver.find_element(By.XPATH,'//*[@class="btn"]').click()
time.sleep(10)
print("Successfully Injected.")


mydriver.find_element(By.XPATH,'//*[@class="wp-block-button__link has-text-color has-background has-very-dark-gray-background-color"]').click()

time.sleep(5)

