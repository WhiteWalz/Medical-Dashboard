from flask import render_template, redirect, request
from flask_login import login_required, login_url, login_user, current_user, logout_user

from app.auth import bp


@bp.route('/login')
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    
@bp.route('/logout')
def logout():
    logout_user()
    return redirect('/')

# Route to the main user dashboard, will render differently for different roles.
@login_required 
@bp.route('/dashboard')
def dashboard(user):
    render_template('/auth/dashboard.html', current_user.role)

# Route used to view or edit current inventory stock, depending on role.
@bp.route('/stock/<string:id>')
def stockadjust(id):
    return render_template('/auth/stockadjust.html', current_user.role, Items.getByID(id))

# Route used to view or edit the employee schedule, depending on role.
@login_required
@bp.route('/schedule')
def schedule():
    return render_template('/auth/schedule.html', current_user.role)