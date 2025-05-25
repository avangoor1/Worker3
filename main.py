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



def force_label_class_to_active(driver, input_id):
    """
    Force a label to stay in active class by disabling event listeners
    """
    try:
        # Find the input element by ID
        input_element = driver.find_element(By.ID, input_id)
        
        # More aggressive approach to force the active class and prevent default behaviors
        script = """
        var input = arguments[0];
        var span = input.parentElement;
        var label = span.parentElement;
        
        if (label.tagName.toLowerCase() === 'label') {
            // Clone the node to remove event listeners
            var oldLabel = label;
            var newLabel = oldLabel.cloneNode(true);
            newLabel.className = 'active';
            
            // Replace old label with new one
            oldLabel.parentNode.replaceChild(newLabel, oldLabel);
            
            // Find the input in the new structure and simulate a click
            var newInput = newLabel.querySelector('input');
            if (newInput) {
                newInput.checked = true;
            }
            
            return true;
        }
        return false;
        """
        
        result = driver.execute_script(script, input_element)
        
        if result:
            print(f"Successfully forced label active state for input with ID: {input_id}")
        else:
            print(f"Could not find a label parent for input with ID: {input_id}")
            
        return result
    except Exception as e:
        print(f"Failed to force label class: {str(e)}")
        return False

def blockTime(date, timevalue):

    options = Options()

    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
    options.add_argument("--incognito")
    options.add_argument("window-size=1200x600")
    options.add_argument('--headless') # whether you can see the program or not
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')  # Optional but often needed



    # ✅ Start Chrome with these security settings
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://walmart.clubautomation.com/member/index")

    driver.maximize_window()

    input_login = driver.find_element(By.ID, "login")

    input_login.send_keys("raghu2007")

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

    force_label_class_to_active(driver, "interval-90")

    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
    search_link = wait.until(EC.element_to_be_clickable((By.ID, "reserve-court-search")))
    now = datetime.datetime.now().time()
    target_time = datetime.time(12, 0, 0)

    while True:
        now = datetime.datetime.now().time()
        if now >= target_time:
            search_link.click()
            break
        time.sleep(0.01)  # Check every half second

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
    blockTime("06/02/2025", "4:30pm")