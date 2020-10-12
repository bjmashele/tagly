from api.utils.database import _db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Link(db.Model):
    __tablemane__= 'links'
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    url_string = db.Column(db.String(100))
    summary = db.Column(db.String(150))
    user_id = db.Column(db.Interger, db.ForeignKey('users.id'))

    def __init__(self, title, url_string, user_id, summary=None):
        self.title = title
        self.url_string = url_string
        self.summary = summary
        self.user_id = user_id
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
class LinkSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model=Link
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    title= fields.String(required=True)
    summary=fields.String()
    user_id = fields.Integer(required=True)