# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for Python and Google Cloud SDK
ENV PYTHONUNBUFFERED=1 \
    CLOUDSDK_CORE_DISABLE_PROMPTS=1 \
    PATH="/opt/google-cloud-sdk/bin:$PATH"

# Install necessary packages
RUN apt-get update && yes | apt-get install gsutil

# Install Python packages using pip
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Copy your application code into the image
COPY . /app

# Set the working directory
WORKDIR /app

# Default command to run when the container starts
CMD ["pytest", "test_example.py","-s"]
