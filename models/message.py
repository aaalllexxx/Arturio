from uuid import uuid4

from settings import db


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.String(180), primary_key=True, default=uuid4().hex)
    from_id = db.Column(db.String(180))
    text = db.Column(db.String(512))
