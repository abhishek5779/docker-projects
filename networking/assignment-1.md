## Create a custom bridge network and connect two containers (alpine and nginx).

1. Create a custom network- 
```bash
docker network create mynetwork
```
2. Create a Nginx container
```bash
docker container run -d --name nginx --network mynetwork nginx:latest
```

3. Create a Alpine container and get inside of it 
```bash
docker container run -it --name alpine --network mynetwork alpine:latest
```

4. Download curl package in alpine container and connect with Nginx container
```bash
apk add --no-cache curl
curl nginx
```

Here above we have used the container name while performing curl command, you would also need to provide the port if your container is listening on any other port than 80.

If your containers are running fine and connected well to the custom network, you would be able to see the Nginx default custom page.