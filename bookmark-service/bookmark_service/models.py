from sqlalchemy import func
from bookmark_service.db import db


class BookmarkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    title = db.Column(db.String(50))
    summary = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, server_default=func.now())
