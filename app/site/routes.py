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
    transportations = Transportation.query.all()
    return render_template("emissions.html", transportations=transportations)

@site.route('/transportation', methods=['POST'])
@login_required
def transportation():
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

@site.route('/homeEnergy', methods=['POST'])
@login_required
def homeEnergy():
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
    
    homeEnergy = HomeEnergy(dishwasher = dishwasher, dishwasherLoads = dishwasherLoads, washer = washer, washerLoads = washerLoads, dryer = dryer, dryerLoads = dryerLoads, lights = lights, lightsTime = lightsTime, hvac = hvac, hvacTime = hvacTime, hvacTemp = hvacTemp, user_token = user_token )
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


# @site.route('/update/<id>/edit', methods=['POST', 'PUT'])
# def update(id):
#     # car = Car.query.get(id)
#     vin = Car.query.filter_by(id=id).first()
#     # form=update_car
#     if request.method == 'POST':
        # print("I printed!")
        # if vin:
        
        #     vin = request.form['vin']
        #     year = request.form['year']
        #     make = request.form['make']
        #     model = request.form['model']
        #     color = request.form['color']
            
    #         car = Car(vin ='',  year ='', make='', model='')
            
    #         db.session.update(car)
    #         db.session.commit()
    #         return  redirect(url_for('/site.cars'))
    #     return f"Car does not exist."
        
    
    # return render_template('update.html', car=car)
    

@site.route('/delete_transportation/<id>', methods=['POST'])
@login_required
def delete_transportation(id):
    transportations = Transportation.query.filter_by(id=id).first()
    if request.method == 'POST':
        if transportations:
            db.session.delete(transportations)
            db.session.commit()
            return redirect(url_for('site.emissions'))
        return render_template('/delete.html')
    
    
    # transportation = Transportation.query.get(id)
    # db.session.delete(transportation)
    # db.session.commit()
    # response = transportation_schema.dump(transportation)
    # return jsonify(response)
    
    
    # transportation = Transportation.query.get(id)
    # if request.method == 'POST':
    #     if transportation:
    #         db.session.delete(transportation)
    #         db.session.commit()
    #         return redirect(urs_for('site.emissions'))
    
    # # for transport in transportation:
    # #     db.session.delete(transport)
    # #     db.session.commit()
    # return redirect(url_for('site.emissions'))
    
    # transportation = Transportation.query.all()
    # for transport in transportation:
    #     db.session.delete(transport)
    #     db.session.commit()
        # return redirect(url_for('site.emissions'))
    
    
    # return redirect(url_for('site.emissions'))

