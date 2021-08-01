import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
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
time.sleep(2)
default_sort = driver.find_element_by_css_selector("[value='menu_order']")
default_sort_selected = default_sort.get_attribute("selected")
if default_sort_selected is not None:
    print("Выбрана сортировка defaul sorting")
else:
    print("Other sorting")
driver.execute_script("window.scrollBy(0,400);")
time.sleep(3)
how_to_low = driver.find_element_by_css_selector("[name='orderby']")
select = Select(how_to_low)
select.select_by_value("price-desc")
time.sleep(3)
cheking_how_to_low = driver.find_element_by_css_selector("[value='price-desc']")
cheking_how_to_low_selected = cheking_how_to_low.get_attribute("selected")
if cheking_how_to_low_selected is not None:
    print ("Выбрана сортировка how-to-low")
else:
    print("Other sorting")
driver.quit()






