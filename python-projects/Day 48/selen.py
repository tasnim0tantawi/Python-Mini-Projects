from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium is a web browser automation tool
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
apple_pencil = "https://www.shopkees.com/" \
               "bahrain-en/apple-pencil-2nd-generation/PSK/607AE7F77660D593888?gclid=" \
               "Cj0KCQjwmdGYBhDRARIsABmSEePYiSNpjWujNku-PP-zTCnRqTwgfvADPc5IwG72jeiELjkiRQQ8Lr0aAv9PEALw_wcB"
driver.get(apple_pencil)
price = driver.find_element(By.CLASS_NAME ,"product_price_amount_spotii")
print(price.text)
logo = driver.find_element(By.CLASS_NAME, "brand")
print(logo.size)
logo.click()
x_path = driver.find_element(By.XPATH, '//*[@id="navbarDropdown2"]/img')
print(x_path.get_attribute("src"))

# close() closes the current tab. quit() closes the entire browser.
driver.close()
