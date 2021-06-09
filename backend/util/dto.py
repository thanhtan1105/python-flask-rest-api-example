from flask_restx import Namespace, fields


class ProductDto:
    api = Namespace('product', description='product')
    product = api.model('product', {
        'name': fields.String(required=True, description='product name'),
        'description': fields.String(required=True, description='product description'),
        'logo_id': fields.String(required=True, description='logo id'),
        'created_at': fields.DateTime(required=True, description='created_at'),
        'updated_at': fields.DateTime(required=True, description='updated_at'),
    })

class VariantDto:
    api = Namespace('variant', description='variant')
    variant = api.model('product', {
        'id': fields.String(required=False),
        'product_id': fields.String(required=True),
        'name': fields.String(required=True),
        'size': fields.Integer(required=False),
        'color': fields.String(required=False),
        'created_at': fields.DateTime(required=True),
        'updated_at': fields.DateTime(required=True),
    })

class ImageDto:
    api = Namespace('image', description='image')
    variant = api.model('product', {
        'id': fields.String(required=False),
        'url': fields.String(required=True),
    })
    