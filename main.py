# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("python")

driver.find_element_by_id('su').click()

time.sleep(6)

driver.quit()
