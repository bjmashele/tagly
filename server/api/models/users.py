from api.utils.database import _db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class User(db.Model):
    __tablemane__= 'users'
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    created = db.Column(db.Datetime, server_default=db.func.now())
    links = db.relationship('Link', backref='User', cascade="all, delete-orphan")

    def __init__(self, username, links):
        self.username = username
        self.links = links

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
class UserSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=User
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    username= fields.String(required=True)
    created = fields.String(dump_only=True)
    links = fields.Nested(BookSchema, many=True, only=['title', 'url_string', 'id'])