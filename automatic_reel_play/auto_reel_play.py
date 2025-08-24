from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
USERNAME = input("Enter Instagram username: ")
PASSWORD = input("Enter Instagram password: ")

REELS_URL = "https://www.instagram.com/reels/"
TOTAL_REELS = 5          # ketli play karvi che 
FALLBACK_DURATION = 15   # if cannot fetch the reel time then aa run thase

driver = webdriver.Chrome()

try:
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(6)

    driver.get(REELS_URL)
    time.sleep(5)

    reel_count = 0
    last_url = ""

    while reel_count < TOTAL_REELS:
        try:
            video = driver.find_element(By.TAG_NAME, 'video')
        except:
            time.sleep(2)
            continue

        current_url = driver.current_url
        if current_url == last_url:
            time.sleep(1)
            continue
        last_url = current_url

        reel_count += 1
        print(f"Playing reel {reel_count}: {current_url}")

        try:
            duration = float(video.get_attribute("duration"))
            print(f"Duration detected: {duration} seconds")
            time.sleep(duration-2)
            # ek j reel thodo time vadhare chale che like 1 reel full pachi eej reel ek sec vadhare chale che so -2
        except:
            print(f"Could not detect duration, using fallback {FALLBACK_DURATION}s")
            time.sleep(FALLBACK_DURATION)

        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)

    print("All reels completed.")

finally:
    driver.quit()
