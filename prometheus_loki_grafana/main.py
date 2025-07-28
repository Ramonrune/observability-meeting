from prometheus_client import start_http_server, Summary, Counter
import time
import random
import logging
import os

# Log path inside container
os.makedirs("/logs", exist_ok=True)
logging.basicConfig(
    filename="/logs/python_app.log",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)

# Metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
ERROR_COUNT = Counter('app_errors_total', 'Number of errors encountered')

@REQUEST_TIME.time()
def process_request():
    duration = random.random()
    time.sleep(duration)
    if duration > 0.8:
        logging.error("Slow processing")
        ERROR_COUNT.inc()
    else:
        logging.info("Request processed in %.2fs", duration)

if __name__ == "__main__":
    print("Starting Python app with metrics and logging...")
    start_http_server(8000)  # Prometheus will scrape here
    while True:
        process_request()
