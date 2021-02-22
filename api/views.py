from flask import Blueprint, jsonify
from .models import Province, City, District, Village

main = Blueprint('/', __name__)

@main.route('/')
def index():
	return jsonify({'code':200, 'message': 'Indonesia API'})


@main.route('/province')
def get_province():
	province_list = Province.query.all()
	provinces = []
	for d in province_list:
		provinces.append({'id': d.id, 'name': d.name, 'coordinate':d.coordinate})

	return jsonify({'code':200, 'message': 'OK','results':provinces})


@main.route('/city/<int:province_id>')
def get_city(province_id):
	city_list = City.query.filter_by(province_id=province_id).all()
	cities = []
	for d in city_list:
		cities.append({'id': d.id, 'name': d.name, 'coordinate':d.coordinate, 'province_id': d.province_id})

	return jsonify({'code':200,'message': 'OK', 'results':cities})


@main.route('/district/<int:city_id>')
def get_district(city_id):
	district_list = District.query.filter_by(city_id=city_id).all()
	districts = []
	for d in district_list:
		districts.append({'id': d.id, 'name': d.name, 'coordinate':d.coordinate, 'city_id': d.city_id})

	return jsonify({'code':200,'message': 'OK', 'results':districts})


@main.route('/village/<int:district_id>')
def get_village(district_id):
	village_list = Village.query.filter_by(district_id=district_id).all()
	villages = []
	for d in village_list:
		villages.append({'id': d.id, 'name': d.name, 'coordinate':d.coordinate, 'district_id': d.district_id})

	return jsonify({'code':200,'message': 'OK', 'results':villages})