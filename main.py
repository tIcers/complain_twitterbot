import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define const speed for up and down internet speed
PROMISED_DOWN = 40
PROMISED_UP = 50
CHROME_DRIVER_PATH = "/Users/atsuki/Downloads/chromedriver"
TWITTER_EMAIL = "###"   #hashing password, email and username
TWITTER_PASSWORD = "####"
USER_NAME= "####"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        s = Service(driver_path)
        self.browser = webdriver.Chrome(service=s)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.browser.get(url)
        self.browser.find_element(by=By.CLASS_NAME, value="start-button").click()
        time.sleep(50)
        self.up = (WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                           '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))).text)
        self.down = (WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                           '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'))).text)

    def tweet_at_provider(self):
        url = 'https://twitter.com/?lang=en'
        self.browser.get(url)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a"))).click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, "text"))).send_keys(TWITTER_EMAIL)
        self.browser.find_element(by=By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()

        # # user name in case for sus login page
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, "text"))).send_keys(USER_NAME)
        # self.browser.find_element(by=By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div").click()


        #password page
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(TWITTER_PASSWORD)
        self.browser.find_element(by=By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div").click()

        #after login in twtter
        tweet = f"Hey internet provider, why my internet speed is {self.up}mph and {self.down}mph when i pay for {PROMISED_UP}mph and {PROMISED_DOWN}mph?"
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div"))).send_keys(tweet)
        self.browser.find_element(by=By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]").click()
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
