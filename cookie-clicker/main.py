from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get("https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/dp/B0773ZY26F/ref=sr_1_5?qid=1664707122&s=electronics&sr=1-5&th=1")
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(price_whole.text + "." + price_fraction.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.tag_name)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# submit_bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_bug_link.text)

upcomings = {}

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")
# for event in events:
    # print(event.text)

times = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul time")
# for time in times:
    # print(time.get_attribute("datetime").split('T')[0])

for i in range(len(events)):
    upcomings[i] = {'time': times[i].get_attribute("datetime").split('T')[0],
                    'event': events[i].text}

print(upcomings)





driver.close()

