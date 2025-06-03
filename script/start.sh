#!/bin/bash

echo "Starting Docker containers..."
docker-compose up --build -d
echo "Containers started!"
echo "Access Python API at http://localhost:8080/random"
echo "Access Prometheus at http://localhost:9090"
echo "Access Grafana at http://localhost:3000 or http://localhost:8080/grafana"