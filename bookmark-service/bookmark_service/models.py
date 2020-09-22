from sqlalchemy import func
from bookmark_service.db import db


class bookmarkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    summary = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, server_default=func.now())
