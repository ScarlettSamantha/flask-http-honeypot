# Flask Honeypot

This is a simple Flask application that logs all incoming requests and blocks any IP that tries to access a suspicious URL. The blocked IPs and request logs are stored in a SQLite database.

## Installation

### Docker

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Run the Docker container:

    ```bash
    docker-compose up
    ```

The application will be available at `http://localhost:8000`.

### Native

1. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:

    ```bash
    gunicorn main:app -b 0.0.0.0:8000
    ```

The application will be available at `http://localhost:8000`.

## Usage

The application will log all incoming requests and block any IP that tries to access a suspicious URL. The blocked IPs and request logs are stored in a SQLite database. You can unban an IP address using the `flask unban` command.

## License

This project is licensed under the MIT License.