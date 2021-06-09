import datetime
from flask import jsonify, make_response

from models import Products, Image, db
from typing import Dict, Tuple


def save_new_product(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    product = Products.query.filter_by(name=data['name']).first()
    if not product:
        new_product = Products(
            name = data['name'],
            description = data['description'],
            logo_id = data['logo_id'],
            created_at = datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow()
        )
        save_changes(new_product)
        return {"message" : "OK"}, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Product already exists',
        }
        return response_object, 409


def update_product(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    product = Products.query.filter_by(id=data['id']).first()
    if not product:
        response_object = {
            'status': 'fail',
            'message': 'Product is not exist',
        }
        return response_object, 404
    product.name = data['name']
    product.description = data['description']
    product.logo_id = data['logo_id']
    product.updated_at = datetime.datetime.utcnow()
    db.session.commit()

    product = Products.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'success',
        'data': {
            'name': product.name,
            'description': product.description,
            'images': product.images,
            'logo_id': product.logo_id,
            'created_at': product.created_at.__str__(),
            'updated_at': product.updated_at.__str__(),
        }
    }
    return response_object, 200

def save_image_to_product(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    product = Products.query.filter_by(id=data['product_id']).first()
    image = Image.query.filter_by(id=data['image_id']).first()
    if not product or not image:
        response_object = {
            'status': 'fail',
            'message': 'Variant or Image does not exists',
        }
        return response_object, 404
    image.image_by_product.append(product)
    db.session.commit()
    return {"message" : "OK"}, 201

def get_product(product_id):
    product = Products.query.filter_by(id=product_id).first()
    if not product:
        response_object = {
            'status': 'fail',
            'message': 'Product does not exists',
        }
        return response_object, 404
    
    image_list = []
    for image in product.images:
        image_list.append({"id" : image.id, "url" : image.url})

    response_object = {
        'status': 'success',
        'data': {
            'name': product.name,
            'description': product.description,
            'logo_id': product.logo_id,
            'image': image_list,
            'created_at': product.created_at.__str__(),
            'updated_at': product.updated_at.__str__(),
        }
    }
    return response_object


def save_changes(data: Products) -> None:
    db.session.add(data)
    db.session.commit()


