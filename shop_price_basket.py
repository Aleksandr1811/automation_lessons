import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver =webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)
shop = driver.find_element_by_xpath("//ul[@id='main-nav']//li[1]//a").click()
driver.execute_script("window.scrollBy(0,400);")
basket_html = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(1)
item = driver.find_element_by_css_selector("[class='cartcontents']")
item_text = item.text
assert item_text == "1 Item"
price = driver.find_element_by_css_selector("[class='amount']")
price_text = price.text
assert price_text == "₹180.00"
basket = driver.find_element_by_css_selector("[class='wpmenucart-contents']").click()
subtotal = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'[data-title="Subtotal"]>span'),"180.00"))
if subtotal is not None:
    print ("Цена в Subtotal отобразилась")
else:
    print ("Ошибка")
total = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class='cart_totals ']>table>tbody>tr:nth-child(3)>td"),"189.00"))
if total is not None:
    print("Цена в Total отобразилась")
else:
    print("Ошибка")
driver.quit()