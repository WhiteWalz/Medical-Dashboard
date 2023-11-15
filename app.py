from flask import Flask, Blueprint
from flask_login import LoginManager
from app.auth import bp as auth_bp
from app.general import bp as general_bp

app = Flask(__name__)
loginmanager = LoginManager()
loginmanager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(general_bp)

if __name__ == "__main__":
    app.run("0.0.0.0", 3333, True)