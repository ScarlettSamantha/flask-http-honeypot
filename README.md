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

### Docker Networking

In the `docker-compose.yml` file, we have set `network_mode: host`. This configuration is necessary for the application to interact with the host's network stack directly.

The main reason we need this is because our application has a feature that interacts with the host's IP tables to block certain IP addresses. IP tables is a user-space utility program that allows a system administrator to configure the IP packet filter rules of the Linux kernel firewall, implemented as different Netfilter modules. 

When a Docker container runs in host network mode, it has the same network access as the host machine. This means the container can listen on any of the host's network interfaces, and it can access network services running on the host or on other containers. In our case, this allows the application to access and modify the host's IP tables.

However, please note that running a Docker container in host network mode can be a security risk, because it gives the container full access to the host's network interfaces and services. Therefore, you should only use this mode if you trust the application running in the container, and you should secure the application and the host machine as much as possible to prevent unauthorized access.

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