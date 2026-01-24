from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def offers():
    return send_from_directory(".", "offers.html")

@app.route("/login")
def login():
    return send_from_directory(".", "login.html")

@app.route("/contact")
def contact():
    return send_from_directory(".", "contact.html")

app.run(host="0.0.0.0", port=8080)
