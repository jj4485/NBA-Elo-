from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

# Initialize Flask extensions
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure the Flask app
    app.config['SECRET_KEY'] = 'your-secret-key'  # Change this in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nba_rankings.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db.init_app(app)

    # Import and register blueprints
    from .routes import main
    app.register_blueprint(main)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
