from flask import Flask, render_template, redirect, url_for, request, flash
import ast
import mysql.connector as mc

# __name__ is a special variable in python which is used to store the name of the module
app = Flask(__name__)
app.secret_key = "dkfd4343"  # secret key is used to secure the session data

try:
    conn = mc.connect(
        host="localhost",
        username="root",
        password=r"@b2h8a1r18a1t20",
        database="flaskapp"
    )  # connect to the database
    print(f"Database connection established", {"success"})
except mc.Error as err:
    print(f"Database connection failed: {err}", {"danger"})
    print(f"Try reconnecting", {"warning"})
    conn = None

# query to insert the data into the database
query = "INSERT INTO contactdata (name, age, roll_no, email, subject, message) VALUES (%s, %s, %s, %s, %s, %s)"


@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')


@app.route('/about')  # http://127.0.0.1:5000/about
def about():
    # job_designation = "Data Scientist"
    # session['job_designation'] = "Data Scientist"
    return render_template('about.html')


@app.route('/services')  # http://127.0.0.1:5000/services
def services():
    return render_template('services.html')


@app.route('/contact')  # http://127.0.0.1:5000/contact
def contact():
    # print(session['job_designation'])
    return render_template('contact.html')


@app.route('/user_query', methods=['GET', 'POST'])
def user_query():
    if request.method == 'POST':
        # data = request.form.values()
        name = request.form['name']
        age = int(request.form['age'])
        roll_no = int(request.form['roll_no'])
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        contact_detail = (name, age, roll_no, email, subject, message)
        try:
            my_curs = conn.cursor()  # cursor object is used to interact with the database
            # my_curs.execute is used to execute the query
            my_curs.execute(query, contact_detail)
            conn.commit()  # commit is used to save the changes
            flash("Data inserted successfully", "success")
        except Exception as e:
            flash(f"Data insertion failed: {e}", "danger")
            conn.rollback()  # rollback is used to revert the changes

        my_curs.close()
        return redirect(url_for('contact'))


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    user_login_data = {}
    my_curs = None
    if request.method == 'POST':
        # data = request.form.values()
        name = request.form['name']
        email = request.form['email']
        password = int(request.form['password'])
        
        user_login_data = {
            "name": name,
            "email": email,
            "password": password
        }
        
        try:
            my_curs = conn.cursor()
            my_curs.execute("SELECT * FROM contactdata")
            user_data_list = my_curs.fetchall() # fetchall is used to fetch all the data from the table
        except Exception as e:
            flash(f"Data fetching failed: {e}", "danger")
        finally:
            if my_curs is not None:
                my_curs.close()

        for user_tuple in user_data_list:
            if (user_login_data['name'] == user_tuple[0] and
                user_login_data['email'] == user_tuple[3] and
                user_login_data['password'] == user_tuple[2]):
                user_name = user_login_data['name']
                return redirect(url_for('user_profile', name=name))
        else:
            flash(f"User Credentials do not match", "danger")
            return redirect(url_for('login'))

    # return user_login_data


@app.route('/user_profile/<name>')
def user_profile(name):
    return render_template('welcome.html', name=name)

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

@app.route('/dashboard_data')
def dashboard_data():
    my_curs = None # initialising the cursor object with none to avoid unbound local error
    # table_data = []
    try:
        my_curs = conn.cursor(dictionary=True) # dictionary=True is used to fetch the data in the form of dictionary
        my_curs.execute("SELECT * FROM contactdata")
        table_data = my_curs.fetchall()
        print(f"Fetched data")
    except Exception as e:
        flash(f"Data fetching failed: {e}", "danger")
        print(f"Error: {e}")
    finally:
        if my_curs is not None:
            my_curs.close()
        
    return render_template('dashboard.html',data=table_data)

if __name__ == "__main__":
    app.run(debug=True)
