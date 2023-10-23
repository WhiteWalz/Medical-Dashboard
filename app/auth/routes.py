from flask import render_template, redirect, request
from flask_login import login_required, login_url, login_user

from app.auth import bp


@bp.route('/login')
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
