from datetime import datetime

from flask import Flask, make_response, request
from gevent import pywsgi, sleep
from geventwebsocket.handler import WebSocketHandler

from websocketout import WebSocketOut

app = Flask(__name__)

id = 0


@app.route("/ws")
def ws_app():
    if request.environ.get("wsgi.websocket"):
        ws = request.environ['wsgi.websocket']
        global id
        id += 1
        process(ws, id)
    return make_response()


@app.route("/reset")
def reset():
    global id
    id = 0
    return make_response("reset")


def process(ws, tmpID: int):
    with WebSocketOut(ws, tmpID) as ws:

        pre = f"process #{tmpID}"
        print(f"{pre} start process {now_str()}")

        sleep(1)
        for i in range(3):
            print(f"{pre}-{i+1} now processing.. {now_str()}")
            sleep(1)

        print(f"{pre} finish process  {now_str()}")
        global id
        ws.latestID = id

    if id == tmpID:
        print("no process exists")


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


server = pywsgi.WSGIServer(("", 8000), app, handler_class=WebSocketHandler)

if __name__ == "__main__":
    server.serve_forever()
    # localhost:8000/static/index.html
