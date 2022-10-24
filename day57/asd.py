import requests

blog_response = requests.get("https://api.npoint.io/8e9188aa541d0225be9b")
posts = blog_response.json()

for post in posts:
    if post["id"] == 1:
        print(post["title"])
        print(post["subtitle"])
        print(post["body"])