from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import sys
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.redbus.in")
source=driver.find_element_by_id("src")
source.send_keys("darsi")
#source=sys.argv[1]
dest=driver.find_element_by_id("dest")
dest.send_keys("Hyderabad")
#dest=sys.argv[2]
date=driver.find_element_by_class_name("text-trans-uc")

date.send_keys("19-Jan-2019")
time.sleep(10)
search=driver.find_element_by_id("search_btn")
search.click()