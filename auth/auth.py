from flask import Flask, request, jsonify
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data.get("user") == "client" and data.get("pass") == "globalnet2026":
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
