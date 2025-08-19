import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

username = input("Enter Instagram username: ")
password = input("Enter Instagram password: ")

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

wait = WebDriverWait(driver, 30)

driver.get("https://www.instagram.com/accounts/login/")
print("Opening login page...")

wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_btn.click()

time.sleep(5)

driver.get("https://www.instagram.com/your_activity/interactions/likes/")
print("✅ Navigated to Likes page")

def unlike_batch(batch_number):
    try:
        select_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Select']"))
        )
        select_btn.click()
        print(f"Batch {batch_number}: Clicked on Select button")
        time.sleep(2)
    except:
        print("Select button not found, continuing...")
        return False

    reel_circles = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@data-bloks-name='ig.components.Icon' and contains(@style, 'circle__outline')]")
        )
    )

    print(f"Batch {batch_number}: Found {len(reel_circles)} reels to select.")

    for i, circle in enumerate(reel_circles, start=1):
        driver.execute_script("arguments[0].click();", circle)
        if i % 10 == 0:
            print(f"Batch {batch_number}: Selected reel #{i}")
        time.sleep(0.1) 

    try:
        unlike_selectors = [
            (By.XPATH, "//span[contains(text(), 'Unlike')]"),
            (By.CSS_SELECTOR, '[aria-label="Unlike"]'),
            (By.XPATH, "//div[contains(@style, 'cursor: pointer')]//span[contains(text(), 'Unlike')]")
        ]
        
        unlike_button = None
        for selector in unlike_selectors:
            try:
                unlike_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(selector))
                break
            except:
                continue
        
        if unlike_button:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", unlike_button)
            time.sleep(1)
            
            driver.execute_script("arguments[0].click();", unlike_button)
            print(f"Batch {batch_number}: Unlike button clicked successfully!")
        else:
            print(f"Batch {batch_number}: Could not find Unlike button with any selector")
            return False
            
    except Exception as e:
        print(f"Batch {batch_number}: Error clicking Unlike button: {str(e)}")
        return False

    try:
        confirm_unlike_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Unlike']]"))
        )
        
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_unlike_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", confirm_unlike_btn)
        print(f"✅ Batch {batch_number}: Confirmed Unlike on popup")
        time.sleep(3)
        
        return True
        
    except Exception as e:
        print(f"Batch {batch_number}: Error confirming unlike: {str(e)}")
        return False

total_to_unlike = 5000
batch_size = 45
batch_count = 1

while total_to_unlike > 0:
    print(f"\n🔄 Processing batch #{batch_count}...")
    
    success = unlike_batch(batch_count)
    
    if not success:
        print("❌ Failed to process batch, stopping...")
        break
    
    processed_in_batch = min(batch_size, total_to_unlike)
    total_to_unlike -= processed_in_batch
    
    print(f"Remaining reels to unlike: {total_to_unlike}")
    
    if total_to_unlike > 0:
        print("🔄 Reloading page to get next batch...")
        driver.get("https://www.instagram.com/your_activity/interactions/likes/")
        time.sleep(5)
    
    batch_count += 1

print("All batches processed successfully!" if total_to_unlike == 0 else " Process incomplete")

time.sleep(10)
driver.quit()