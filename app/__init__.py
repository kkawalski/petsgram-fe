from flask import Flask

from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes

from auth import auth_blueprint, routes
from users import users_blueprint, routes
app.register_blueprint(auth_blueprint)
app.register_blueprint(users_blueprint)
