import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)
account = driver.find_element_by_xpath("//ul[@id='main-nav']//li[2]//a").click()
email = driver.find_element_by_css_selector("[id='reg_email']")
email.send_keys("nhasvet@gmail.com")
passw = driver.find_element_by_css_selector("[id='reg_password']")
passw.send_keys("Alex0845$?k")
time.sleep(3)
register =WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[name='register']")))
register.click()
time.sleep(7)
driver.quit()