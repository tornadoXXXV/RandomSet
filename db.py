from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)

def init_db(app):
    db.init_app(app)
    Migrate(app,db)