##BUilding url dynamically
### variable rules

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to the youtube channel"


@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the score is " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the score is " + str(score)
##result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50: 
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score=marks))



if __name__ == "__main__":
    app.run(debug=True)

# https://github.com/krishnaik06/Flask-Web-Framework
# https://www.youtube.com/watch?v=cWOpkTWg2vE&list=PLZoTAELRMXVPBaLN3e-uoVRR9hlRFRfUc&index=5