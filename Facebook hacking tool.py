from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace 'your_email' and 'your_password' with your actual Facebook credentials
email = 'your_email'
password = 'your_password'

# Set up the webdriver (you need to have the appropriate driver for your browser)
driver = webdriver.Chrome()

# Navigate to the Facebook login page
driver.get('https://www.facebook.com/login')

# Find the email and password input fields and enter your credentials
email_input = driver.find_element_by_id('email')
password_input = driver.find_element_by_id('pass')
email_input.send_keys(email)
password_input.send_keys(password)

# Submit the login form
password_input.send_keys(Keys.ENTER)

# Wait for the page to load (you can adjust the time based on your internet speed)
time.sleep(5)

# Check if the login was successful
try:
    driver.find_element_by_id('userNavigationLabel')
    print('Login successful!')
except:
    print('Login failed.')

# Close the browser
driver.quit()