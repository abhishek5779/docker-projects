# Flask API with PostgreSQL using Docker Compose

Create a `docker-compose.yml` file to launch a Flask API and a PostgreSQL database together.

- Implement environment variables in your Docker Compose file to configure database credentials securely.
- Implement container health checks in Docker Compose (`healthcheck:` section).

## Build and Run the Containers

To build and run the containers via Docker Compose:

```bash
docker compose up -d --build
```

Check if the Flask API is running
```bash
curl http://localhost:5000
```
