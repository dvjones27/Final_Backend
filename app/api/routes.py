from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Transportation, transportation_schema, transportations_schema, HomeEnergy, homeEnergy_schema, homeEnergys_schema, Recycling, recycling_schema, recyclings_schema

# Waste, waste_schema, wastes_schema, Water, water_schema, waters_schema, Recycling, recycling_schema, recyclings_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/emissions', methods = ['GET'  ,'POST'])
@token_required
def emissions(current_user_token):
    transportations = Transportation.query.all()
    homeEnergys = HomeEnergy.query.all()
    recyclings = Recycling.query.all()
    waters = Water.query.all()
    wastes = Waste.query.all()
    
    
    transportation = Transportation(travel, vehicle, fuel, carpool, miles, user_token = user_token)

    homeEnergy = HomeEnergy(dishwasher, dishwasherLoads, washer, washerLoads, dryer, dryerLoads, lights, lightsNumber, lightsTime, hvac, hvacTime, hvacTemp, user_token = user_token)

    recycling = Recycling(paper, paperAmount, glass, glassAmount, plastic, plasticAmount, user_token=user_token)

    
    db.session.add(transportation, homeEnergy, recycling)
    db.session.commit()

    
    
    response = waters_schema.dump(waters), recyclings_schema.dump(recyclings), homeEnergys_schema.dump(homeEnergys), transportations_schema.dump(transportations), waters_schema.dump(waters)
    
    return jsonify(response)


@api.route('/transportation', methods = ['POST'])
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

@api.route('/homeEnergy', methods = ['POST'])
@token_required
def create_homeEnergy(current_user_token):
    dishwasher = request.json['dishwasher']
    dishwasherLoads = request.json['dishwasherLoads']
    washer = request.json['washer']
    washerLoads = request.json['washerLoads']
    dryer = request.json['dryer']
    dryerLoads = request.json['dryerLoads']
    lights = request.json['lights']
    lightsNumber = request.json['lightsNumber']
    lightsTime = request.json['lightsTime']
    hvac = request.json['hvac']
    hvacTime = request.json['hvacTime']
    hvacTemp= request.json['hvacTemp']
    user_token = current_user.token
    
    homeEnergy = HomeEnergy(dishwasher = dishwasher, dishwasherLoads = dishwasherLoads, washer = washer, washerLoads = washerLoads, dryer = dryer, dryerLoads = dryerLoads, lights = lights,  lightsNumber = lightsNumber ,lightsTime = lightsTime, hvac = hvac, hvacTime = hvacTime, hvacTemp = hvacTemp, user_token = user_token )

    db.session.add(homeEnergy)
    db.session.commit()

    response = homeEnergy_schema.dump(homeEnergy)
    return jsonify(response)

@api.route('/recycling', methods = ['POST'])
@token_required
def create_recycling(current_user_token):
    paper = request.json['paper']
    paperAmount = request.json['paperAmoung']
    glass = request.json['glass']
    glassAmount = request.json['glassAmount']
    plastic = request.json['plastic']
    plasticAmount = request.json['plasticAmount']
    user_token = current_user.token
    
    
    recycling = Recycling(paper=paper, paperAmount=paperAmount, glass=glass, glassAmount=glassAmount, plastic=plastic, plasticAmount=plasticAmount,   user_token=user_token)

    db.session.add(recycling)
    db.session.commit()
    
    response = recycling_schema.dump(recycling)
    return jsonify(response)


@api.route('/transportation', methods = ['GET'])
@token_required
def get_transportations(current_user_token, id):
    user_token = current_user_token.token
    transportations = Transportation.query.filter_by(user_token = user_token).all()
    response = transportations_schema.dump(transportations)
    return jsonify(response)

@api.route('/homeEnergy', methods = ['GET'])
@token_required
def get_homeEnergys(current_user_token, id):
    user_token = current_user_token.token
    homeEnergys = HomeEnergy.query.filter_by(user_token = user_token).all()
    response = homeEnergys_schema.dump(homeEnergys)
    return jsonify(response)

