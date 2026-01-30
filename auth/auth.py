from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_Client import generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
CORS(app)

metrics = PrometheusMetrics(app)
metrics.info("auth_service", "Auth service metrics")

@app.route("/auth")
def auth_page():
    return render_template("auth.html")

@app.route("/auth/api", methods=["POST"])
def auth_api():
    data = request.json
    if data.get("username") == "user" and data.get("password") == "pass":
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route("/metrics")
def metrics_endpoint():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
