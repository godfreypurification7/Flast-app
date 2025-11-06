from flask import Flask

app = Flask(__name__)  # WSGI application

@app.route('/')
def welcome(): 
    return "Welcome to my YouTube channel. Please subscribe to my channel."

@app.route('/members')
def members():
    return "Members page"

@app.route('/admin')
def admin():
    return "Admin page"

@app.route('/member/Sajib')
def Sajib(name):
    return "Sajib Member page"

if __name__ == "__main__":
    app.run(debug=True)

