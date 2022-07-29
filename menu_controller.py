from flask import request, jsonify, render_template
from flask.blueprints import Blueprint
from models.models import *
from db import db
import random

menu_blueprint = Blueprint('menu', __name__, url_prefix="/menu")


@menu_blueprint.route('/')
def show_menus():
    return render_template('index.html')

@menu_blueprint.route('/get1000', methods=['GET'])
def random_select_handler1000():
    max = 1000
    total_price = 0
    total_cal = 0
    selected = []

    while True:
        menu = db.session.query(Menu).filter(
            Menu.id <= 90 , Menu.price <= max
        ).all()

        if not menu:
            break

        rand = random.choice(menu)
        max -= int(rand.price)
        total_price += int(rand.price)
        total_cal += int(rand.cal)
        selected.append(rand)
    
    print(selected)
    return render_template('index.html', selected=selected, total_price=total_price, total_cal=total_cal)

@menu_blueprint.route('/get2000', methods=['GET'])
def random_select_handler2000():
    max = 2000
    total_price = 0
    total_cal = 0
    selected = []

    while True:
        menu = db.session.query(Menu).filter(
            Menu.id <= 90 , Menu.price <= max
        ).all()

        if not menu:
            break

        rand = random.choice(menu)
        max -= int(rand.price)
        total_price += int(rand.price)
        total_cal += int(rand.cal)
        selected.append(rand)
    
    print(selected)
    return render_template('index.html', selected=selected, total_price=total_price, total_cal=total_cal)

@menu_blueprint.route('/get3000', methods=['GET'])
def random_select_handler3000():
    max = 3000
    total_price = 0
    total_cal = 0
    selected = []

    while True:
        menu = db.session.query(Menu).filter(
            Menu.id <= 90 , Menu.price <= max
        ).all()

        if not menu:
            break

        rand = random.choice(menu)
        max -= int(rand.price)
        total_price += int(rand.price)
        total_cal += int(rand.cal)
        selected.append(rand)
    
    print(selected)
    return render_template('index.html', selected=selected, total_price=total_price, total_cal=total_cal)