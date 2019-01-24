import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
driver.get("http://mail.google.com")
email = driver.find_element_by_id("identifierId")
email.send_keys('bvsubbareddy414@gmail.com')
time.sleep(2)
next=driver.find_element_by_id("identifierNext")
next.click()
pass_word = driver.find_element_by_class_name("whsOnd")
pass_word.send_keys("bijjam.1992")

#time.sleep(10)
button=driver.find_element_by_id("passwordNext")
button.click()

time.sleep(20)
driver.maximize_window()
driver.refresh()