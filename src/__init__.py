from flask import Flask
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor

app = Flask(__name__)


# app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['CKEDITOR_PKG_TYPE'] = 'full'
app.config['SECRET_KEY'] = '8d128903f0d3bcec0f4866d4444951f02b1f22c891dafe2f'

# database = SQLAlchemy(app)
ckeditor = CKEditor(app)
bcrypt = Bcrypt(app)

from cerebro.src.routes import routes
