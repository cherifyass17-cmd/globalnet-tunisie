from flask import Flask, jsonify
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

offers = [
    {"id": 1, "name": "Internet 50GB", "price": "15TND"},
    {"id": 2, "name": "Mobile 100min", "price": "10TND"}
]

@app.route("/offers")
def get_offers():
    return jsonify(offers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
