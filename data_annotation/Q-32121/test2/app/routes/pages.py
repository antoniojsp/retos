from flask import Blueprint, render_template

pages = Blueprint('pages', __name__)


@pages.route('/')
def home():
    return render_template('pages/home.html')


@pages.route('/whats-going-on')
def whats_going_on():
    return render_template('pages/whats_going_on.html')


@pages.route('/what-can-we-do')
def what_can_we_do():
    return render_template('pages/what_can_we_do.html')
