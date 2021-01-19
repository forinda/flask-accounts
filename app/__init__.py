from flask import Flask
from app.config import DevelopmentConfig


app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

from app.main import views
