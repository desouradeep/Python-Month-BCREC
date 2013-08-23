from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()	# opens firefox
driver.maximize_window()

driver.get('http://google.com')
assert "Google" in driver.title
elem = driver.find_element_by_xpath('//*[@id="gbqfq"]')
elem.send_keys("pycon india")	# webdriver enters data in search bar
elem.send_keys(Keys.RETURN)	# ENTER key press
sleep(2)
# Google search results loaded
elem = driver.find_element_by_xpath('//*[@id="rso"]/li/div/h3/a')
elem.send_keys(Keys.RETURN)	# ENTER pressed on first link
sleep(2)
# PyCon India page loaded
elem = driver.find_element_by_xpath('/html/body/div/nav/ul/li[6]/a')
elem.send_keys(Keys.RETURN)	# ENTER pressed on Python Month link
# Python Month page loaded
