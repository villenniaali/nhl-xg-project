# Dockerfile

# Use Ubuntu as the base image
FROM ubuntu:20.04

# Update packages and install Python 3 and pip
RUN apt-get update \
    && apt-get install -y \
        python3 \
        python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port if needed
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]

##
