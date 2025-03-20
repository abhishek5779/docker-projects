## Run a MySQL container with a named volume (mysql_data) and confirm data persistence after container restart.

1. Create Volume
```bash
docker volume create mysql_data
```
2. Create MySQL container using docker volume
```bash
docker container run -d --name mysql \
    -v mysql_data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=mysql \
    -e MYSQL_DATABASE=mydb \
    -p 3306:3306 \
    mysql:latest
```