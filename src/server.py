import logging
import os
import sys

# Ensure imports work from the current directory structure
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastmcp import FastMCP
from tools.prometheus_metrics import get_p95_latency
from tools.k8s_operations import get_pod_status

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-sre-gateway")

# Initialize FastMCP without the dependencies argument
mcp = FastMCP("Fintech-SRE-Gateway")

# Register Tools
mcp.tool()(get_p95_latency)
mcp.tool()(get_pod_status)

if __name__ == "__main__":
    logger.info("Starting Agentic SRE Gateway...")
    mcp.run()
