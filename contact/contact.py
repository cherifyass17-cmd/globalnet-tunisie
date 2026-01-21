from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

messages = []

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    messages.append(data)
    return jsonify({"status": "received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
