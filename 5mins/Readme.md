### Containerize your python app in 5 mins

Following super simple [example](https://www.wintellect.com/containerize-python-app-5-minutes/).

#### Build image
```
docker build --tag 5mins .
```

Now that the image is built, check out available images:
```
docker images
```
But there are no containers running yet.
```
docker ps
```

### Run the image
```
docker run --name containerin5mins -p 5000:5000 5mins
```

Now the container is running, checkout ```localhost:5000``` from browser.

List the running containers again to see it's running. 
```
docker ps
```
```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
c89cf9233c5f        5mins               "/bin/sh -c 'python …"   5 minutes ago       Up 5 minutes        0.0.0.0:5000->5000/tcp   5mins
```

If you have seen "Hello world!", all is working, great, but did you see the output:
```
 * Serving Flask app "index" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
```

You can kill the docker image by container_id (first 4 characters are enough, for the example above):
```
docker kill c89c
```
Head on googling more on WSGI, ASGI... until you end up finding about ```responder``` or ```uwsgi-nginx``` server deployment schemes.