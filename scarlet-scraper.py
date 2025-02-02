from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.marvel.com/signin')

timeout = 60

driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# email_input = WebDriverWait(driver, timeout).until(
#     EC.element_to_be_clickable((By.ID, "InputIdentityFlowValue"))

# )
# submit_button = WebDriverWait(driver, timeout).until(
#         EC.element_to_be_clickable((By.ID, "BtnSubmit"))
# )
email_input, submit_button = WebDriverWait(driver, timeout).until(
    EC.all_of(
        EC.element_to_be_clickable((By.ID, "InputIdentityFlowValue")),
        EC.element_to_be_clickable((By.ID, "BtnSubmit"))
    )
)

email_input.click()
email_input.send_keys(input("Enter your email: "))
submit_button.click()

# password_input = WebDriverWait(driver, timeout).until(
#     EC.element_to_be_clickable((By.ID, "InputPassword"))
# )
# submit_button = WebDriverWait(driver, timeout).until(
#     EC.element_to_be_clickable((By.ID, "BtnSubmit"))
# )
password_input, submit_button = WebDriverWait(driver, timeout).until(
    EC.all_of(
        EC.element_to_be_clickable((By.ID, "InputIdentityFlowValue")),
        EC.element_to_be_clickable((By.ID, "BtnSubmit"))
    )
)

password_input.click()
password_input.send_keys(getpass("Enter your password: "))
submit_button.click()

WebDriverWait(driver, 600).until(EC.url_changes(driver.current_url))

input()