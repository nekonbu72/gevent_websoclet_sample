from geventwebsocket.websocket import WebSocket

from customout import CustomOutBase, end_filter


class WebSocketOut(CustomOutBase):
    def __init__(self, ws: WebSocket):
        super().__init__()
        self.ws = ws

    def __exit__(self, ex_type, ex_value, trace):
        # stdout は手動で元に戻す
        pass

    @end_filter
    def write(self, s: str) -> int:
        self.ws.send(s)
        return len(s)