@api.route('/recycling', methods = ['GET'])
@token_required
def get_recycling(current_user_token, id):
    user_token = current_user_token.token
    recyclings = Recycling.query.filter_by(user_token = user_token).all()
    response = recyclings_schema.dump(recyclings)
    return jsonify(response)

@api.route('/transportation', methods = ['GET'])
@token_required
def get_transportation(current_user_token):
    transport = current_user_token.token
    if transport == current_user_token.token:
        transportation = Transportation.query.get(id)
        response = transportation_schema.dump(transportation)
        return jsonify(response)
    else:
        return jsonify({"Message": "Invalid Token. Please Verify Token."}), 401

@api.route('/homeEnergy', methods = ['GET'])
@token_required
def get_homeEnergy(current_user_token):
    homeEn = current_user_token.token
    if homeEn == current_user_token.token:
        homeEnergy = HomeEnergy.query.get(id)
        response = homeEnergy_schema.dump(homeEnergy)
        return jsonify(response)
    else:
        return jsonify({"Message": "Invalid Token. Please Verify Token."}), 401

@api.route('/transportation/<id>', methods = ['POST','PUT'])
@token_required
def update_transportation(current_user_token, id):
    transportation = Transportation.query.get(id) 
    travel = request.json['travel']
    vehicle = request.json['vehicle']
    fuel = request.json['fuel']
    carpool = request.json['carpool']
    miles = request.json['miles']
    user_token = current_user_token.token
    
    transportation.travel = travel
    transportation.vehicle = vehicle
    transportation.fuel = fuel
    transportation.carpool = carpool
    transportation.miles = miles
    transportation.user_token = current_user_token.token
    
    db.session.commit()
    response = transportation_schema.dump(transportation)
    return jsonify(response)

@api.route('/homeEnergy/<id>', methods = ['POST','PUT'])
@token_required
def update_homeEnergy(current_user_token, id):
    homeEnergy = HomeEnergy.query.get(id) 
    dishwasher = request.json['dishwasher']
    dishwasherLoads = request.json['dishwasherLoads']
    washer = request.json['washer']
    washerLoads = request.json['washerLoads']
    dryer = request.json['dryer']
    dryerLoads = request.json['dryerLoads']
    lights = request.json['lights']
    lightsNumber = request.json['lightsNumber']
    lightsTime = request.json['lightsTime']
    hvac = request.json['hvac']
    hvacTime = request.json['hvacTime']
    hvacTemp= request.json['hvacTemp']
    user_token = current_user_token.token
    
    homeEnergy.dishwasher = dishwasher
    homeEnergy.dishwasherLoads = dishwasherLoads
    homeEnergy.washer = washer
    homeEnergy.washerLoads = washerLoads
    homeEnergy.dryer = dryer
    homeEnergy.dryerLoads = dryerLoads
    homeEnergy.lights = lights
    homeEnergy.lightsNumber = lightsNumber
    homeEnergy.lightsTime = lightsTime
    homeEnergy.hvac = hvac
    homeEnergy.hvacTime = hvacTime
    homeEnergy.hvacTemp = hvacTemp
    homeEnergy.user_token = current_user_token.token
    
    db.session.commit()
    response = homeEnergy_schema.dump(homeEnergy)
    return jsonify(response)

@api.route('/transportation/<id>', methods = ['DELETE'])
@token_required
def delete_transportation(current_user_token, id):
    transportation = Transportation.query.get(id)
    db.session.delete(transportation)
    db.session.commit()
    response = transportation_schema.dump(transportation)
    return jsonify(response)


@api.route('/homeEnergy/<id>', methods = ['DELETE'])
@token_required
def delete_homeEnergy(current_user_token, id):
    homeEnergy = HomeEnergy.query.get(id)
    db.session.delete(homeEnergy)
    db.session.commit()
    response = homeEnergy_schema.dump(homeEnergy)
    return jsonify(response)

