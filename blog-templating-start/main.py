from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    time = datetime.now().year
    posts = requests.get("https://api.npoint.io/8e9188aa541d0225be9b").json()

    return render_template("index.html", time=time, posts=posts)


@app.route('/blog/<int:num>')
def get_blog(num):
    time = datetime.now().year
    posts = requests.get("https://api.npoint.io/8e9188aa541d0225be9b").json()

    content = None
    for post in posts:
        if post["id"] == num:
            content = post

    return render_template('post.html', time=time, content=content)


if __name__ == "__main__":
    app.run(debug=True)

