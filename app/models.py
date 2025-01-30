from . import db
from datetime import datetime

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500))
    elo_rating = db.Column(db.Integer, default=1000)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Player {self.name} (ELO: {self.elo_rating})>'
    
    def win_percentage(self):
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0
        return (self.wins / total_games) * 100

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    winner_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    loser_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    winner = db.relationship('Player', foreign_keys=[winner_id], backref='won_matches')
    loser = db.relationship('Player', foreign_keys=[loser_id], backref='lost_matches')