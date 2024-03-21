from cerebro.src.models.models import database
from cerebro.src import app

with app.app_context():
    database.create_all()
