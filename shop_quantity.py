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
time.sleep(1)
categ_html = driver.find_element_by_css_selector("[class='product-categories']>li:nth-child(2)>a").click()
time.sleep(1)
quantity = driver.find_elements(By.CSS_SELECTOR,"[class='products masonry-done']>li")
print("Количество товаров на странице","= "+str(len(quantity)))
driver.quit()
