from flask import Flask
from config import Config
from extensions import db, jwt
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.post import post_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)

    Swagger(app)

    return app
