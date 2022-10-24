import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Sceptre-E248W-19203R-Monitor-Speakers-Metallic/dp/B0773ZY26F/ref=sr_1_5?qid=1664707122&s=electronics&sr=1-5&th=1"

headers = {
        'Accept-Language': "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }

response = requests.get(url=URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen").getText()
price = float(price.split("$")[1])

title = soup.find(name="title").getText().split(':')[1]

target_price = 123.0
if price < target_price:
    message = f"{title} is now ${price}"
    # with smtplib.SMTP("START_ADDRS") as smtp:
    #     smtp.starttls()
    #     smtp.login(user="user", password="password")
    #     smtp.sendmail(from_addr="from_addr",
    #                   to_addrs="to_addrs",
    #                   msg=f"Subject: Price Alert\n\n Price has down. Go to {URL}.")


