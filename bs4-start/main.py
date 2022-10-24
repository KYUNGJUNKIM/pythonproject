from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com")
data = response.text

soup = BeautifulSoup(data, "html.parser")

titles = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")
votes = []
for score in scores:
    votes.append(int(score.getText().split()[0]))

i = 0
news = []
for title in titles:
    news_title = title.find_next(name="a").getText()
    link = title.find_next(name="a").get("href")
    # print(f"{i+1}. news: {news_title}, link: {link}, vote: {votes[i]}")
    news.append((news_title, link, votes[i]))
    i += 1

news.sort(key=lambda x: x[2], reverse=True)
print(news)










# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# # all_anchor = soup.find_all(name="a")
# # for tag in all_anchor:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# department_url = soup.select_one(selector="p a")
# print(department_url.get("href"))
