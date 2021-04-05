# Basic setup

I'm using the Redis container image from bitname, just because I heard good things about it and I would like to try it for myself.
Other images are availabe. 

Pull the image and run it with Podman

```
podman pull bitnami/redis
podman run -e ALLOW_EMPTY_PASSWORD=yes  bitnami/redis
```