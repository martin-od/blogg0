from flask import Flask, render_template
import requests
import os


app = Flask(__name__)

@app.route('/')
def home():
    URL = os.environ.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
    response = requests.get(URL)
    data = response.json()
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog_1')
def cactus():
    URL = os.environ.get("https://api.npoint.io/eb6cd8a5d783f501ee7d")
    response = requests.get(URL)
    data = response.json()
    ID = 1
    return render_template('post.html', ID=ID, data=data)

@app.route('/blog_2')
def boring():
    URL = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(URL)
    data = response.json()
    ID = 2
    return render_template('post.html', ID=ID, data=data)

@app.route('/blog_2')
def fasting():
    URL = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(URL)
    data = response.json()
    ID = 3
    return render_template('post.html', ID=ID, data=data)

if __name__=="__main__":
    app.run(debug=False)