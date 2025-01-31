from flask import Flask, render_template, session, url_for,request, json, jsonify
from collections import OrderedDict
import mysql.connector as mc

conn = mc.connect(host="localhost", username="root", password=r"@b2h8a1r18a1t20", database="flaskapp")

query = "INSERT INTO user_query (name, age, roll_no, email, subject, message) VALUES (%s, %s, %s, %s, %s, %s)"

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
        
        contact_detail =(name, age, roll_no, email, subject, message)
        try:
            my_curs = conn.cursor() # cursor object is used to interact with the database
            my_curs.execute(query) # my_curs.execute is used to execute the query
            conn.commit() # commit is used to save the changes
            print("Data Inserted")
        except Exception as e:
            print("Unable to insert data: ", e)
            conn.rollback() # rollback is used to revert the changes
            
        my_curs.close()
        conn.close()
        return "Data Inserted Successfully"

if __name__ == '__main__':
    app.run(debug=True)





















