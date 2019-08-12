# CNU2k19_sagar

1. docker build -t img .
2. sudo docker run --name my-redis-container -d redis
3. docker run -it --name my-redis-cli -p 80:5000 --env REDIS_HOST=redis --env REDIS_PORT=6379 --link my-redis-container:redis img

