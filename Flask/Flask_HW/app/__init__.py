from flask import Flask
from config import Config
# from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_object(config)

from app import routes 