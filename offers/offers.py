from flask import Flask, jsonify, render_template, Response
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
CORS(app)

metrics = PrometheusMetrics(app)
metrics.info("offers_service", "Offers service metrics")

offers_data = [
    {"id": 1, "name": "Internet 50GB", "price": "15 TND"},
    {"id": 2, "name": "Mobile 100min", "price": "10 TND"}
]

@app.route("/offers")
def offers_page():
    return render_template("offers.html")

@app.route("/offers/api")
def get_offers():
    return jsonify(offers_data)

@app.route("/metrics")
def metrics_endpoint():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
