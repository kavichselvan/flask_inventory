from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '852cbb7ad2de2d36f474737943057604'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rohit:sharma45@localhost/product?unix_socket=/var/run/mysqld/mysqld.sock'
db = SQLAlchemy(app)

from flaskinventory import routes

with app.app_context():
    db.create_all()
    db.session.commit()
