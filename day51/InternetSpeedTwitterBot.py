from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TWITTER_EMAIL = "KComplain28815"
TWITTER_PASSWORD = "u#D6w,/i#U:6-an"
URL = "https://twitter.com"


class InternetSpeedTwitterBot:

    def __init__(self, url, up, down):
        self.driver = self.create_driver()
        self.url = url
        self.up = up
        self.down = down
        self.test_up = 0
        self.test_down = 0

    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def get_internet_speed(self):
        driver = self.driver
        driver.get(url=self.url)
        ok_cookies = driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p')

        ok_cookies.click()
        time.sleep(5)
        start_button = driver.find_element(By.XPATH, value='//*[@id="tester"]/div[1]/div/div/div/div[1]')
        start_button.click()
        time.sleep(60)

        get = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/span').text
        get_value = float(get)
        self.test_up = get_value
        print(get_value)
        send = driver.find_element(By.XPATH, value='/html/body/div[1]/main/div/div[2]/div[2]/div[1]/div/div[3]/div[4]/div/span').text
        send_value = float(send)
        self.test_down = send_value
        print(send_value)

    def tweet_at_provider(self):
        driver = self.driver
        tweet_text = f"Hey Internet Provider, why is my internet speed {self.test_up}down/{self.test_down}up when i pay for 100down/30up?"
        # if self.test_up < self.up and self.test_down < self.down:
        driver.get(URL)

        cookies = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]')
        cookies.click()
        time.sleep(2)

        sign_up = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        sign_up.click()
        time.sleep(2)
        # user_name_click = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[1]/div')
        # user_name_click.click()
        time.sleep(2)
        username = driver.find_element(By.TAG_NAME, value='input')
        username.click()
        time.sleep(2)
        username.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        next_window = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_window.click()
        time.sleep(2)

        password = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        time.sleep(2)

        password.send_keys(TWITTER_PASSWORD)

        time.sleep(2)
        sign_up = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        sign_up.click()

        # close = driver.find_element()

        time.sleep(10)
        tweet = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        time.sleep(2)
        text = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/div/span')
        time.sleep(2)
        text.send_keys(tweet_text)
        time.sleep(2)
        post = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        post.click()



