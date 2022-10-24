import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())

# titles = soup.find_all(name="div", class_="entity-info-items__list")
#
# movie = []
# for title in titles:
#     for i in range(100):
#         title = title.find_next(name="a")
#         movie.append(f"Title: {title.getText()}, url: {title.get('href')}")
# # print(movie[::-1])
#
#
# with open("movie.txt", "w") as file:
#     for i in range(len(movie)):
#         file.write(f"{(i+1)}) {movie[::-1][i]}\n")

all_movies = soup.find_all(name="h3", class_="title")
movies = [movie.getText() for movie in all_movies]

with open("movie_solution.txt", "w") as file:
    for i in range(len(movies)):
        file.write(f"{movies[::-1][i]}\n")