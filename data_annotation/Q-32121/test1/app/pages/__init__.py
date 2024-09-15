from flask import Blueprint, render_template

pages_bp = Blueprint('templates', __name__, template_folder='templates')

@pages_bp.route('/whats-going-on')
def whats_going_on():
    return render_template('templates/whats_going_on.html')

@pages_bp.route('/what-can-we-do')
def what_can_we_do():
    return render_template('templates/what_can_we_do.html')

@pages_bp.route('/')  # Assuming you have a home page
def home():
    return render_template('templates/home.html')