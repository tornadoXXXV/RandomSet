from flask import request, jsonify, render_template
from flask.blueprints import Blueprint
import random
import datetime
import jpholiday
from models.models import *
from db import db
from sub import isBizDay

menu_blueprint = Blueprint('menu', __name__, url_prefix="/menu")

@menu_blueprint.route('/')
def show_menus():
    now = datetime.datetime.now()
    date = now.strftime('%Y年%m月%d日 %H:%M（%a）')
    return render_template('index.html', date=date)

@menu_blueprint.route('/get1000', methods=['GET'])
# コントローラーの引数について調べる
def random_select_handler1000():
    max = 1000
    total_price = 0
    total_cal = 0
    selected = []
    set_menu = []
    drink_list = [30,33,36,39,42,45,48,51,54,57,60,62,64,66,69,71,72,74,76,78]
    side_list = [19,21,23,24,25]
    now = datetime.datetime.now()
    date = now.strftime('%Y年%m月%d日 %H:%M（%a）')
    Ymd = now.strftime('%Y%m%d')
    HM = now.strftime('%H%M')
    WeekOrHoli = isBizDay(Ymd)

    while True:
        menu = db.session.query(Menu).filter(
            Menu.price <= max
        ).all()

        if not menu:
            break

        rand = random.choice(menu)

        if rand.id >= 91:
            if WeekOrHoli == 1 and 1030 <= int(HM) < 1400:
                if rand.id == 91:
                    rand.price -= 90
                elif rand.id == 98:
                    rand.price -= 120
                elif rand.id == 94 or rand.id == 95 or rand.id == 96:
                    rand.price -= 100
            drink_number = random.choice(drink_list)
            side_number = random.choice(side_list)
            
            set_burger = db.session.query(Menu).filter(
                Menu.id == rand.id-90   
            ).all()
            set_drink = db.session.query(Menu).filter(
                Menu.id == drink_number
            ).all()
            set_side = db.session.query(Menu).filter(
                Menu.id == side_number
            ).all()

            set_menu.extend([set_burger[0],set_drink[0],set_side[0]])
            total_cal += (int(set_drink[0].cal) + int(set_side[0].cal) + int(set_burger[0].cal))
        else:
            total_cal += int(rand.cal)

        max -= int(rand.price)
        total_price += int(rand.price)
        selected.append(rand)
    
    print(selected)
    return render_template('index.html', date=date, selected=selected, set_menu=set_menu, total_price=total_price, total_cal=total_cal)

@menu_blueprint.route('/get2000', methods=['GET'])
def random_select_handler2000():
    max = 2000
    total_price = 0
    total_cal = 0
    selected = []
    set_menu = []
    drink_list = [30,33,36,39,42,45,48,51,54,57,60,62,64,66,69,71,72,74,76,78]
    side_list = [19,21,23,24,25]
    now = datetime.datetime.now()
    date = now.strftime('%Y年%m月%d日 %H:%M（%a）')
    Ymd = now.strftime('%Y%m%d')
    HM = now.strftime('%H%M')
    WeekOrHoli = isBizDay(Ymd)

    while True:
        menu = db.session.query(Menu).filter(
            Menu.price <= max
        ).all()

        if not menu:
            break

        rand = random.choice(menu)

        if rand.id >= 91:
            if WeekOrHoli == 1 and 1030 <= int(HM) < 1400:
                if rand.id == 91:
                    rand.price -= 90
                elif rand.id == 98:
                    rand.price -= 120
                elif rand.id == 94 or rand.id == 95 or rand.id == 96:
                    rand.price -= 100
            drink_number = random.choice(drink_list)
            side_number = random.choice(side_list)
            
            set_burger = db.session.query(Menu).filter(
                Menu.id == rand.id-90   
            ).all()
            set_drink = db.session.query(Menu).filter(
                Menu.id == drink_number
            ).all()
            set_side = db.session.query(Menu).filter(
                Menu.id == side_number
            ).all()

            set_menu.extend([set_burger[0],set_drink[0],set_side[0]])
            total_cal += (int(set_drink[0].cal) + int(set_side[0].cal) + int(set_burger[0].cal))
        else:
            total_cal += int(rand.cal)

        max -= int(rand.price)
        total_price += int(rand.price)
        selected.append(rand)
    
    print(selected)
    return render_template('index.html', date=date, selected=selected, set_menu=set_menu, total_price=total_price, total_cal=total_cal)

@menu_blueprint.route('/get3000', methods=['GET'])
def random_select_handler3000():
    max = 3000
    total_price = 0
    total_cal = 0
    selected = []
    set_menu = []
    drink_list = [30,33,36,39,42,45,48,51,54,57,60,62,64,66,69,71,72,74,76,78]
    side_list = [19,21,23,24,25]
    now = datetime.datetime.now()
    date = now.strftime('%Y年%m月%d日 %H:%M（%a）')
    Ymd = now.strftime('%Y%m%d')
    HM = now.strftime('%H%M')
    WeekOrHoli = isBizDay(Ymd)

    while True:
        menu = db.session.query(Menu).filter(
            Menu.price <= max
        ).all()

        if not menu:
            break

        rand = random.choice(menu)

        if rand.id >= 91:
            if WeekOrHoli == 1 and 1030 <= int(HM) < 1400:
                if rand.id == 91:
                    rand.price -= 90
                elif rand.id == 98:
                    rand.price -= 120
                elif rand.id == 94 or rand.id == 95 or rand.id == 96:
                    rand.price -= 100
            drink_number = random.choice(drink_list)
            side_number = random.choice(side_list)
            
            set_burger = db.session.query(Menu).filter(
                Menu.id == rand.id-90   
            ).all()
            set_drink = db.session.query(Menu).filter(
                Menu.id == drink_number
            ).all()
            set_side = db.session.query(Menu).filter(
                Menu.id == side_number
            ).all()

            set_menu.extend([set_burger[0],set_drink[0],set_side[0]])
            total_cal += (int(set_drink[0].cal) + int(set_side[0].cal) + int(set_burger[0].cal))
        else:
            total_cal += int(rand.cal)

        max -= int(rand.price)
        total_price += int(rand.price)
        selected.append(rand)
    
    set_length = len(set_menu)
    print(selected)
    return render_template('index.html', date=date, selected=selected, set_menu=set_menu, total_price=total_price, total_cal=total_cal)
