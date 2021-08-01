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
time.sleep(2)
basket_js = driver.find_element_by_css_selector("[data-product_id='180']").click()
time.sleep(2)
basket = driver.find_element_by_css_selector("[class='wpmenucart-contents']").click()
time.sleep(2)
del_1_book = driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(2)
undo = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[class='woocommerce-message']>a")))
undo.click()
time.sleep(2)
quantity_js_clear = driver.find_element_by_css_selector("[type='number']").clear()
quantity_js = driver.find_element_by_css_selector("[type='number']")
quantity_js.send_keys("3")
update_basket=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[value='Update Basket']")))
time.sleep(2)
update_basket.click()
quantity_3 = driver.find_element_by_css_selector("[class='shop_table shop_table_responsive cart']>tbody>tr:nth-child(1)>td:nth-child(5)>div>input")
quantity_3_text = quantity_3.get_attribute("value")
assert quantity_3_text == "3"
time.sleep(2)
apply_coupon = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[name='apply_coupon']")))
apply_coupon.click()
time.sleep(5)
message = driver.find_element_by_css_selector("[class='woocommerce-error']>li")
message_text=message.text
assert message_text == "Please enter a coupon code."
driver.quit()