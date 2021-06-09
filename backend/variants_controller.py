from flask import request
from flask_restx import Resource

from util.dto import VariantDto
from variants_service import save_new_variants, update_variants, save_image_to_variant, get_variant
from typing import Dict, Tuple

api = VariantDto.api
_variant = VariantDto.variant

@api.route('/')
class VariantsController(Resource):
    def post(self):
        data = request.json        
        return save_new_variants(data=data)

    def put(self):
        data = request.json
        return update_variants(data=data)


@api.route('/<variant_id>')
class VariantDetail(Resource):
    def get(self, variant_id):
        return get_variant(variant_id)

@api.route('/image/<variant_id>')
@api.param('variant_id', 'The variant identifier')
class VariantImageController(Resource):
    def post(self, variant_id):
        data = request.json
        data['variant_id'] = variant_id
        save_image_to_variant(data=data)
        return None
    