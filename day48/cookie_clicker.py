from selenium.webdriver.common.by import By
from selenium import webdriver
import time


URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment",
               "buyMine", "buyFactory", "buyGrandma", "buyCursor"]

cookie = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 60*5
iterations = 1
while time.time() <= timeout:
    for _ in range(iterations):
        cookie.click()

    for upgrade_id in upgrades_id:
        try:
            driver.find_element(By.ID, value=upgrade_id).click()
        except:
            continue
    iterations += 10

cps = driver.find_element(By.ID, value="cps").text
print(cps)

driver.quit()






# driver.quit()