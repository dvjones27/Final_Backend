from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Transportation, transportation_schema, transportations_schema
# Waste, waste_schema, wastes_schema, Water, water_schema, waters_schema, HomeEnergy, homeEnergy_schema, homeEnergys_schema, Recycling, recycling_schema, recyclings_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/emissions', methods = ['POST'])
@token_required
def create_transportation(current_user_token):
    travel = request.json['travel']
    vehicle = request.json['vehicle']
    fuel = request.json['fuel']
    carpool = request.json['carpool']
    miles = request.json['miles']
    user_token = current_user_token.token
    
    
    transportation = Transportation(travel, vehicle, fuel, carpool, miles, user_token = user_token)

    db.session.add(transportation)
    db.session.commit()

    response = transportation_schema.dump(transportation)
    return jsonify(response)



@api.route('/emissions', methods = ['GET'])
@token_required
def get_transportations(current_user_token):
    ride = current_user_token.token
    if ride == current_user_token.token:
        transportation = Transportation.query.get(id)
        response = transportation_schema.dump(transportation)
        return jsonify(response)
    else:
        return jsonify({"Message": "Invalid Token. Please Verify Token."}), 401



@api.route('/emissions', methods = ['GET'])
@token_required
def get_transportation(current_user_token, id):
    ride = current_user_token.token
    transportations = Transportation.query.filter_by(user_token = ride).all()
    response = transportations_schema.dump(transportations)
    return jsonify(response)


@api.route('/emissions/<id>', methods = ['POST','PUT'])
@token_required
def update_transportation(current_user_token, id):
    transportation = Transportation.query.get(id) 
    transportation.travel = request.json['travel']
    transportation.vehicle = request.json['vehicle']
    transportation.fuel = request.json['fuel']
    transportation.carpool = request.json['carpool']
    transportation.miles = request.json['miles']
    transportation.user_token = current_user_token.token

    db.session.commit()
    response = transportation_schema.dump(transportation)
    return jsonify(response)

@api.route('/emissions/<id>', methods = ['DELETE'])
@token_required
def delete_transportation(current_user_token, id):
    transportation = Transportation.query.get(id)
    db.session.delete(transportation)
    db.session.commit()
    response = transportation_schema.dump(transportation)
    return jsonify(response)


# @api.route('/emissions', methods = ['POST'])
# @token_required
# def create_emissions(current_user_token):
#     transportation = request.json['vin']
#     make = request.json['make']
#     model = request.json['model']
#     year = request.json['year']
#     color = request.json['color']
#     user_id = User.query.get(current_user_token.id)
    
    
#     car = Car(vin, make, model, year, color, user_id = user_id)

#     db.session.add(car)
#     db.session.commit()

#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/cars', methods = ['GET'])
# @token_required
# def get_cars(current_user_token):
#     user_id = current_user_token.id
#     cars = Car.query.filter_by(user_id = user_id).all()
#     response = cars_schema.dump(cars)
#     return jsonify(response)


# @api.route('/cars/<id>', methods = ['GET'])
# @token_required
# def get_single_car(current_user_token, id):
#     car_Token = current_user_token.token
#     if car_Token == current_user_token.token:
#         car = Car.query.get(id)
#         response = car_schema.dump(car)
#         return jsonify(response)
#     else:
#         return jsonify({'message': "Invalid Token"}), 401


# @api.route('/cars/<id>', methods = ['POST','PUT'])
# @token_required
# def update_car(current_user_token, id):
#     car = Car.query.get(id) 
#     car.vin = request.json['vin']
#     car.make = request.json['make']
#     car.model = request.json['model']
#     car.year = request.json['year']
#     car.color = request.json['color']
#     car.user_id = current_user_token.id

#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)

# @api.route('/cars/<id>', methods = ['DELETE'])
# @token_required
# def delete_car(current_user_token, id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/emissions', methods = ['POST'])
# @token_required
# def create_emissions(current_user_token):
#     transportation = request.json['vin']
#     make = request.json['make']
#     model = request.json['model']
#     year = request.json['year']
#     color = request.json['color']
#     user_id = User.query.get(current_user_token.id)
    
    
#     car = Car(vin, make, model, year, color, user_id = user_id)

#     db.session.add(car)
#     db.session.commit()

#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/cars', methods = ['GET'])
# @token_required
# def get_cars(current_user_token):
#     user_id = current_user_token.id
#     cars = Car.query.filter_by(user_id = user_id).all()
#     response = cars_schema.dump(cars)
#     return jsonify(response)


# @api.route('/cars/<id>', methods = ['GET'])
# @token_required
# def get_single_car(current_user_token, id):
#     car_Token = current_user_token.token
#     if car_Token == current_user_token.token:
#         car = Car.query.get(id)
#         response = car_schema.dump(car)
#         return jsonify(response)
#     else:
#         return jsonify({'message': "Invalid Token"}), 401


# @api.route('/cars/<id>', methods = ['POST','PUT'])
# @token_required
# def update_car(current_user_token, id):
#     car = Car.query.get(id) 
#     car.vin = request.json['vin']
#     car.make = request.json['make']
#     car.model = request.json['model']
#     car.year = request.json['year']
#     car.color = request.json['color']
#     car.user_id = current_user_token.id

