# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Update package lists and install the procps package for the 'ps' command
RUN apt-get update && apt-get install -y procps

# Define the command to run your application
CMD ["python", "ZeroStroke.py"]
