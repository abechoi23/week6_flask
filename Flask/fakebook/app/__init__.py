from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# import routes at bottom of the page
from app import routes 

