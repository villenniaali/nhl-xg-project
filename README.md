
# NHL XG Project

This project retrieves and analyzes NHL play-by-play data to calculate expected goals (xG) for each shot event.

## Overview

The NHL XG Project fetches play-by-play data from the NHL API, processes shot events (goals, shots on goal, missed shots), calculates xG values, and provides insights into team performance based on shot locations and types.

## Requirements

- Python 3.9+
- Flask
- Requests
- Pandas

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/nhl-xg-project.git
   cd nhl-xg-project
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

To run the project locally:

```bash
python app.py
```

The application will start locally and can be accessed at `http://localhost:5000`.

### Docker

#### Building the Docker Image

To build the Docker image using the provided Dockerfile:

```bash
docker build -t nhl-xg-project .
```

##### Explanation of Dockerfile

The Dockerfile sets up the environment for running the NHL XG Project in a Docker container using Ubuntu 20.04:

```dockerfile
# Dockerfile

# Use Ubuntu 20.04 as the base image
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
```

#### Running the Docker Container

Once the Docker image is built, you can run the container with:

```bash
docker run -p 5000:5000 nhl-xg-project
```

The application will be accessible at `http://localhost:5000`.

## Project Structure

- `app.py`: Flask application to fetch and analyze NHL play-by-play data.
- `requirements.txt`: List of Python dependencies.
- `nhl_teams.json`: JSON file containing NHL team data.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any enhancements, bug fixes, or new features.

## Issues

If you encounter any issues or have suggestions, please [create an issue](https://github.com/villenniaali/nhl-xg-project/issues) on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
