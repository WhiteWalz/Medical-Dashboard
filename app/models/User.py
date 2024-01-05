from app import db, loginmanager
from flask_login import UserMixin
from hashlib import sha256
from dotenv import load_dotenv
from enum import Enum
from os import getenv

load_dotenv('../.env', override=True)
SALT = getenv('SALT')

class roles(Enum):
    GENERAL = 0
    RECEPTION = 1
    INVENTORY = 2
    MANAGER = 3
    ADMIN = 4

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    is_authenticated = True
    is_active = db.Column(db.String(5), nullable=False)
    is_anonymous = False

    def __init__(self, email: str, pwd: str, role: int):
        self.email = email
        self.password = sha256(SALT + pwd)
        self.role = role

    def get_id(self):
        return str(self.id)

    def findByID(id):
        return User.query.filter_by(user_id=id).first()
    
    def findByEmail(email: str):
        return User.query.filter_by(email=email).first()
    
    def verifyLogin(email: str, password: str):
        user = User.findByEmail(email)
        if user is None:
            return None
        pwdHash = sha256(SALT + password)

        if user.password == pwdHash:
            return user.id
        
        return None
    
@loginmanager.user_loader
def loadUser(id):
    return User.findByID(id)