from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Selenium is a web browser automation tool
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
shop = "https://www.shopkees.com/uae-en/mobile-phones-tablets"
driver.get(shop)
search = driver.find_element(By.CSS_SELECTOR, ".input-group #main_search_input")
print(search.get_attribute("placeholder"))
search.send_keys("Apple Pencil")
search.send_keys(Keys.ENTER)


driver.close()
