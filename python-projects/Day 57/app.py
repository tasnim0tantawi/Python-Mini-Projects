from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=year)


@app.route('/guess/<name>')
def guess_number(name):
    genderize = "https://api.genderize.io?name="+name
    response = requests.get(genderize)
    gender = response.json()["gender"]
    name = name.replace("_", " ")
    name = name.title()
    return render_template('guess.html', name=name, gender=gender)


@app.route('/blog')
def get_blog():
    blog = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

