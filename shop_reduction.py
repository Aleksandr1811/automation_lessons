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
email = driver.find_element_by_css_selector("[id='username']")
email.send_keys("nhasvet@gmail.com")
passw = driver.find_element_by_css_selector("[id='password']")
passw.send_keys("Alex0845$?")
time.sleep(1)
login = driver.find_element_by_css_selector("[name='login']").click()
time.sleep(1)
shop = driver.find_element_by_xpath("//ul[@id='main-nav']//li[1]//a").click()
driver.execute_script("window.scrollBy(0,400);")
time.sleep(1)
android = driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
old_price = driver.find_element_by_xpath("//p[@class='price']/del/span")
old_price_text = old_price.text
assert old_price_text == '₹600.00'
new_price = driver.find_element_by_xpath("//p[@class='price']/ins/span")
new_price_text =new_price.text
assert new_price_text == '₹450.00'
cover_android = driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
cover = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"fullResImage")))
close = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[class='pp_close']")))
close.click()
time.sleep(5)
driver.quit()
