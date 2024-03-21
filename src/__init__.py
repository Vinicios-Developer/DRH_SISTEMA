from flask import Flask
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cerebro.db'
app.config['CKEDITOR_PKG_TYPE'] = 'full'
app.config['SECRET_KEY'] = '8d128903f0d3bcec0f4866d4444951f02b1f22c891dafe2f'

database = SQLAlchemy(app)
ckeditor = CKEditor(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from cerebro.src.routes import routes
