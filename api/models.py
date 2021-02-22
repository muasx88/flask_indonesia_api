import datetime
from .ext import db


class Province(db.Model):
	__tablename__ = 'idn_provinces'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	coordinate = db.Column(db.Text())
	created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__(self, name, coordinate=None):
		self.name = name
		self.coordinate = coordinate

	def __str__(self):
		return f"Name : {self.name} - Coordinate: {self.coordinate}"


class City(db.Model):
	__tablename__ = 'idn_cities'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	coordinate = db.Column(db.Text())
	province_id = db.Column(db.Integer, db.ForeignKey('id_provinces.id'), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__(self, name, coordinate=None, province_id=None):
		self.name = name
		self.coordinate = coordinate
		self.province_id = province_id

	def __str__(self):
		return f"Name : {self.name} - Coordinate: {self.coordinate}"


class District(db.Model):
	__tablename__ = 'idn_districts'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	coordinate = db.Column(db.Text())
	city_id = db.Column(db.Integer, db.ForeignKey('id_cities.id'), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__(self, name, coordinate=None, city_id=None):
		self.name = name
		self.coordinate = coordinate
		self.city_id = city_id

	def __str__(self):
		return f"Name : {self.name} - Coordinate: {self.coordinate}"


class Village(db.Model):
	__tablename__ = 'idn_villages'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	coordinate = db.Column(db.Text())
	district_id = db.Column(db.Integer, db.ForeignKey('id_districts.id'), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

	def __init__(self, name, coordinate=None, district_id=None):
		self.name = name
		self.coordinate = coordinate
		self.district_id = district_id

	def __str__(self):
		return f"Name : {self.name} - Coordinate: {self.coordinate}"

	