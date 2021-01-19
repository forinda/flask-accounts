from app import app
from flask import Blueprint,render_template,redirect,request,flash
home_blueprint = Blueprint(
    'home',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/home/'
)

@home_blueprint.route('/')
def index():
    return render_template('index.html')