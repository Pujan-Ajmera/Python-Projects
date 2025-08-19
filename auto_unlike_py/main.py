# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Your Instagram credentials USERNAME = "pujanajmera2" PASSWORD = "AjmeraPujan@1816"

# USERNAME = "pujanajmera2"
# PASSWORD = "AjmeraPujan@1816"
# NUM_REELS = 10
# WAIT_SECONDS = 15

# driver = webdriver.Chrome()
# driver.get("https://www.instagram.com/accounts/login/")
# time.sleep(5)
# driver.find_element(By.NAME, "username").send_keys(USERNAME)
# driver.find_element(By.NAME, "password").send_keys(PASSWORD + Keys.RETURN)
# time.sleep(10)
# driver.get("https://www.instagram.com/reels/")
# time.sleep(5)
# driver.find_element(By.XPATH, '//article//a').click()
# time.sleep(5)

# html = driver.find_element(By.TAG_NAME, 'body')
# for _ in range(NUM_REELS):
#     time.sleep(WAIT_SECONDS)
#     html.send_keys(Keys.ARROW_DOWN)

# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "pujanajmera2"
PASSWORD = "AjmeraPujan@1816"
NUM_REELS = 10
WAIT_SECONDS = 15

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys(USERNAME)
driver.find_element(By.NAME, "password").send_keys(PASSWORD)
driver.find_element(By.NAME, "password").submit()
time.sleep(10)

driver.get("https://www.instagram.com/reels/")
time.sleep(5)
driver.find_element(By.XPATH, '//article//a').click()
time.sleep(5)

for _ in range(NUM_REELS):
    time.sleep(WAIT_SECONDS)
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(0.5)
    driver.execute_script("window.scrollBy(0, 500);")

driver.quit()
