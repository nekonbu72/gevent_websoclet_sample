from geventwebsocket.websocket import WebSocket

from customout import CustomOutBase, end_filter


class WebSocketOut(CustomOutBase):
    def __init__(self, ws: WebSocket, startID: int):
        super().__init__()
        self.ws = ws
        self.startID = startID
        self.latestID = startID

    def __exit__(self, ex_type, ex_value, trace):
        if self.latestID == self.startID:
            super().__exit__(ex_type, ex_value, trace)

    @end_filter
    def write(self, s: str) -> int:
        self.ws.send(s)
        return len(s)
