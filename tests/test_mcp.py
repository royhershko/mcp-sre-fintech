import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tools.prometheus_metrics import get_p95_latency

print("--- Testing Prometheus Tool (Mock) ---")
# This will fail gracefully if no Prometheus is found, but tests the logic
result = get_p95_latency("trading-service")
print(result)
