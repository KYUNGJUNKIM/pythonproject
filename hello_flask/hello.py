from flask import Flask
app = Flask(__name__)


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def function_wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return function_wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog.")


user1 = User("KYUNGJUN")
user1.is_logged_in = True
create_blog_post(user1)


def make_bold(function):
    def function_wrapper(*args, **kwargs):
        return f'<b>{function(**kwargs)}</b>'
    return function_wrapper


def make_emphasis(function):
    def function_wrapper(*args, **kwargs):
        return f'<em>{function(**kwargs)}</em>'
    return function_wrapper


def make_underline(function):
    def function_wrapper(*args, **kwargs):
        return f'<u>{function(**kwargs)}</u>'
    return function_wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>Show Yourself</p>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif", width=400, height=400>'


@app.route('/<name>')
@make_underline
@make_emphasis
@make_bold
def greet(name):
    return f'Hello, {name}!'



if __name__ == "__main__":
    app.run(debug=True)

#

