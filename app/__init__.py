from flask import Flask
from app.config import DevelopmentConfig


app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

from app.main.views import home_blueprint as hbp
from app.accounts.views import accounts_blueprint as acbp
from app.inventories.views import inventory_blueprint as ivbp

app.register_blueprint(hbp)
app.register_blueprint(acbp)
app.register_blueprint(ivbp)

