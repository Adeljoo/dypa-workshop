# Quick start with responder
# https://github.com/taoufik07/responder/blob/master/docs/source/quickstart.rst

import responder
import time
import json
import datetime
import signal

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"

@api.route("/hello/{who}")
def hello_to(req, resp, *, who):
    resp.text = f"hello, {who}!"

@api.route("/add/{a:int}/{b:int}")
async def add(req, resp, *, a, b):
    resp.text = f"{a} + {b} = {a + b}"

@api.route("/hello/{who}/json")
def hello_to(req, resp, *, who):
    resp.media = {"hello": who}

@api.route("/pizza")
def pizza_pizza(req, resp):
    resp.headers['X-Pizza'] = '42'

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

if __name__ == "__main__":
    api.run(address="0.0.0.0", port=5042, debug=True)