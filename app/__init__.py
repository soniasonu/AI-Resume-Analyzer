from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    #import models
    from app.models.user import User
    from app.models.resume import Resume
    from app.models.analysis import Analysis

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #import blueprints
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.resume import resume

    #register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(resume)

    return app
    
    
