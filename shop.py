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
time.sleep(3)
login = driver.find_element_by_css_selector("[name='login']").click()
time.sleep(3)
shop = driver.find_element_by_xpath("//ul[@id='main-nav']//li[1]//a").click()
driver.execute_script("window.scroll(0,300);")
book_html5 = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
time.sleep(3)
title = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class='summary entry-summary']>h1"),"HTML5 Forms"))
if title is not None:
    print ("Заголовок книги HTML5 Forms")
else:
    print ("Заголовок книги другой")
time.sleep(3)
driver.quit()
