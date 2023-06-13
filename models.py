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
    lightsTime = db.Column(db.Integer, nullable = False)
    hvac = db.Column(db.String(75), nullable = False)
    hvacTime = db.Column(db.Integer, nullable = False)
    hvacTemp = db.Column(db.Integer, nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, dishwasher, dishwasherLoads, washer, washerLoads, dryer, dryerLoads, lights,lightsTime, hvac, hvacTime, hvacTemp,  user_token):
        self.dishwashe = dishwasher
        self.dishwasherLoads = dishwasherLoads
        self.washer = washer
        self.washerLoads = washerLoads
        self.dryer = dryer
        self.dryerLoads = dryerLoads
        self.lights = lights
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
        fields = ['dishwasher', 'dishwasherLoads', 'washer', 'washerLoads', 'dryer', 'dryerLoads', 'lights','lightsTime', 'hvac', 'hvacTime', 'hvacTemp']

homeEnergy_schema = HomeEnergySchema()
homeEnergys_schema = HomeEnergySchema(many=True)


# class Car(db.Model):
#     vin = db.Column(db.String(17), primary_key=True)
#     make = db.Column(db.String(75), unique = False, nullable = False)
#     model = db.Column(db.String(75), unique = False, nullable = False)
#     year = db.Column(db.Integer,  unique = False, nullable = False)
#     color = db.Column(db.String, unique = False, nullable = False)
#     user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False, default = '')
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    
    
#     def __init__(self,  vin, make, model, year, color,  user_id):
#         self.vin = vin
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.user_id = user_id
    
    
#     def __repr__(self):
#         return f'Car {self.year} {self.make} {self.model} has been added to the database'
    
 
# class CarSchema(ma.Schema):
#     class Meta:
#         fields = ['vin', 'make', 'model', 'year', 'color', 'user_id']

# car_schema = CarSchema()
# cars_schema = CarSchema(many=True)

