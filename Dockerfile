# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies (if needed - StrokeCap doesn't have any external ones)
# For ZeroStroke, if you plan to add dependencies later, you can uncomment this line
# RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your application
CMD ["python", "StrokeCap.py"]
