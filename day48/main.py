from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
current_year = datetime.now().year

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
dates = [f"{current_year}-{time.text}"for time in event_times]
event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
names = [f"{name.text}" for name in event_names]
events = {}

for n in range(len(names)):
    events[n] = {
        "time": dates[n],
        "names": names[n]
    }
print(events)



