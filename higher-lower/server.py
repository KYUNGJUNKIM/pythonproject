from flask import Flask
import random
app = Flask(__name__)

RANDOM_NUMBER = random.randint(0, 9)

@app.route('/')
def main_page():
    return '<h1>Guess A Number Between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif", width=400, height=400>'


@app.route('/<int:guess>')
def guessing(guess):
    if guess < RANDOM_NUMBER:
        return f'<h1 style="color: red">Too Low, Try Again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif", width=400, height=400 >'
    elif guess > RANDOM_NUMBER:
        return f'<h1 style="color: purple">Too High, Try Again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=400, height=400 >'
    else:
        return f'<h1 style="color: green">You Found ME!</h1> ' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif", width=400, height=400 >'



if __name__ == "__main__":
    app.run(debug=True)

