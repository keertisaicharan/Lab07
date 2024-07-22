from flask import render_template, request, redirect, url_for, flash, Flask
from flask_sqlalchemy import SQLAlchemy
from utils import check_password

app = Flask(__name__,template_folder="")
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)