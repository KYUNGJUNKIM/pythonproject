from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3266313450&f_AL=true&geoId=105149562&keywords=Python%20Developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&refresh=true")


login = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login.click()

time.sleep(5)

email = driver.find_element(By.ID, "username")
email.send_keys("jun9894@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("Rudwnsl2017*")
password.send_keys(Keys.ENTER)

time.sleep(5)

recruiting = driver.find_elements(By.CLASS_NAME, "job-card-list__insight")
i = 0
for recruit in recruiting:
    recruit.click()
    # save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    # save.click()
    follow = driver.find_element(By.CLASS_NAME, "artdeco-button--secondary")
    follow.click()
    if i > 5:
        break

time.sleep(5000)
driver.close()

