from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Set the path to the ChromeDriver executable
chrome_driver_path = "C:\\chromedriver\\chromedriver.exe"

# Create a ChromeDriver service instance with the executable path
chrome_service = Service(executable_path=chrome_driver_path)

# Start the service
chrome_service.start()

# Create a Chrome webdriver instance and connect it to the service
browser = webdriver.Chrome(service=chrome_service)

browser.get('https://www.google.com')
time.sleep(100) 
# Perform your automation tasks here

# Remember to quit the browser and the service after you're done
#browser.quit()
#chrome_service.stop()
