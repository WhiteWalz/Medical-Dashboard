from flask import Blueprint
from flask_login import LoginManager
from models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.getByID(user_id)

bp = Blueprint('auth', __name__)