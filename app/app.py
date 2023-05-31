from flask import Flask, jsonify
from prometheus_client import Counter, Gauge, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import logging

# Create Flask app
app = Flask(__name__)

# Create Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Gauge('http_request_latency_seconds', 'HTTP Request Latency', ['method', 'endpoint'])

# Define root endpoint
@app.route('/', methods=['GET'])
def welcome():
    """
    This function returns a welcome message.

    Returns:
    str: A welcome message
    """
    return 'Welcome to the service API'

# Define data endpoint
@app.route('/data', methods=['GET'])
def get_data():
    """
    This function returns some mocked data.

    Returns:
    dict: A dictionary containing the mocked data
    """
    # Increment request count
    REQUEST_COUNT.labels(method='GET', endpoint='/data', http_status='200').inc()

    # Record request latency
    with REQUEST_LATENCY.labels(method='GET', endpoint='/data').time():
        # Mock data
        data = {'name': 'Hashem', 'age': 30, 'location': 'Dubai - UAE'}

        # Return data as JSON
        return jsonify(data)

if __name__ == '__main__':
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    

    # Create Prometheus middleware
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/v1/metrics': make_wsgi_app()
    })

    # Run app
    app.run(host='0.0.0.0', port=5000, debug=True)
