from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []

@app.route("/contact", methods=["POST"])
def contact():
    messages.append(request.get_json())
    return jsonify({"status":"ok"})

app.run(host="0.0.0.0", port=5002)
