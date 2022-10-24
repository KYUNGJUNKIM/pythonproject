from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)




@app.route('/')
def home():
    return '<h1 style="text-align: center"><b>Want to guess an age with specific person?</b></h1>'


@app.route('/guess/<name>')
def login_home(name):
    time = datetime.now().year

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_data = gender_response.json()
    age_data = age_response.json()

    gender = gender_data["gender"]
    probability = gender_data["probability"]
    age = age_data["age"]

    return render_template('index.html', name=name, time=time, gender=gender, probability=probability, age=age)


@app.route('/blog')
def blog_post():
    time = datetime.now().year

    blog_response = requests.get("https://api.npoint.io/8e9188aa541d0225be9b")
    posts = blog_response.json()

    return render_template('blog.html', posts=posts, time=time)

if __name__ == "__main__":
    app.run(debug=True)

