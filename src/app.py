from datetime import datetime
from typing import Callable

import gevent
from flask import Flask, make_response, redirect, request
from gevent import pywsgi, sleep
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket

app = Flask(__name__)

id = -1


@app.route("/ws")
def ws_app():
    if request.environ.get("wsgi.websocket"):
        ws = request.environ['wsgi.websocket']
        global id
        id = id + 1
        process(ws.send, id)
    return make_response()


# 呼び出し可能型; Callable[[int], str] は (int) -> str の関数です。

def process(printws: Callable[[str], None], id: int = -1):
    pre = f"process #{id}"
    printws(f"{pre} start process {now_str()}")

    for i in range(10):
        printws(f"{pre}-{i} now processing.. {now_str()}")
        sleep(1)

    printws(f"{pre} finish process  {now_str()}")


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


server = pywsgi.WSGIServer(("", 8000), app, handler_class=WebSocketHandler)

if __name__ == "__main__":
    server.serve_forever()
