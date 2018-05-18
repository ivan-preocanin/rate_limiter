from flask import Flask, request, make_response
import time

app = Flask(__name__)

clients = {}

@app.route('/')
def index():
    return 'INDEX'

@app.route('/greet/<string:name>/')
def greet(name):

    address = request.remote_addr

    request_limit = 10   # number of requests
    interval = 60        # per X seconds

    if address not in clients or time.time() > clients[address]['expires']:
        clients[address] = {
            'expires' : time.time() + interval,
            'remaining' : request_limit
        }

    if time.time() <= clients[address]['expires']:
        if clients[address]['remaining'] > 0:
            clients[address]['remaining'] -= 1  
        else:
            return 'You hit the rate limit', 429              

    response = make_response("Hi, {0}!".format(name))
    response.headers['X-RateLimit-Limit'] = request_limit
    response.headers['X-RateLimit-Remaining'] = clients[address]['remaining']
    
    return response


if __name__ == '__main__':
    app.run(debug=True)