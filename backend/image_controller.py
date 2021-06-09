from flask import request
from flask_restx import Resource

from util.dto import ImageDto
from image_service import save_new_image
from typing import Dict, Tuple

api = ImageDto.api

@api.route('/')
class ImageController(Resource):
    def post(self):
        data = request.json
        return save_new_image(data=data)
        
