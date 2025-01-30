from flask import Blueprint, render_template, request, jsonify
from random import sample
from . import db
# We'll import our models once we create them
# from .models import Player, Vote

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Homepage - shows two random players to vote between"""
    return render_template('index.html')  
@main.route('/leaderboard')
def leaderboard():
    """Shows all players ranked by their ELO rating"""
    
    return render_template('leaderboard.html')  

@main.route('/api/vote', methods=['POST'])
def submit_vote():
    """Handle voting submission"""
    data = request.get_json()
    
    return jsonify({'status': 'success'})

@main.route('/api/players')
def get_random_players():
    """Get two random players for voting"""
    return jsonify([])
