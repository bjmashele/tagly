from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Link(db.Model):
    __tablename__ = 'link'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250))
    url_string = db.Column(db.String(250))
    summary = db.Column(db.String(150))

    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, title, url_string, summary=None):
        self.title = title
        self.url_string = url_string
        self.summary = summary
        # self.user_id = user_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class LinkSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Link
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    title = fields.String(required=True)
    url_string = fields.String(required=True)
    summary = fields.String()
    # user_id = fields.Integer()
