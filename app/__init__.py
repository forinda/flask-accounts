from flask import Flask
from app.config import DevelopmentConfig,ProductionConfig
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
# login = LoginManager(app)
migrate = Migrate(app,db)

app.config.from_object(DevelopmentConfig)

from app.main.views import home_blueprint as hbp
from app.auth.views import auth_blueprint as abp
from app.inventories.views import inventory_blueprint as ivbp

app.register_blueprint(hbp)
app.register_blueprint(abp)
app.register_blueprint(ivbp)

