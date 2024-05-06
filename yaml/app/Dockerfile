# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py /app

# Install Flask
RUN pip install Flask

# Command to run the Python script
CMD ["python", "app.py"]
