# Dockerfile Example

Write a simple Dockerfile that runs a Python Flask app serving an HTML page using an official base image (`python:3.9`).

Note: Same application can be created on (`python:3.9-slim`) image as well and it will drastically reduce the size.

## Build the Docker Image

Build a Docker image from your Dockerfile and tag it with a version:

```bash
docker build -t flask .
```
## Run the container

Run a container from your custom image, map necessary ports, and test the app.

```bash
docker container run -d -p 8080:5000 flask:latest
```

## Access the static page

To access the static HTML page

```bash
curl localhost:8080
```
## Publish the image

Push your custom Docker image to Docker Hub.

Enter your Docker Hub username and password when prompted.
```bash
docker login
```

Tag the Image for Docker Hub
```bash
docker tag flask:v1 abhishek5779/flask:v1
```

Push the Image to Docker Hub
```bash
docker push abhishek5779/flask:v1
```