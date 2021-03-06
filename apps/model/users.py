from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .base import db, Base
class Users(UserMixin, Base):
    __tablename__ = 'users'
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column('password',db.String(128))
    @property
    def password(self):
        # raise AttributeError('password is not a readable attribute')
        return self.password_hash
    @password.setter      # 设置password属性的值时，赋值函数会调用generate_password_hash函数
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    #下面这个是解密
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return '<Users -{}>'.format(self.username)
