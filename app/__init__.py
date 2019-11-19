from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

obj = Flask(__name__)
obj.config.from_object(Config)
db = SQLAlchemy(obj)

from app import routes, models

if(__name__=='__main__'):
    app.run()
