from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# nothing but the secret key to encrypt the cookies
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abb9614f40e5f6521adb623714cdfc9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'

from blog import routes