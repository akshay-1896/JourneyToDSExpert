# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' # URI--> uniform resource identifier to identify the file as a database
# db = SQLAlchemy(app)

# Define your database models
# class Item(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(length=30), nullable= False, unique=True)
#     price = db.Column(db.Integer(), nullable=False)
#     barcode = db.Column(db.String(length=12), nullable=False, unique=True)
#     description = db.Column(db.String(length=1024), nullable=False, unique=True)
    
#     def __repr__(self):
#         return f'Item {self.name}'
    
# Initialise the database
# with app.app_context():
#     db.create_all()
#     print("Database created successfully!!")
  
# @app.route('/')
# @app.route('/home')
# # def hello_world():
# #     return '<h1>Hello World is now BIGGER!!</h1>'

# def home_page():
#     return render_template('home.html')

# # @app.route('/about/<username>') # <username> --> to receive any string
# # def about_page(username):
# #     return f'<h1>This is an About Page of {username}</h1>'

# @app.route('/market')
# def market_page():
#     # items = [
#     #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#     #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#     #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
#     # ]
    
#     items = Item.query.all()
    
#     # return render_template('market.html', item_name= 'Phone')
#     return render_template('market.html', items_list= items)
