from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

product_image = db.Table('product_image',
        db.Column('product_id', db.Integer, db.ForeignKey('products.id')),
        db.Column('image_id', db.Integer, db.ForeignKey('image.id')),
    )

variant_image = db.Table('variant_image',
        db.Column('variant_id', db.Integer, db.ForeignKey('variants.id')),
        db.Column('image_id', db.Integer, db.ForeignKey('image.id')),
    )

class Products(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(2000))
    logo_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    variants = db.relationship('Variants', backref='owner')
    images = db.relationship('Image', secondary=product_image, backref=db.backref('image_by_product'), lazy='dynamic')

class Variants(db.Model):
    __tablename__ = "variants"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    name = db.Column(db.String(2000))
    size = db.Column(db.Integer)
    color = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    images = db.relationship('Image', secondary=variant_image, backref=db.backref('image_by_variant'), lazy='dynamic')

class Image(db.Model):
    __tablename__ = "image"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(2000))

