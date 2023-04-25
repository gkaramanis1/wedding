from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.html')

if __name__ == '__main__':
    app.run(debug=True)