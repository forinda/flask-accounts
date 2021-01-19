from app import app
from flask import Blueprint,render_template,redirect,request,flash
inventory_blueprint = Blueprint(
    'inventory',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/inventory/'
)

@inventory_blueprint.route('/')
def account():
    return render_template('resource.html')