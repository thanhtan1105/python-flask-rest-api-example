import datetime
from flask import jsonify, make_response

from models import Image, db
from typing import Dict, Tuple

def save_new_image(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    image = Image.query.filter_by(url=data['url']).first()
    if not image:
        new_image = Image(
            url=data['url']
        )
        save_changes(new_image)
        return {"message" : "OK"}, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product already exists',
        }
        return response_object, 409

def save_changes(data: Image) -> None:
    db.session.add(data)
    db.session.commit()


