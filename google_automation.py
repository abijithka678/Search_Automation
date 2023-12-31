from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
path = 'C:\\chromedriver\\chromedriver.exe'
service_dir = Service(executable_path=path)
service_dir.start()

browser = webdriver.Chrome(service=service_dir)
browser.get('https://www.google.com')

search_box = browser.find_element(By.NAME, 'q')  # Find the search box element
search_box.send_keys('hello world')  # Send the search query

# Find the Google Search button and perform the click action
google_search_button = browser.find_element(By.NAME, 'btnK')
actions = ActionChains(browser)
actions.click(google_search_button).perform()

time.sleep(5)  # Wait for 5 seconds to see the result
browser.quit()  # Close the browser
