import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Fintech-SRE-Gateway")

# Set Prometheus URL (using a placeholder for testing)
PROMETHEUS_URL = os.getenv("PROMETHEUS_URL", "http://localhost:9090")

@mcp.tool()
def get_p95_latency(service_name: str) -> str:
    """
    Queries Prometheus for the p95 latency of a specific microservice.
    Args:
        service_name: The name of the service to check (e.g., 'order-service')
    """
    query = f'histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{{job="{service_name}"}}[5m])) by (le))'
    
    try:
        # In a real scenario, this hits the Prometheus API
        response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query}, timeout=2)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'success' and data['data']['result']:
            value = float(data['data']['result'][0]['value'][1])
            return f"Service {service_name} p95 Latency: {value:.4f}s"
        return f"No metrics found for {service_name}."
    except Exception as e:
        return f"Diagnostic: Could not connect to Prometheus at {PROMETHEUS_URL}. (Expected in local test)"

if __name__ == "__main__":
    mcp.run()
