from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    
    items = Item.query.all()
    
    return render_template('market.html', items_list= items)

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    
    if form.errors != {}: # if there are no errors from validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
            
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit(): # (1) To validate that all information is valid & (2) If validation is successful, then submits the info on executing submit button
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password do not match! Please try again', category='danger')
    return render_template('login.html', form=form)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    