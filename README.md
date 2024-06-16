
# Dockerized NHL Expected Goals (xG) Project

This project dockerizes a Flask application that analyzes NHL play-by-play data to calculate expected goals (xG) based on shot events during games.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [Usage](#usage)
- [Built With](#built-with)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

This project dockerizes a Flask application that retrieves NHL game data from the NHL API and processes shot events to calculate expected goals (xG). The Docker container encapsulates all dependencies and environment configurations, making it easy to deploy and run the application consistently across different environments.

## Setup

Follow these steps to set up and run the Dockerized application.

### Prerequisites

- Docker installed on your system ([Install Docker](https://docs.docker.com/get-docker/))

### Building the Docker Image

1. **Clone the repository:**

   ```bash
   git clone https://github.com/villenniaali/nhl-xg-project.git
   cd nhl-xg-project
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t nhl-xg-project .
   ```

   This command builds a Docker image named `nhl-xg-project` based on the `Dockerfile` in the project directory.

### Running the Docker Container

1. **Run the Docker container:**

   ```bash
   docker run -p 5000:5000 nhl-xg-project
   ```

   This command starts a Docker container based on the `nhl-xg-project` image, exposing port 5000 for the Flask application.

2. **Access the application:**

   Open your web browser and navigate to http://localhost:5000 to view the application.

## Usage

- Enter a valid NHL game ID to retrieve play-by-play data.
- View shot events (goals, shots on goal, missed shots) with additional details such as coordinates and time since the last event.

## Built With

- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [Requests](https://docs.python-requests.org/) - HTTP requests handling
- [Docker](https://www.docker.com/) - Containerization platform

## Authors

- [Ville Sainio](https://github.com/villenniaali) - Initial work

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- NHL API for providing game data
- OpenAI for providing guidance on project structure
