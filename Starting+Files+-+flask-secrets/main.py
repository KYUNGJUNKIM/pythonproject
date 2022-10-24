from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

# class PhotoForm(FlaskForm):
#     photo = FileField(validators=[FileRequired()])
#
#
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     form = PhotoForm()
#
#     if form.validate_on_submit():
#         f = form.photo.data
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(
#             app.instance_path, 'photos', filename
#         ))
#         return redirect(url_for('index'))
#
#     return render_template('upload.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)