from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_options = webdriver.ChromeOptions()


class InternetSpeedTwitterBot:

    def __init__(self):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()

        time.sleep(80)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = download_speed
        self.up = upload_speed

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(5)
        login_google = self.driver.find_element(By.ID, ".haAclf div")
        login_google.click()

        time.sleep(5)
        email = self.driver.find_element(By.CLASS_NAME, "whsOnd zHQkBf")
        email.send_keys("jun9894@gmail.com")

        time.sleep(5)
        password = self.driver.find_element(By.CLASS_NAME, "whsOnd zHQkBf")
        password.send_keys("PASSWORD")

        time.sleep(5)
        mention = self.driver.find_element(By.CSS_SELECTOR, ".DraftEditor-editorContainer span")
        mention.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up\n "
                          f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()
