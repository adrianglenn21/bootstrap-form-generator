from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

db_uri = f"postgresql://{config['database']['username']}:{config['database']['password']}@{config['database']['host']}:{config['database']['port']}/{config['database']['database']}"
app = Flask(__name__)
app.config["SECRET_KEY"] = config['app']['secret_key']
app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
db = SQLAlchemy(app)