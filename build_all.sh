#!/bin/bash

echo "Building StrokeCap Docker image..."
docker build -t strokecap ./stroke_cap

echo "\nBuilding ZeroStroke Docker image..."
docker build -t zerostroke ./zero_stroke

echo "\nAll Docker images built successfully!"
