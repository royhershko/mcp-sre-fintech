FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Default environment variables
ENV PROMETHEUS_URL="http://prometheus-server.monitoring.svc.cluster.local"
ENV PYTHONUNBUFFERED=1

# Run the server via stdio
CMD ["python", "src/server.py"]
