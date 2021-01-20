from app import app, db
from app.models import User
from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    flash,
    url_for
)
from app.auth.forms import LoginForm, RegistrationForm
auth_blueprint = Blueprint(
    'auth',
    __name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/accounts/auth/'
)


@auth_blueprint.route('/admin/')
def admin():
    return render_template('admin.html')


@auth_blueprint.route('/register/new/student/',methods=['GET','POST'])
def register_student():
    return render_template('studentAdmit.html',methods=['GET','POST'])


@auth_blueprint.route('/register/new/tacher/',methods=['GET','POST'])
def register_teacher():
    return render_template('teacherEmploy.html')


@auth_blueprint.route('/user/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data)
        if user is not None and user.check_password(form.password.data):
            ...

    return render_template('login.html', form=form)


@auth_blueprint.route('/register/user/register/',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,middle_name=form.middle_name.data,last_name=form.last_name.data,email=form.username.data,username=form.username.data, gender=form.gender.data)
        user.hash_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully',category='success')
        return redirect(url_for('auth.login'))
        
    return render_template('registration.html',form=form)


@auth_blueprint.route('/users/update/user/',methods=['GET','POST'])
def update_profile():
    return render_template('updateProfile.html')


@auth_blueprint.route('/users/user/profile/')
def profile():
    return render_template('profile.html')
