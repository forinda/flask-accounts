from app import db
from flask import current_app
from datetime import datetime
from app import login_manager
from flask_login import UserMixin,AnonymousUserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), index=True)
    middle_name = db.Column(db.String(100), index=True)
    last_name = db.Column(db.String(100), index=True)
    email = db.Column(db.String(100), index=True, unique=True)
    username = db.Column(db.String(100), index=True, unique=True)
    gender = db.Column(db.String(100), index=True)
    hashed_password = db.Column(db.String(128))
    roles = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.roles is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.roles = Role.query.filter_by(name='Administrator').first()
            if self.roles is None:
                self.roles = Role.query.filter_by(default=True).first()

    def can(self, perm):
        return self.roles is not None and self.role.has_permission(perm)

    def is_administrator(self):
        return self.can(Permission.ADMIN)

    @property
    def password(self):
        return AttributeError("This fiels cannot be viewed")

    def hash_password(self, passw):
        self.hashed_password = generate_password_hash(passw)

    def verify_password(self, passw):
        val = check_password_hash(self.hashed_password,passw)

class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser
    
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permission is None:
            self.permissions = 0

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {
            "User": [
                Permission.FOLLOW,
                Permission.COMMENT
                ],
            "Moderator": [
                Permission.COMMENT,
                Permission.FOLLOW,
                Permission.MODERATE
                ],
            "Administrator": [
                Permission.WRITE,
                Permission.COMMENT,
                Permission.FOLLOW,
                Permission.MODERATE,
                Permission.ADMIN
                ],
        }

        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()


class Permission:
    '''
    None - Read only
    User - Follow, comment, write(Default to write and coment, for default users)
    Moderator - follow,comment,write,moderate(Adds permission to modrate users comments)
    Administrator - follow,comment,write,moderate,admin(Full access and can even change users)
    '''
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id)).first()