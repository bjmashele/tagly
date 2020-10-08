from sqlalchemy import func
from bookmark_service.db import db


tags = db.Table('tags',
       db.Column('bookmark_id', db.Integer, db.ForeignKey('bookmark.id'),primary_key=True),
       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'),primary_key=True)
)
       
class BookmarkModel(db.Model):
    __tablename__ = 'bookmark'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(150))
    title = db.Column(db.String(50))
    summary = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, server_default=func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey('user_model.id'))
    tags = db.relationship(
        'TagModel',
        secondary= tags,
        backref=db.backref('bookmarks')
    )

class TagModel(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(25))
    

class UserModel(db.Model):
    __tablename__ = 'user_model'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    pword = db.Column(db.String(25)) # TODO: hash and salt password before saving to DB
    creation = db.Column(db.DateTime, server_default=func.now())
    bookmarks = db.relationship('BookmarkModel', backref='user_model', lazy=True)