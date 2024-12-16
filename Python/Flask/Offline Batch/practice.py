from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        # data = request.form.values()
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user_login_data = {
            "name": name,
            "email": email,
            "password": password
        }

    # user_data= [name,email,password]
    user_data_list = [{'name': 'Radhey', 'email': 'ranjit.upflairs@gmail.com',  'password': "258"}, {'name': 'Anshika', 'email': 'anshika.upflairs@gmail.com', 'password': "786"}, {'name': 'Akshay', 'email': 'akshay.upflairs@gmail.com',  'password': "343"}, {'name': 'Lakshay', 'email': 'lakshay.upflairs@gmail.com',  'password': "927"}]

    for i in range(len(user_data_list)):
        status = " "
        if user_login_data['name'] == user_data_list[i]['name'] and user_login_data['email'] == user_data_list[i]['email'] and user_login_data['password'] == user_data_list[i]['password']:
            status = "matched"
            user_name = user_login_data['name']
            break
        else:
            status = "unmatched"
            
    if status == 'matched':
        return redirect(url_for('user_profile', name= user_name))
    elif status == 'unmatched':
        return "Credentials do not match!!"
    
    # return user_login_data


@app.route('/user_profile/<name>')
def user_profile(name):
   return render_template('welcome.html', name=name)
            
            
if __name__ == "__main__":
    app.run(debug=True)
