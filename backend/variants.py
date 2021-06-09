from .. import db

class Variants(db.Model):
    """ Variants Model for storing user related details """
    __tablename__ = "variants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer)
    name = db.Column(db.String(2000))
    size = db.Column(db.Integer)
    color = db.Column(db.String(100))
    images = db.Column(db.String(2000))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    
