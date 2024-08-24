# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import BlackjackGame, Player, Deck

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/start_game', methods=['POST'])
def start_game():
    session['game'] = BlackjackGame()
    session['game'].start_new_round()
    return redirect(url_for('main.game'))

@bp.route('/game')
def game():
    game = session.get('game')
    if not game:
        return redirect(url_for('main.index'))
    return render_template('game.html', game=game)

@bp.route('/hit')
def hit():
    game = session.get('game')
    game.player_hit()
    session['game'] = game
    return redirect(url_for('main.game'))

@bp.route('/stand')
def stand():
    game = session.get('game')
    game.player_stand()
    session['game'] = game
    return redirect(url_for('main.result'))

@bp.route('/result')
def result():
    game = session.get('game')
    return render_template('result.html', game=game)