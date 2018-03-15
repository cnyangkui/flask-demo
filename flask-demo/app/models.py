# -*- encoding: utf-8 -*-
from app import db

class User(db.Model):
    __tablename__ = 'User'
    username = db.Column(db.String(45), primary_key=True)
    pwd = db.Column(db.String(45))

    def __repr__(self):
        return '<User %r>' % self.username