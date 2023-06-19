from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(150), nullable = False)
    first_name = db.Column(db.String(150), nullable=False, default='')
    last_name = db.Column(db.String(150), nullable = False, default = '')
    username = db.Column(db.String(25), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    token = db.Column(db.String, default = '', unique = True )
    g_auth_verify = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email='', first_name='', last_name='', username = '', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash


    def __repr__(self):
        return f'User {self.email} has been added to the database.'
    
class Transportation(db.Model):
    id = db.Column(db.String, primary_key=True)
    travel = db.Column(db.String(75), nullable = False)
    vehicle = db.Column(db.String(75), nullable = False)
    fuel = db.Column(db.String(75), nullable = False)
    carpool = db.Column(db.String(5), nullable = False)
    miles = db.Column(db.String(5), nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, travel, vehicle, fuel, carpool, miles, user_token):
        self.id = self.set_id()
        self.travel = travel
        self.vehicle = vehicle
        self.fuel = fuel
        self.carpool = carpool
        self.miles = miles
        self.user_token = user_token


    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.first_name} {self.last_name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class TransportationSchema(ma.Schema):
    class Meta:
        fields = ['id', 'travel', 'vehicle', 'fuel','carpool', 'miles']

transportation_schema = TransportationSchema()
transportations_schema = TransportationSchema(many=True)


class HomeEnergy(db.Model):
    id = db.Column(db.String, primary_key=True)
    dishwasher = db.Column(db.String(75), nullable = False)
    dishwasherLoads = db.Column(db.Integer, nullable = False)
    washer = db.Column(db.String(75), nullable = False)
    washerLoads = db.Column(db.Integer, nullable = False)
    dryer = db.Column(db.String(75), nullable = False)
    dryerLoads = db.Column(db.Integer, nullable = False) 
    lights = db.Column(db.String(75), nullable = False)
    lightsNumber = db.Column(db.Integer, nullable = False)
    lightsTime = db.Column(db.Integer, nullable = False)
    hvac = db.Column(db.String(75), nullable = False)
    hvacTime = db.Column(db.Integer, nullable = False)
    hvacTemp = db.Column(db.Integer, nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, dishwasher, dishwasherLoads, washer, washerLoads, dryer, dryerLoads, lights, lightsNumber, lightsTime, hvac, hvacTime, hvacTemp,  user_token):
        self.id = self.set_id()
        self.dishwasher = dishwasher
        self.dishwasherLoads = dishwasherLoads
        self.washer = washer
        self.washerLoads = washerLoads
        self.dryer = dryer
        self.dryerLoads = dryerLoads
        self.lights = lights
        self.lightsNumber = lightsNumber
        self.lightsTime = lightsTime
        self.hvac = hvac
        self.hvacTime = hvacTime
        self.hvacTemp = hvacTemp
        self.user_token = user_token


    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.first_name} {self.last_name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class HomeEnergySchema(ma.Schema):
    class Meta:
        fields = ['dishwasher', 'dishwasherLoads', 'washer', 'washerLoads', 'dryer', 'dryerLoads', 'lights',  'lightsNumber','lightsTime', 'hvac', 'hvacTime', 'hvacTemp']

homeEnergy_schema = HomeEnergySchema()
homeEnergys_schema = HomeEnergySchema(many=True)


class Recycling(db.Model):
    id = db.Column(db.String, primary_key=True)
    paper = db.Column(db.String(75), nullable = False)
    paperAmount = db.Column(db.Integer, nullable = False)
    glass = db.Column(db.String(75), nullable = False)
    glassAmount = db.Column(db.Integer, nullable = False)
    plastic = db.Column(db.String(75), nullable = False)
    plasticAmount = db.Column(db.Integer, nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, paper, paperAmount, glass, glassAmount,plastic, plasticAmount,   user_token):
        self.id = self.set_id()
        self.paper = paper
        self.paperAmount = paperAmount
        self.glass = glass
        self.glassAmount = glassAmount
        self.plastic = plastic
        self.plasticAmount = plasticAmount
        self.user_token = user_token


    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.first_name} {self.last_name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class RecyclingSchema(ma.Schema):
    class Meta:
        fields = ['paper', 'paperAmount', 'glass', 'glassAmount', 'plastic', 'plasticAmount']

recycling_schema = RecyclingSchema()
recyclings_schema = RecyclingSchema(many=True)


class Water(db.Model):
    id = db.Column(db.String, primary_key=True)
    shower = db.Column(db.String(75), nullable = False)
    showerTime = db.Column(db.Integer, nullable = False)
    washer = db.Column(db.String(75), nullable = False)
    washerLoads = db.Column(db.Integer, nullable = False)
    dryer = db.Column(db.String(75), nullable = False)
    dryerLoads = db.Column(db.Integer, nullable = False) 
    lights = db.Column(db.String(75), nullable = False)
    lightsNumber = db.Column(db.Integer, nullable = False)
    lightsTime = db.Column(db.Integer, nullable = False)
    hvac = db.Column(db.String(75), nullable = False)
    hvacTime = db.Column(db.Integer, nullable = False)
    hvacTemp = db.Column(db.Integer, nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, dishwasher, dishwasherLoads, washer, washerLoads, dryer, dryerLoads, lights, lightsNumber, lightsTime, hvac, hvacTime, hvacTemp,  user_token):
        self.id = self.set_id()
        self.dishwasher = dishwasher
        self.dishwasherLoads = dishwasherLoads
        self.washer = washer
        self.washerLoads = washerLoads
        self.dryer = dryer
        self.dryerLoads = dryerLoads
        self.lights = lights
        self.lightsNumber = lightsNumber
        self.lightsTime = lightsTime
        self.hvac = hvac
        self.hvacTime = hvacTime
        self.hvacTemp = hvacTemp
        self.user_token = user_token


    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.first_name} {self.last_name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class WaterSchema(ma.Schema):
    class Meta:
        fields = ['dishwasher', 'dishwasherLoads', 'washer', 'washerLoads', 'dryer', 'dryerLoads', 'lights',  'lightsNumber','lightsTime', 'hvac', 'hvacTime', 'hvacTemp']

water_schema = WaterSchema()
waters_schema = WaterSchema(many=True)


class Waste(db.Model):
    id = db.Column(db.String, primary_key=True)
    dishwasher = db.Column(db.String(75), nullable = False)
    dishwasherLoads = db.Column(db.Integer, nullable = False)
    washer = db.Column(db.String(75), nullable = False)
    washerLoads = db.Column(db.Integer, nullable = False)
    dryer = db.Column(db.String(75), nullable = False)
    dryerLoads = db.Column(db.Integer, nullable = False) 
    lights = db.Column(db.String(75), nullable = False)
    lightsNumber = db.Column(db.Integer, nullable = False)
    lightsTime = db.Column(db.Integer, nullable = False)
    hvac = db.Column(db.String(75), nullable = False)
    hvacTime = db.Column(db.Integer, nullable = False)
    hvacTemp = db.Column(db.Integer, nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, dishwasher, dishwasherLoads, washer, washerLoads, dryer, dryerLoads, lights, lightsNumber, lightsTime, hvac, hvacTime, hvacTemp,  user_token):
        self.id = self.set_id()
        self.dishwasher = dishwasher
        self.dishwasherLoads = dishwasherLoads
        self.washer = washer
        self.washerLoads = washerLoads
        self.dryer = dryer
        self.dryerLoads = dryerLoads
        self.lights = lights
        self.lightsNumber = lightsNumber
        self.lightsTime = lightsTime
        self.hvac = hvac
        self.hvacTime = hvacTime
        self.hvacTemp = hvacTemp
        self.user_token = user_token


    def __repr__(self):
        return f'The following contact has been added to the phonebook: {self.first_name} {self.last_name}'

    def set_id(self):
        return (secrets.token_urlsafe())

class WasteSchema(ma.Schema):
    class Meta:
        fields = ['dishwasher', 'dishwasherLoads', 'washer', 'washerLoads', 'dryer', 'dryerLoads', 'lights',  'lightsNumber','lightsTime', 'hvac', 'hvacTime', 'hvacTemp']

waste_schema = WaterSchema()
wastes_schema = WaterSchema(many=True)

