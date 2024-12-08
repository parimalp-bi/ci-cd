from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest


app = Flask(__name__)

# Define a Counter metric
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'Latency of HTTP requests in seconds', ['method', 'endpoint'])


@app.route('/')
def index():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        return "Welcome to the Flask app!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
