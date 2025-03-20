## Run a MySQL container with a named volume (mysql_data) and confirm data persistence after container restart.

1. Create Volume
```bash
docker volume create mysql_data
```

2. Create MySQL container using docker volume
```bash
docker container run -d --name mysql-container \
    -v mysql_data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=pass \
    -e MYSQL_DATABASE=mydb \
    -p 3306:3306 \
    mysql:latest
```

3. Create a table in MYSQL
```bash
docker exec -it mysql-container mysql -uroot -ppass -e "CREATE TABLE mydb.users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));"
```

4. Insert some sample data in MySQL table
```bash
docker exec -it mysql-container mysql -uroot -ppass -e "INSERT INTO mydb.users (name) VALUES ('Abhishek'), ('jain');"
```

5. Verify the data in MySQL table
```bash
docker exec -it mysql-container mysql -uroot -ppass -e "SELECT * FROM mydb.users;"
```

6. Stop and Remove the container
```bash
docker container stop mysql-container
docker rm mysql-container
```

7. Restart the container
```bash
docker container run -d --name mysql-container \
    -v mysql_data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=pass \
    -e MYSQL_DATABASE=mydb \
    -p 3306:3306 \
    mysql:latest
```

8. Verify whether the data still persists or not
```bash
docker container exec -it mysql-container mysql -uroot -ppass -e "SELECT * FROM mydb.users;"
```

If the data is still visible that means data is persisted using volumes.