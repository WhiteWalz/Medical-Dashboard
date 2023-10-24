from flask import render_template, redirect, request
from flask_login import login_required, login_url, login_user

from app.general import bp


@bp.route('/')
def index():
    return render_template('general/index.html')