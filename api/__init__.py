
from flask import Flask, make_response

from . import config
from .views import main
from .ext import db # migrate, seeder


def create_app():
	app = Flask(__name__)

	app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URL
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
	app.register_blueprint(main)

	@app.errorhandler(404)
	def not_found(error):
		resp = make_response({'code':404,'message':'Route Not Found'}, 404)
		resp.headers['content-type'] = 'application/json'
		return resp

	db.init_app(app)
	# migrate.init_app(app, db)
	# seeder.init_app(app, db)

	return app