from .. import db

class Image(db.Model):
    """ Image Model for storing user related details """
    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(2000))

