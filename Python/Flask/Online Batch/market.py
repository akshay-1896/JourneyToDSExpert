from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
# def hello_world():
#     return '<h1>Hello World is now BIGGER!!</h1>'

def home_page():
    return render_template('home.html')

# @app.route('/about/<username>') # <username> --> to receive any string
# def about_page(username):
#     return f'<h1>This is an About Page of {username}</h1>'

@app.route('/market')
def market_page():
    return render_template('market.html')