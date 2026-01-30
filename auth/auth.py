from flask import Flask, render_template, Response
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
CORS(app)

metrics = PrometheusMetrics(app)
metrics.info("contact_service", "Contact service metrics")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/metrics")
def metrics_endpoint():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

