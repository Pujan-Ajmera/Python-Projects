from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ====== User Config ======
USERNAME = "karan280917"
PASSWORD = "Pujan@123"
FIRST_REEL = "DLuzhkqvGi7"
COLLECTION_LINK = f"https://www.instagram.com/{USERNAME}/saved/all-posts/"
WATCH_TIME = 6  # fallback in seconds if duration can't be fetched
TOTAL_REELS = None  # not used anymore, here just to keep variable list same
# =========================

driver = webdriver.Chrome()

try:
    # Step 1: Login
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(6)

    # Step 2: Go to saved collection page
    driver.get(COLLECTION_LINK)
    time.sleep(5)

    # Step 3: Start from the most recent saved reel (logic you want to keep forever)
    first_thumb = driver.find_element(By.XPATH, '(//a[contains(@href, "/p/")])[1]')
    first_thumb.click()
    time.sleep(4)

    # Step 4: Loop until no more reels
    reel_count = 1
    while True:
        print(f"▶ Playing reel {reel_count}")
        reel_count += 1

        # Try to detect video duration
        try:
            video = driver.find_element(By.TAG_NAME, 'video')
            watch_time = float(video.get_attribute("duration"))
            time.sleep(watch_time)
        except:
            print("⚠ Could not detect duration, using fallback WATCH_TIME.")
            time.sleep(WATCH_TIME)

        # Move to next reel
        try:
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.ARROW_RIGHT)
            time.sleep(1)
        except:
            print("⚠ No more reels.")
            break

finally:
    driver.quit()
