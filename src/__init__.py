from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['CKEDITOR_PKG_TYPE'] = 'full'
app.config['SECRET_KEY'] = ''

database = SQLAlchemy(app)
ckeditor = CKEditor(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'
login_manager.login_message_category = 'alert-info'
