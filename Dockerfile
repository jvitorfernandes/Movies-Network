# Multi-stage Dockerfile: build React app, then build Python runtime

# --- Build React ---
FROM node:18-alpine AS client-build
WORKDIR /app/client
COPY client/package.json client/package-lock.json* ./
RUN npm ci
COPY client/ .
RUN npm run build


# --- Python runtime ---
FROM python:3.12-slim

# Install system packages required by numpy/pandas and building wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    libatlas-base-dev \
    python3-dev \
    python3-distutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/server

# Copy and install python requirements
COPY server/requirements.txt ./requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy server source
COPY server/ .

# Copy client build into server (served by Flask)
COPY --from=client-build /app/client/build ./client_build

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:api", "--workers", "4"]
