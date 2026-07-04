from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    #import models
    from app.models.user import User

    #import blueprints
    from app.routes.main import main
    from app.routes.auth import auth

    #register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
    
    
