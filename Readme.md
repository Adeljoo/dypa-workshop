## DYPA Workshop

__at Data Champions Day 2019 - December edition__

by _KPN Data & Analytics + KPN Consulting_

_13.00 - 15.30 Hands-on/Deep dive workshops_

### Docker workshop - Containerize your python application

In this workshop, we will containerize a python application to run as a standalone RESTful service. We will start from scratch with a piece of python code, dockerize the application with an HTTP framework (responder), and run the service as a docker container. Thus, we will end-up with an API that is ready to deploy as a microservice. This workshop will provide insights to building and deploying micro-services and bring you up-to-speed creating dockerized python applications within 5 minutes in the future.

No prior docker knowledge is needed. But installing docker on your system, and bringing along your favorite python scripts would speed-up the process ([suggested setup on Win10: wsl, docker and VSCode](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4)).

## Agenda

* Welcome and introduction round (~ 10 mins)
* A short overview (~ 10-15 mins)
* Hands-on (~ 1.0-1.5 hours)
* Wrap-up (~ 10 mins)

## Background

Why?

Enough examples on the internet [1](https://medium.com/google-cloud/how-to-convert-a-simple-python-application-to-a-containerized-docker-one-d6103bfffc7b), [2](https://medium.com/faun/getting-started-with-docker-using-python-flask-application-b6dcd1a08626), [3](https://runnable.com/docker/python/dockerize-your-python-application), [4](https://www.wintellect.com/containerize-python-app-5-minutes/), [5](https://dev.to/riverfount/dockerize-a-flask-app-17ag), [6](https://stackabuse.com/dockerizing-python-applications/) [etc...](https://www.google.com/search?q=containerize+your+python+application)

## Docker

### [Documentation](https://docs.docker.com/)

### [Docker Hub](https://hub.docker.com/)

### [Docker get started](https://docs.docker.com/get-started/)

## Python apps

### 5mins

Flask app, alpine based, pip install 

### 5mins-responder

Responder app, alpine based, pip install, signal handling added
https://geekflare.com/python-asynchronous-web-frameworks/

### More challenges

* [alpine base image, conda package manager and jupyter notebook](https://github.com/bkasap/alpine-miniconda) 

* [docker-compose - camera-app](https://github.com/bkasap/camera-app)

* [tensorflow2-yolov3](https://github.com/bkasap/TensorFlow2.0-Examples/tree/master/4-Object_Detection/YOLOV3)
  
* ...