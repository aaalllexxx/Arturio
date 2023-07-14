from uuid import uuid4

from settings import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(180), primary_key=True, default=uuid4().hex)
    name = db.Column(db.String(180))
    password = db.Column(db.String(180))
    profile_image_uri = db.Column(db.String(180))
    friends = db.Column(db.String(4096), default="[]")
    session_id = db.Column(db.String(180))
