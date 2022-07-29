import os

from flask_sqlalchemy import SQLAlchemy

DEBUG = True

SQLAlchemy_DATABASE_URI = 'postgresql://postgres:cryout35P@127.0.0.1/postgres'
SQLAlchemy_TRACK_MODIFICATIONS = False
SQLAlchemy_ECHO = False