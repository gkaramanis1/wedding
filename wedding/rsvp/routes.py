from flask import render_template, redirect, request, Blueprint
from wedding import db
from wedding.models import Guest,Family

rsvps = Blueprint('rsvp', __name__)

@rsvps.route("/rsvp")
def rsvp():
        guest = Guest.query.first()
        print(guest)
        return render_template('rsvp.html')
