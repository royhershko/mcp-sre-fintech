import os
import requests

PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://localhost:9090")

def get_p95_latency(service_name: str):
    """
    Queries Prometheus for the p95 latency of a specific microservice.
    Used for diagnosing performance bottlenecks.
    """
    query = f'histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{{job="{service_name}"}}[5m])) by (le))'
    try:
        response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query}, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'success' and data['data']['result']:
            value = float(data['data']['result'][0]['value'][1])
            return f"Service {service_name} p95 Latency: {value:.4f}s"
        return f"No metrics found for {service_name}."
    except Exception as e:
        return f"Prometheus Query Error: {str(e)}"
