from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)

# Locate the search bar element by name
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()

# Enter the search term and submit the form
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# Print the current URL
print(driver.current_url)

# Close the driver
driver.close()