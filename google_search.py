from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Automation step by step")
driver.maximize_window()
driver.find_element_by_name("btnK").click()
driver.find_element_by_class_name("r").find_element_by_tag_name('a').click()