# registration.py

from flask import Blueprint

from auth import auth_bp

register_bp = Blueprint('register', __name__)

@register_bp.route('/')
def index():
    ...

@register_bp.route('/success')
def success():
    ...