#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)

# @api.route('/cars/<id>', methods = ['DELETE'])
# @token_required
# def delete_car(current_user_token, id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/emissions', methods = ['POST'])
# @token_required
# def create_emissions(current_user_token):
#     transportation = request.json['vin']
#     make = request.json['make']
#     model = request.json['model']
#     year = request.json['year']
#     color = request.json['color']
#     user_id = User.query.get(current_user_token.id)
    
    
#     car = Car(vin, make, model, year, color, user_id = user_id)

#     db.session.add(car)
#     db.session.commit()

#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/cars', methods = ['GET'])
# @token_required
# def get_cars(current_user_token):
#     user_id = current_user_token.id
#     cars = Car.query.filter_by(user_id = user_id).all()
#     response = cars_schema.dump(cars)
#     return jsonify(response)


# @api.route('/cars/<id>', methods = ['GET'])
# @token_required
# def get_single_car(current_user_token, id):
#     car_Token = current_user_token.token
#     if car_Token == current_user_token.token:
#         car = Car.query.get(id)
#         response = car_schema.dump(car)
#         return jsonify(response)
#     else:
#         return jsonify({'message': "Invalid Token"}), 401


# @api.route('/cars/<id>', methods = ['POST','PUT'])
# @token_required
# def update_car(current_user_token, id):
#     car = Car.query.get(id) 
#     car.vin = request.json['vin']
#     car.make = request.json['make']
#     car.model = request.json['model']
#     car.year = request.json['year']
#     car.color = request.json['color']
#     car.user_id = current_user_token.id

#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)

# @api.route('/cars/<id>', methods = ['DELETE'])
# @token_required
# def delete_car(current_user_token, id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/emissions', methods = ['POST'])
# @token_required
# def create_emissions(current_user_token):
#     transportation = request.json['vin']
#     make = request.json['make']
#     model = request.json['model']
#     year = request.json['year']
#     color = request.json['color']
#     user_id = User.query.get(current_user_token.id)
    
    
#     car = Car(vin, make, model, year, color, user_id = user_id)

#     db.session.add(car)
#     db.session.commit()

#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/cars', methods = ['GET'])
# @token_required
# def get_cars(current_user_token):
#     user_id = current_user_token.id
#     cars = Car.query.filter_by(user_id = user_id).all()
#     response = cars_schema.dump(cars)
#     return jsonify(response)


# @api.route('/cars/<id>', methods = ['GET'])
# @token_required
# def get_single_car(current_user_token, id):
#     car_Token = current_user_token.token
#     if car_Token == current_user_token.token:
#         car = Car.query.get(id)
#         response = car_schema.dump(car)
#         return jsonify(response)
#     else:
#         return jsonify({'message': "Invalid Token"}), 401


# @api.route('/cars/<id>', methods = ['POST','PUT'])
# @token_required
# def update_car(current_user_token, id):
#     car = Car.query.get(id) 
#     car.vin = request.json['vin']
#     car.make = request.json['make']
#     car.model = request.json['model']
#     car.year = request.json['year']
#     car.color = request.json['color']
#     car.user_id = current_user_token.id

#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)

# @api.route('/cars/<id>', methods = ['DELETE'])
# @token_required
# def delete_car(current_user_token, id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/emissions', methods = ['POST'])
# @token_required
# def create_emissions(current_user_token):
#     transportation = request.json['vin']
#     make = request.json['make']
#     model = request.json['model']
#     year = request.json['year']
#     color = request.json['color']
#     user_id = User.query.get(current_user_token.id)
    
    
#     car = Car(vin, make, model, year, color, user_id = user_id)

#     db.session.add(car)
#     db.session.commit()

#     response = car_schema.dump(car)
#     return jsonify(response)



# @api.route('/cars', methods = ['GET'])
# @token_required
# def get_cars(current_user_token):
#     user_id = current_user_token.id
#     cars = Car.query.filter_by(user_id = user_id).all()
#     response = cars_schema.dump(cars)
#     return jsonify(response)


# @api.route('/cars/<id>', methods = ['GET'])
# @token_required
# def get_single_car(current_user_token, id):
#     car_Token = current_user_token.token
#     if car_Token == current_user_token.token:
#         car = Car.query.get(id)
#         response = car_schema.dump(car)
#         return jsonify(response)
#     else:
#         return jsonify({'message': "Invalid Token"}), 401


# @api.route('/cars/<id>', methods = ['POST','PUT'])
# @token_required
# def update_car(current_user_token, id):
#     car = Car.query.get(id) 
#     car.vin = request.json['vin']
#     car.make = request.json['make']
#     car.model = request.json['model']
#     car.year = request.json['year']
#     car.color = request.json['color']
#     car.user_id = current_user_token.id

#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)

# @api.route('/cars/<id>', methods = ['DELETE'])
# @token_required
# def delete_car(current_user_token, id):
#     car = Car.query.get(id)
#     db.session.delete(car)
#     db.session.commit()
#     response = car_schema.dump(car)
#     return jsonify(response)



