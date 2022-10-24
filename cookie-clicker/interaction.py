from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# portal = driver.find_element(By.LINK_TEXT, count.text)
# portal.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

fname.send_keys("KYUNGJUN")
fname.send_keys(Keys.TAB)
lname.send_keys("KIM")
lname.send_keys(Keys.TAB)
email.send_keys("jun9894@snu.ac.kr")

submit = driver.find_element(By.CLASS_NAME, "btn-primary")
submit.click()
time.sleep(5)


