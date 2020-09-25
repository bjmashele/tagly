from sqlalchemy import func
from bookmark_service.db import db


class BookmarkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    url = db.Column(db.String(150))
    title = db.Column(db.String(50))
    summary = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, server_default=func.now())

class TagModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    name= db.Column(db.String(25))

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(25)) # TODO: hash and salt password before saving to DB
    creation = db.Column(db.DateTime, server_default=func.now())