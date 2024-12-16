from flask import Flask, render_template, session, url_for,request, json, jsonify
from collections import OrderedDict

app = Flask(__name__)
app.secret_key = "dkfd4343"

# session = dict() # empty dictionary
# session['name'] = 'radhey'

@app.route('/') # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/about') # http://127.0.0.1:5000/about
def about():
    # job_designation = "Data Scientist"
    # session['job_designation'] = "Data Scientist"
    return render_template('about.html')

@app.route('/services') # http://127.0.0.1:5000/services
def services():
    return render_template('services.html')

# def services():
#     message = """
#     <html>
#     <head>
#     <body>
#     <h1> Hey this is the Service Page</h1>
    
#     """

@app.route('/contact') # http://127.0.0.1:5000/contact
def contact():
    # print(session['job_designation'])
    return render_template('contact.html')

@app.route('/user_query', methods=['GET','POST'])
def user_query():
    if request.method == 'POST':
        # data = request.form.values()
        name = request.form['name']
        age = int(request.form['age'])
        roll_no = int(request.form['roll_no'])
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        user_data = {
            "Name": name, 
            "Age": age, 
            "Roll No": roll_no, 
            "Email": email, 
            "Subject": subject, 
            "Message": message
        }
        # user_data= [name, age, roll_no, email, subject, message]
        return user_data

if __name__ == '__main__':
    app.run(debug=True)





















