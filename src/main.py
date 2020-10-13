from os import getenv

from flask import Flask
from flask_migrate import Migrate


from src.models import db
from src.api import actors, movies, errors


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        app.register_blueprint(errors.bp)
        app.register_blueprint(actors.bp)
        app.register_blueprint(movies.bp)
    return app
