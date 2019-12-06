## Responder version of the previous example

[responder](https://responder.readthedocs.io/en/latest/),
 version of Flask application from [previous example](./../5mins/).

Build with:
```
docker build -t 5mins-responder .
```

And run with:
```
docker run -p 5042:5042 5mins-responder
```
If you like ```KeybordInterrupt``` support, start with
```
docker run -p 5042:5042 -it 5mins-responder
```
Browse to:

- [localhost:5042](localhost:5042)
- [localhost:5042/hello/datachampion](localhost:5042/hello/datachampion)
- [localhost:5042/hello/whoever](localhost:5042/hello/whoever)
- [localhost:5042/add/19/23](localhost:5042/add/19/23)
- [localhost:5042/hello/kpn/json](localhost:5042/hello/kpn/json)
- [localhost:5042/pizza](localhost:5042/pizza)

Review ```index.py``` for the functions these endpoints route to.

Really curious about the ```x-pizza``` header? 
```
curl -v localhost:5042/pizza
```

## Different ways to start the container

### Start container with a shell session
```
docker run -p 5042:5042 -it 5mins-responder /bin/sh
```

### Start a shell session into a running container
```
docker exec -it CONTAINER_ID /bin/sh 
```
you need to lookup CONTAINER_ID with ```docker ps```.

### Start the container 
```
docker run -d -p 5042:5042 5mins-responder
```

## Async what?

A bit of [background](https://en.wikipedia.org/wiki/Async/await#In_Python).

Exploring ```incoming``` route in ```index.py```.
```py
@api.route("/incoming")
async def receive_incoming(req, resp):

    @api.background.task
    def process_data(data):
        """Wait for a while and append incoming data to file"""
        with open('incoming.txt', 'a') as file:
            file.write(datetime.datetime.now().strftime('%H:%M:%S'))
            file.write(json.dumps(data))
            file.write('\n')
        time.sleep(30)
        with open('incoming.txt', 'a') as file:
            file.write(datetime.datetime.now().strftime('%H:%M:%S'))
            file.write(json.dumps(data))
            file.write('\n')
        
    # Parse the incoming data as form-encoded.
    # Note: 'json' and 'yaml' formats are also automatically supported.
    data = await req.media()

    # Process the data (in the background).
    process_data(data)

    # Immediately respond that upload was successful.
    resp.media = {'success': True,
                'timestamp': datetime.datetime.now().strftime('%H:%M:%S')}
```
```process_data()``` will write the json to the file, wait for 30 seconds and write the json to the file again.

Start multiple terminal sessions:
- __Session 1:__ This session is to output responder application. Start the container in attached mode:
  ```
  docker run -p 5042:5042 -it 5mins-responder
  ```
- __Session 2:__ A shell session in the container to see the contents of the ```incoming.txt```
  - Get the ```CONTAINER_ID``` from ```docker ps```
    ```
    docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
    b167297b7ce0        5mins-responder     "/bin/sh -c 'python …"   About a minute ago   Up About a minute   0.0.0.0:5042->5042/tcp   epic_hoover
    ```
  - Start a shell session in the container:
    ```
    docker exec -it b167 /bin/sh
    ```
  - See the files under ```app/``` folder:
    ```
    ls -ltr
    ```
  - ```incoming.txt``` is not available yet. It will be created after the first call from another session.
  - Once you are in the container:
    ```
    more incoming.txt
    ```
    ```
    tail -f incoming.txt
    ```

- __Session 3:__
  ```POST``` some data to ```localhost:5042/incoming``` endpoint
  ```
  curl --verbose --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"session3", "order":"first json"}' \
  localhost:5042/incoming
  ```
  ```incoming.txt``` should be available now, you can start watching the file in __Session 2__.
  ```
  curl --verbose --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"session3", "order":"second json"}' \
  localhost:5042/incoming
  ```

  ```
  curl --verbose --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"session3", "order":"third json"}' \
  localhost:5042/incoming
  ```
Data is processed in the background task, yet the API already responded to the request with {"success": true}. The subroutine will run the processes/tasks in the background.

### Signal Handling


A simple signal handling example will let you kill an attached running container.