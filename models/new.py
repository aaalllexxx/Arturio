from settings import db


class New(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.String(180), nullable=False)
    text = db.Column(db.String(512))
    image_uri = db.Column(db.String(512))
