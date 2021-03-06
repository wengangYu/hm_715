from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ =True
    id = db.Column(db.Integer,primary_key=True)
    sign = db.Column(db.Integer,default=1)  #设置flag 标记方便后面是否删除

    def setattr(self,f):
        for k,v in f.items():
            if hasattr(self,k) and k != 'id':
                setattr(self,k,v)

    def __getitem__(self, item):    #判断对象是否有v值,如果有则返回字典的v
        if hasattr(self,item):
            return getattr(self,item)
from .users import Users
from .seller_model import ShopInfo