from flask import request
from flask_restx import Resource

from util.dto import ProductDto
from product_service import save_new_product, update_product, save_image_to_product, get_product
from typing import Dict, Tuple

api = ProductDto.api
_product = ProductDto.product

@api.route('/')
class Product(Resource):
    def post(self):
        data = request.json
        return save_new_product(data=data)

    def put(self):
        data = request.json
        return update_product(data=data)    

@api.route('/<product_id>')
class VariantDetail(Resource):
    def get(self, product_id):
        return get_product(product_id)

@api.route('/image/<product_id>')
@api.param('variant_id', 'The variant identifier')
class VariantImageController(Resource):
    def post(self, product_id):
        data = request.json
        data['product_id'] = product_id        
        return save_image_to_product(data=data)
    