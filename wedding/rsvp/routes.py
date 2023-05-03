from flask import render_template, redirect, request, Blueprint
from wedding import db
from wedding.models import Guest,Family

rsvps = Blueprint('rsvp', __name__)

@rsvps.route("/find-invitation")
def findInvitation():
    return render_template('find_invitation.html')

@rsvps.route("/find-invitation",methods=['POST'])
def findGuest():
    name_search = request.form['name-search'].casefold()
    print("Name input: ", name_search)
    guest_search = list(filter(lambda guest: guest.first_name.casefold() in name_search or guest.last_name.casefold() in name_search, Guest.query.all()))

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
    for response_id, response_value in request.form.items():
        # Get the guest's ID in this key value pair and the value ID. Example: 3_allergies -> guest_id = 3, val_id = allergies
        guest_id = response_id[:response_id.index("_")]
        val_id = response_id[response_id.index("_")+1:]

        # Get the guest from the SQL Alchemy load and set the values based on what came through in the request.
        if guest_id is not None:
            guest = next((guest for guest in Guest.query.all() if guest.id == int(guest_id)), None)
            if guest:
                setattr(guest, val_id, response_value)

        print(response_id)
        print(type(response_value))

    # Now that you've updated all of the guests, commit the changes to the database.
    db.session.commit()

    return redirect("/")
