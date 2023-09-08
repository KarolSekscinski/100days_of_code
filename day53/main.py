from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# for selenium usage
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd-bCpGPR4SkGhoPegldksdwNDUQKd5j3xTSWL0VSo1c6FGQw/viewform?usp=sf_link"
# for bs4 usage
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.73932632963956%2C%22north%22%3A37.81123909008061%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6"
}

response = requests.get(url=ZILLOW_URL, headers=header)
data = response.text

soup = BeautifulSoup(data, "html.parser")
# LINKS
all_link_elements = soup.find_all("a", attrs={"data-test": "property-card-link"})
all_links = []
for link in all_link_elements:
    href = link["href"]

    if "http" not in href:
        href = f"https://www.zillow.com{href}"
    if href in all_links:
        continue
    all_links.append(href)

# Addresses
all_addresses_elements = soup.find_all("address", attrs={"data-test": "property-card-addr"})
all_addresses = [address.text for address in all_addresses_elements]

# Prices
all_price_elements = soup.find_all("span", attrs={"data-test": "property-card-price"})
all_prices = [price.text for price in all_price_elements]

for n in range(len(all_links)):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(GOOGLE_FORM_URL)
    time.sleep(2)

    address_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link_input = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    time.sleep(1)

    address_input.send_keys(all_addresses[n])

    price_input.send_keys(all_prices[n])

    link_input.send_keys(all_links[n])
    time.sleep(1)
    submit_button.click()

    driver.quit()

