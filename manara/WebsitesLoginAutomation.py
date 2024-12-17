import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Selenium setup
service = Service(executable_path='D:\\manara\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://temp-mail.io/")

# Wait for the email field to be populated (input box with class "email__input")
try:
    # Wait until the email input field is present and populated
    email_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.email__input"))
    )

    # Wait a few seconds to ensure the email is fully loaded
    time.sleep(5)

    # Extract the value (temporary email)
    temp_email = email_element.get_attribute("value")
    print(f"Scraped email: {temp_email}")

except Exception as e:
    print(f"Error: {e}")


# Open the signup page and fill the form with the scraped email

# Open the Manara signup page in a new tab
driver.execute_script("window.open('https://app.manara.tech/auth/signup', '_blank');")

# Switch to the newly opened tab (Manara signup page)
driver.switch_to.window(driver.window_handles[1])  # Switch to the second tab

# Fill out the form with dynamic values
firstName = driver.find_element(By.ID, "firstName")
firstName.send_keys("mohamed")

lastName = driver.find_element(By.ID, "lastName")
lastName.send_keys("mohsen")

email = driver.find_element(By.ID, "email")
email.send_keys(temp_email)

# Interact with the checkbox
tospp = driver.find_element(By.ID, "tospp")
tospp.click()  # Use click() for checkboxes

# Submit the form
submit_button = driver.find_element(By.CSS_SELECTOR, "button.inline-flex")
submit_button.click()
time.sleep(5)
driver.close()  # Closes the current window

# Open Temp-Mail.io in another tab for verification
driver.switch_to.window(driver.window_handles[0])  # Switch to the first tab (Temp-Mail)
try:
    print("Waiting for an email message to appear...")

    # Wait for the email container (list item) to load
    email_message = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-qa='message']"))
    )
    # Click on the email to open it
    email_message.click()  # Click on the email message to view the full content

     # Wait for the email content to load after clicking on it
    email_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".message__body"))
    )

    # Wait for the "Verify" link to be present in the email body
    verify_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='https://click.pstmrk.it']"))
    )
    # Click on the verify link
    verify_link.click()  # Click on the verify link
    print("Clicked on the verify link.")

except Exception as e:
    print(f"Error during email verification: {e}")


# --- Select Gender ---
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'gender'))  # Change the selector if needed
)

# Interact with the dropdown element
select = Select(dropdown)
select.select_by_visible_text('Mela')  # Choose the option 'Mela'


# Keep the browser open for manual inspection
input("Press Enter to exit...")  # Optional to keep the browser open

# Do not close the browser, it will stay open
# driver.quit()  # Commented out to keep the browser open
