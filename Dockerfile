# Dockerfile

# Use Ubuntu 20.04 as the base image
FROM ubuntu:20.04

# Update packages and install Python 3 and pip
RUN apt-get update \
    && apt-get install -y \
        python3 \
        python3-pip \
    && python3 -m pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN cat requirements.txt  # Print contents of requirements.txt for debugging
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port if needed
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]
