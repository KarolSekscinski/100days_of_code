from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys("Karol")

last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys("Karol1")

email = driver.find_element(By.NAME, value='email')
email.send_keys("karol@gmail.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")

sign_up_button.click()



#
# num_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# # num_articles.click()
# search_icon = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]').click()
#
#
# wikipedia = driver.find_element(By.NAME, value="search")
# wikipedia.send_keys("Python")
#
#
# python_site = driver.find_element(By.XPATH, value='//*[@id="cdx-menu-item-1"]/a').click()
