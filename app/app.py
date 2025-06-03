from flask import Flask, jsonify, redirect
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import random

app = Flask(__name__)

# Define a Prometheus metric
random_metric = Gauge('custom_random_metric', 'Random value between 10 and 50')

@app.route('/random')
def get_random_number():
    value = random.randint(10, 50)
    random_metric.set(value)
    return jsonify({"random_number": value})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/grafana')
def grafana_redirect():
    return redirect("http://localhost:3000")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
