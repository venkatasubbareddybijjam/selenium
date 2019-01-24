from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.youtube.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
