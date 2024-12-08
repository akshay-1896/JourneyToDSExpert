from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/about') # http://127.0.0.1:5000/about
def about():
    job_designation = "Data Scientist"
    return render_template('about.html')

@app.route('/services') # http://127.0.0.1:5000/services
def services():
    return render_template('services.html')

def services():
    message = """
    <html>
    <head>
    <body>
    <h1> Hey this is the Service Page</h1>
    
    """

@app.route('/contact') # http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')






















