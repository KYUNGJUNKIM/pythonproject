from flask import Flask, render_template, request
import requests
import smtplib

blog_data = requests.get("https://api.npoint.io/34d38c483b94d0ac81e9").json()
# for blog in blog_data:
#     print(blog["title"])

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html', blog_data=blog_data)


@app.route('/about')
def about():
    return render_template('about.html', blog_data=blog_data)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        #
        # email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login('email', 'password')
        #     connection.sendmail(from_addr='jun9894@gmail.com', to_addrs=email, msg=email_message)
        return render_template('contact.html', h3_entry=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}")
    return render_template('contact.html')


@app.route('/post/<int:num>')
def posting(num):
    filename = "{}.jpg".format(num)
    return render_template('post.html', blog_data=blog_data, num=num, filename=filename)




if __name__ == '__main__':
    app.run(debug=True)
