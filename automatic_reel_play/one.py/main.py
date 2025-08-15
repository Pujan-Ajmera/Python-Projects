import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

time.sleep(50)
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
FIRST_REEL = "DLuzhkqvGi7"
COLLECTION_LINK = f"https://www.instagram.com/{USERNAME}/saved/all-posts/"
WATCH_TIME = 6
TOTAL_REELS = 15

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Login
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)

    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    time.sleep(6)

    driver.get(COLLECTION_LINK)
    time.sleep(5)

    reel_url = f"https://www.instagram.com/p/{FIRST_REEL}/"
    driver.execute_script(f"history.pushState(null, '', '{reel_url}');")

    first_thumb = driver.find_element(By.XPATH, '(//a[contains(@href, "/p/")])[1]')
    first_thumb.click()
    time.sleep(4)

    for i in range(TOTAL_REELS):
        print(f"▶ Playing reel {i+1}/{TOTAL_REELS}")
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
