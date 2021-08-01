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
logout =WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class='woocommerce-MyAccount-navigation']>ul"),"Logout"))
time.sleep(3)
if logout is not None:
    print ("Элемент Logout есть на текущей странице")
else:
    print ("Ошибка")
driver.quit()