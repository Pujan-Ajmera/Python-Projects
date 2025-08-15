import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# ========================
# CONFIG
# ========================
USERNAME = ""
PASSWORD = ""
FIRST_REEL = "DLuzhkqvGi7"  # Shortcode of the first reel to play https://www.instagram.com/p/DNAHANozHUf/
COLLECTION_LINK = f"https://www.instagram.com/{USERNAME}/saved/all-posts/"
WATCH_TIME = 6  # Fallback watch time in seconds
TOTAL_REELS = 2  # Number of reels to watch

# ========================
# Setup Chrome
# ========================
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Login
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(6)

    # Step 2: Go to collection page
    driver.get(COLLECTION_LINK)
    time.sleep(5)

    # Step 3: Push first reel URL to history
    reel_url = f"https://www.instagram.com/p/{FIRST_REEL}/"
    driver.execute_script(f"history.pushState(null, '', '{reel_url}');")

    # Step 4: Click first reel
    first_thumb = driver.find_element(By.XPATH, '(//a[contains(@href, "/p/")])[1]')
    first_thumb.click()
    time.sleep(4)

    # Step 5: Loop through reels
    for i in range(TOTAL_REELS):
        print(f"▶ Playing reel {i+1}/{TOTAL_REELS}")

        try:
            # Try to get actual video length
            video_element = driver.find_element(By.TAG_NAME, "video")
            duration = driver.execute_script("return arguments[0].duration", video_element)
            if duration and duration > 0:
                print(f"   ⏳ Reel length: {duration:.2f}s")
                time.sleep(duration)
            else:
                print(f"   ⚠ No duration found, using fallback: {WATCH_TIME}s")
                time.sleep(WATCH_TIME)
        except:
            print(f"   ⚠ Video not found, using fallback: {WATCH_TIME}s")
            time.sleep(WATCH_TIME)

        try:
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.ARROW_RIGHT)
            time.sleep(3)
        except:
            print("⚠ No more reels.")
            break

finally:
    driver.quit()

