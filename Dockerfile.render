# Render.com Optimized Deployment Dockerfile for Hermes Agent API Server
FROM python:3.12-slim

WORKDIR /app

# Install minimal OS dependencies needed for Python packages and git
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv for high-speed package resolution
RUN pip install --no-cache-dir uv

# Copy requirements first for Docker cache optimization
COPY requirements.txt /app/requirements.txt

# Explicitly install all core requirements into Python environment
RUN uv pip install --system -r /app/requirements.txt

# Copy project files
COPY . /app

# Install hermes-agent in editable mode without re-resolving dependencies
RUN uv pip install --system --no-deps -e .

# Environment configuration for Render deployment
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV API_SERVER_HOST=0.0.0.0
ENV API_SERVER_PORT=10000
ENV PORT=10000
ENV PYTHONPATH=/app

EXPOSE 10000

# Start the Hermes Gateway API Server via Render-aware entrypoint
CMD ["python", "entrypoint.py"]
