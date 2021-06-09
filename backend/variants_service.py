import datetime
from flask import jsonify, make_response

from models import Variants, Products, Image, db
from typing import Dict, Tuple


def save_new_variants(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    product = Products.query.filter_by(id=data['product_id']).first()
    if not product:
        response_object = {
            'status': 'fail',
            'message': 'Product does not exists',
        }
        return response_object, 404
        
    for variant in data['variants']:
        save_changes(Variants(
            name = variant["name"],
            size = variant["size"],
            color = variant["color"],
            created_at = datetime.datetime.utcnow(),
            updated_at = datetime.datetime.utcnow()
        ))

    return {"message" : "OK"}, 201

def update_variants(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    variant = Variants.query.filter_by(id=data['id']).first()
    if not variant:
        response_object = {
            'status': 'fail',
            'message': 'Variant does not exists',
        }
        return response_object, 404
    
    variant.name = data['name']
    variant.size = data['size']
    variant.color = data['color']
    db.session.commit()

    variant = Variants.query.filter_by(id=data['id']).first()
    response_object = {
        'status': 'success',
        'data': {
            'id': variant.id,
            'name': variant.name,
            'size': variant.size,
            'color': variant.color,
            'created_at': variant.created_at.__str__(),
            'updated_at': variant.updated_at.__str__(),
        }
    }
    return response_object, 200   

def save_image_to_variant(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    variant = Variants.query.filter_by(id=data['variant_id']).first()
    image = Image.query.filter_by(id=data['image_id']).first()
    if not variant or not image:
        response_object = {
            'status': 'fail',
            'message': 'Variant or Image does not exists',
        }
        return response_object, 404

    image.image_by_variant.append(variant)
    db.session.commit()
    return {"message" : "OK"}, 201

def get_variant(variant_id):
    variant = Variants.query.filter_by(id=variant_id).first()
    if not variant:
        response_object = {
            'status': 'fail',
            'message': 'Variant does not exists',
        }
        return response_object, 404
    
    image_list = []
    for image in variant.images:
        image_list.append({"id" : image.id, "url" : image.url})

    response_object = {
        'status': 'success',
        'data': {
            'id': variant.id,
            'name': variant.name,
            'size': variant.size,
            'color': variant.color,
            'image': image_list,
            'created_at': variant.created_at.__str__(),
            'updated_at': variant.updated_at.__str__(),
        }
    }
    return response_object


def save_changes(data: Variants) -> None:
    db.session.add(data)
    db.session.commit()


