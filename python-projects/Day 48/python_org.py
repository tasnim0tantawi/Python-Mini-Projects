from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
website = "https://www.python.org/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(website)
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li a")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
for date in dates:
    print(date.text)
for event in events:
    print(event.text)

events_dict = {}
for event in events:
    events_dict[event.text] = dates[events.index(event)].text
print(events_dict)
driver.close()