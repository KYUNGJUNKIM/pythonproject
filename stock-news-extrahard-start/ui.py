import requests
from datetime import datetime, timedelta

today = datetime.now()

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "J9RU2N0BELX1S33W"
}
stock_response = requests.get(url='https://www.alphavantage.co/query', params=stock_parameters)
stock_response.raise_for_status()
data = stock_response.json()

news_parameters = {
    "q": "Tesla Inc",
    "from": today,
    "sortBy": "publishedAt",
    "apiKey": "3f4f6427ee534563a44b0d99e0223b9f"
}
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news = news_response.json()

try:
    if today.hour < 16:
        today = datetime.now() - timedelta(days=1)

    if today.weekday() == 0:
        yesterday = today - timedelta(days=3)
        today = today.strftime("%Y-%m-%d")
        yesterday = yesterday.strftime("%Y-%m-%d")
    elif today.weekday() != 5 or today.weekday() != 6:
        yesterday = today - timedelta(days=1)
        today = today.strftime("%Y-%m-%d")
        yesterday = yesterday.strftime("%Y-%m-%d")

    today_close_value = float(data["Time Series (Daily)"][today]["4. close"])
    yesterday_close_value = float(data["Time Series (Daily)"][yesterday]["4. close"])

    difference = today_close_value - yesterday_close_value

    if difference >= 0:
        actual = round((difference / yesterday_close_value), 4)
        percentage = "{:.2%}".format(actual)
        print("TSLA: 🔺" + percentage)
    else:
        actual = round((difference / yesterday_close_value), 4)
        percentage = "{:.2%}".format(actual)
        print("TSLA: 🔻" + percentage)

    if float(percentage.split("%")[0]) >= 5:
        print("headline: ", news["articles"][0]["title"])
        print("brief: ", news["articles"][0]["description"])

except KeyError:
    print("Stock Market doesn't Open Today.")