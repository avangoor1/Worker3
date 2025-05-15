from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import datetime

def blockTime(date, timevalue):

    options = Options()

    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.add_argument("--incognito")
    options.add_argument("window-size=1200x600")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')  # Optional but often needed



    # ✅ Start Chrome with these security settings
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://walmart.clubautomation.com/member/index")

    driver.maximize_window()

    input_login = driver.find_element(By.ID, "login")

    input_login.send_keys("avangoor")

    input_password = driver.find_element(By.ID, "password")

    input_password.send_keys("Welcome1")

    link = driver.find_element(By.ID, "loginButton")
    link.click()

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    reservation_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Reservations")))
    reservation_link.click()

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    service_link = wait.until(EC.element_to_be_clickable((By.ID, "component_chosen")))
    service_link.click()

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    sport_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Gym')]")))
    sport_link.click()

    time.sleep(2)

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    location_link = wait.until(EC.element_to_be_clickable((By.ID, "location_chosen")))
    location_link.click()

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    gym_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Badminton')]")))
    gym_link.click()

    time.sleep(2)

    # Locate the input field by ID
    date_input = driver.find_element(By.ID, "date")

    # Clear any existing value and enter the new date
    date_input.clear()
    date_input.send_keys(date)

    time.sleep(2)

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    search_link = wait.until(EC.element_to_be_clickable((By.ID, "reserve-court-search")))
    now = datetime.datetime.now().time()
    target_time = datetime.time(12, 00, 0)

    while True:
        now = datetime.datetime.now().time()
        if now >= target_time:
            search_link.click()
            break
        time.sleep(1)  # Check every second

    try:
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
        time_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, timevalue)))
        time_link.click()    
        wait = WebDriverWait(driver, 10)
        confirm_link = wait.until(EC.element_to_be_clickable((By.ID, "confirm")))
        confirm_link.click()
        time.sleep(2)
        print("Booked court")
    except TimeoutException:
            print("Not found")



    driver.quit()


if __name__ == "__main__":
    blockTime("05/23/2025", "5:00pm")