from flask import render_template, redirect, request, Blueprint
from wedding import db
from wedding.models import Guest,Family

rsvps = Blueprint('rsvp', __name__)

@rsvps.route("/rsvp")
def rsvp():
    return render_template('rsvp.html')

@rsvps.route("/rsvp",methods=['POST'])
def findGuest():
    name_search = request.form['name-search']
    print("Name input: ", name_search)
    guest_search = list(filter(lambda guest: guest.first_name in name_search or guest.last_name in name_search, Guest.query.all()))

    for guest in guest_search:
       print(guest)

    return render_template('rsvp.html',guests=guest_search)
