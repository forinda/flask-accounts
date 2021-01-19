from app import app
from flask import Blueprint,render_template,redirect,request,flash
accounts_blueprint = Blueprint(
    'accounts',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/accounts/'
)

@accounts_blueprint.route('/users/')
def account():
    return render_template('profile.html')