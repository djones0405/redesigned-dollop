# login.py

from flask import Blueprint

from auth import auth_bp

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def index():
    ...

@login_bp.route('/logout')
def logout():
    ...
