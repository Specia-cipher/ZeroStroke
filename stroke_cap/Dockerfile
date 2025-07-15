# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Replace the default sources.list with a mirror in South Africa
RUN rm /etc/apt/sources.list
RUN echo "deb http://mirror.za.datapacket.com/debian/ bullseye main contrib non-free" > /etc/apt/sources.list
RUN echo "deb-src http://mirror.za.datapacket.com/debian/ bullseye main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://mirror.za.datapacket.com/debian/ bullseye-updates main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://security.debian.org/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list

# Update package lists and install build essentials and kernel headers
RUN apt-get update && apt-get install -y build-essential linux-headers-generic

# Install dependencies
RUN pip install --no-cache-dir pynput

# Define the command to run your application
CMD ["python", "StrokeCap.py"]
