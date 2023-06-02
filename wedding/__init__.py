from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('WEDDING_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('WEDDINGDB')

    db.init_app(app)

    @app.route("/")
    def home():
        return render_template('home.html')

    @app.route("/schedule")
    def schedule():
        return render_template('schedule.html')

    @app.route("/questions")
    def questions():
        return render_template('questions.html')

    @app.route("/travel")
    def travel():
        return render_template('travel.html')

    @app.route("/registry")
    def registry():
        return render_template('registry.html')

    # from wedding.rsvp.routes import rsvps
    # app.register_blueprint(rsvps)

    return app
