from datetime import datetime
from flask import current_app
from wedding import db

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    allergies = db.Column(db.String(120), nullable=True)
    response = db.Column(db.Boolean, nullable=True)
#    family_id = db.relationship('family', backref='family', lazy=True)

    def __repr__(self):
        return f"Guest('{self.last_name}', '{self.first_name}')"


class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Family('{self.name}')"
