from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from models import db, User, Transportation, transportation_schema, transportations_schema, HomeEnergy, homeEnergy_schema, homeEnergys_schema
from flask_login import current_user, login_required


site = Blueprint('site', __name__,template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/emissions')
@login_required
def emissions():
    transportations = Transportation.query.all(),
    homeEnergys = HomeEnergy.query.all()
    return render_template("emissions.html", transportations=transportations, homeEnergys=homeEnergys )

@site.route('/transportations')
@login_required
def transportations():
    transportations = Transportation.query.all()
    return render_template('transportation.html', transportations=transportations)

@site.route('/homeEnergys')
@login_required
def homeEnergys():
    homeEnergys = HomeEnergy.query.all()
    return render_template('homeEnergy.html', homeEnergys=homeEnergys)

@site.route('/create_transportation', methods=['POST'])
@login_required
def create_transportation():
    travel = request.form['travel']
    vehicle = request.form['vehicle']
    fuel = request.form['fuel']
    carpool = request.form['carpool']
    miles = request.form['miles']
    user_token = current_user.token
    
    transportation = Transportation(travel = travel, vehicle = vehicle, fuel = fuel, carpool = carpool, miles = miles, user_token = user_token )
    db.session.add(transportation)
    db.session.commit()
    
    return render_template('site.transportations')

@site.route('/create_homeEnergy', methods=['POST'])
@login_required
def create_homeEnergy():
    dishwasher = request.form['dishwasher']
    dishwasherLoads = request.form['dishwasherLoads']
    washer = request.form['washer']
    washerLoads = request.form['washerLoads']
    dryer = request.form['dryer']
    dryerLoads = request.form['dryerLoads']
    lights = request.form['lights']
    lightsNumber = request.form['lightsNumber']
    lightsTime = request.form['lightsTime']
    hvac = request.form['hvac']
    hvacTime = request.form['hvacTime']
    hvacTemp= request.form['hvacTemp']
    user_token = current_user.token
    
    homeEnergy = HomeEnergy(dishwasher = dishwasher, dishwasherLoads = dishwasherLoads, washer = washer, washerLoads = washerLoads, dryer = dryer, dryerLoads = dryerLoads, lights = lights,  lightsNumber = lightsNumber ,lightsTime = lightsTime, hvac = hvac, hvacTime = hvacTime, hvacTemp = hvacTemp, user_token = user_token )
    
    db.session.add(homeEnergy)
    db.session.commit()
    
    return redirect(url_for('site.homeEnergy'))

@site.route('/recycling', methods=['POST'])
@login_required
def recycling():
    travel = request.form['travel']
    vehicle = request.form['vehicle']
    fuel = request.form['fuel']
    carpool = request.form['carpool']
    miles = request.form['miles']
    user_token = current_user.token
    
    transportation = Transportation(travel = travel, vehicle = vehicle, fuel = fuel, carpool = carpool, miles = miles, user_token = user_token )
    db.session.add(transportation)
    db.session.commit()
    
    return redirect(url_for('site.emissions'))

@site.route('/water', methods=['POST'])
@login_required
def water():
    travel = request.form['travel']
    vehicle = request.form['vehicle']
    fuel = request.form['fuel']
    carpool = request.form['carpool']
    miles = request.form['miles']
    user_token = current_user.token
    
    transportation = Transportation(travel = travel, vehicle = vehicle, fuel = fuel, carpool = carpool, miles = miles, user_token = user_token )
    db.session.add(transportation)
    db.session.commit()
    
    return redirect(url_for('site.emissions'))

@site.route('/waste', methods=['POST'])
@login_required
def waste():
    travel = request.form['travel']
    vehicle = request.form['vehicle']
    fuel = request.form['fuel']
    carpool = request.form['carpool']
    miles = request.form['miles']
    user_token = current_user.token
    
    transportation = Transportation(travel = travel, vehicle = vehicle, fuel = fuel, carpool = carpool, miles = miles, user_token = user_token )
    db.session.add(transportation)
    db.session.commit()
    
    return redirect(url_for('site.emissions'))

@site.route('/update_transportation/<string:id>', methods = ['POST', 'PUT'])
@login_required
def update_transportation(id):
    transportation = Transportation.query.get(id)
    
    travel = request.form['travel']
    vehicle = request.form['vehicle']
    fuel = request.form['fuel']
    carpool = request.form['carpool']
    miles = request.form['miles']
    
    transportation = Transportation(travel = travel, vehicle = vehicle, fuel = fuel, carpool = carpool, miles = miles, user_token = user_token )
    
    db.session.update(transportation)
    db.session.commit()
    
    return redirect(url_for('site.transportation'))


@site.route('/update_homeEnergy/<string:id>', methods = ['POST', 'PUT'])
@login_required
def update_homeEnergy(id):
    homeEnergy = HomeEnergy.query.get(id)
    
    dishwasher = request.form['dishwasher']
    dishwasherLoads = request.form['dishwasherLoads']
    washer = request.form['washer']
    washerLoads = request.form['washerLoads']
    dryer = request.form['dryer']
    dryerLoads = request.form['dryerLoads']
    lights = request.form['lights']
    lightsNumber = request.form['lightsNumber']
    lightsTime = request.form['lightsTime']
    hvac = request.form['hvac']
    hvacTime = request.form['hvacTime']
    hvacTemp= request.form['hvacTemp']
    
    homeEnergy = HomeEnergy(dishwasher = dishwasher, dishwasherLoads = dishwasherLoads, washer = washer, washerLoads = washerLoads, dryer = dryer, dryerLoads = dryerLoads, lights = lights,  lightsNumber = lightsNumber ,lightsTime = lightsTime, hvac = hvac, hvacTime = hvacTime, hvacTemp = hvacTemp, user_token = user_token )
    
    db.session.add(homeEnergy)
    db.session.commit()
    
    return redirect(url_for('site.homeEnergy'))


@site.route('/delete_transportation/<id>', methods=['POST', 'GET', 'DELETE'])
@login_required
def delete_transportation(id):
    transportations = Transportation.query(id)
    if request.method == 'POST':
        if transportation:
            db.session.delete(transportations)
            db.session.commit()
            return redirect(url_for('site.transportations'))
        return render_template('stie.transportations')
    

@site.route('/delete_homeEnergy/<id>', methods=['POST', 'GET', 'DELETE'])
@login_required
def delete_homeEnergy(id):
    homeEnergys = HomeEnergy.query(id)
    if request.method == 'POST':
        if homeEnergy:
            db.session.delete(homeEnergys)
            db.session.commit()
            return redirect(url_for('site.homeEnergys'))
        return render_template('stie.homeEnergys')
    