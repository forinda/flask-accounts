from app import app
from flask import Blueprint,render_template,redirect,request,flash
accounts_blueprint = Blueprint(
    'accounts',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/accounts/'
)

@accounts_blueprint.route('/admin/')
def admin():
    return render_template('admin.html')


@accounts_blueprint.route('/register/new/student/')
def register_student():
    return render_template('studentAdmit.html')


@accounts_blueprint.route('/register/new/tacher/')
def register_teacher():
    return render_template('teacherEmploy.html')


@accounts_blueprint.route('/user/login')
def login():
    return render_template('login.html')


@accounts_blueprint.route('/register/user/register/')
def register():
    return render_template('registration.html')

@accounts_blueprint.route('/users/update/user/')
def update_profile():
    return render_template('updateProfile.html')

@accounts_blueprint.route('/users/user/profile/')
def profile():
    return render_template('profile.html')