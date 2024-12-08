from flask import Flask,render_template,url_for,request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/') # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/about') # http://127.0.0.1:5000/about
def about():
    return render_template('about.html')

@app.route('/services') # http://127.0.0.1:5000/services
def services():
    return render_template('services.html')

@app.route('/contact') # http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')

# @app.route('/query')
# def query():
#     return render_template('query.html') # http://127.0.0.1:5000/query

@app.route('/user_query', methods=['GET','POST'])
def user_query():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        roll_no = int(request.form['roll_no'])
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        user_data = [name,age,roll_no,email,subject,message]
    
        # database
        conn = sql.connect("userdata.db")
        insert_data_query = """
        insert into user_records values(?,?,?,?,?,?)
        """

        cur = conn.cursor()
        cur.execute(insert_data_query, user_data)
        print("You have successfully inserted your data into table", user_data)
        conn.commit()
        cur.close()
        conn.close()
        
        return "Your data is submitted"

if __name__ == '__main__': 
    app.run(debug=True)










































































































