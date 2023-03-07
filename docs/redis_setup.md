# Basic setup

I'm using the Redis container image from bitname, just because I heard good things about it and I would like to try it for myself.
Other images are availabe. 

Pull the image and run it with Podman

```
podman pull bitnami/redis
podman run -e ALLOW_EMPTY_PASSWORD=yes -p 6379:6379 bitnami/redis
```

or do the same with docker

```
docker pull bitnami/redis
docker run -e ALLOW_EMPTY_PASSWORD=yes -p 6379:6379 bitnami/redis
```

