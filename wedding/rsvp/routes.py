from flask import render_template, redirect, request, Blueprint
from wedding import db
from wedding.models import Guest,Family

rsvps = Blueprint('rsvp', __name__)

@rsvps.route("/find-invitation")
def findInvitation():
    return render_template('find_invitation.html')

@rsvps.route("/find-invitation",methods=['POST'])
def findGuest():
    name_search = request.form['name-search']
    print("Name input: ", name_search)
    guest_search = list(filter(lambda guest: guest.first_name in name_search or guest.last_name in name_search, Guest.query.all()))

    return render_template('find_invitation.html',guests=guest_search)

@rsvps.route("/rsvp",methods=['POST'])
def rsvp():
    # Get the selected IDs from the HTML form through the request.
    guest_ids = []
    if request.form is not None:
        for selected in request.form:
            id = selected[0]
            if id is not None:
                guest_ids.append(int(id))

    # Get the guest object based on the selected IDs in the form.
    selected_guests = list(filter(lambda guest: guest.id in guest_ids, Guest.query.all()))            

    return render_template('rsvp.html', guests=selected_guests)

@rsvps.route("/submit-rsvp",methods=['POST'])
def submit_rsvp():
    # Once you get the RSVP, you take in the form data here and put it all in your database.

    return redirect("/home")