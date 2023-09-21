from selenium.webdriver.common.by import By
from selenium import webdriver
import time

INSTAGRAM_PASSWORD = "nlaoasdojd12@3"
INSTAGRAM_USERNAME = "karoltest90312"

URL = "https://www.instagram.com/accounts/login/"



class InstaFollower:
    def __init__(self, account_to_follow, page):
        self.driver = self.create_driver()
        self.account = account_to_follow
        self.page = page

    def create_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def login(self):
        driver = self.driver
        driver.get(url=URL)

        time.sleep(1)
        cookies = driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        cookies.click()

        time.sleep(2)
        username_click = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div')
        username_click.click()

        time.sleep(2)
        username_field = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(INSTAGRAM_USERNAME)

        time.sleep(2)
        password_click = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div')
        password_click.click()

        time.sleep(2)
        password_field = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(INSTAGRAM_PASSWORD)

        time.sleep(5)
        sign_up_button = driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        sign_up_button.click()

    def find_followers(self):
        # TODO find a way to go to account page while being logged and then find their followers
        pass

    def follow(self):
        pass
