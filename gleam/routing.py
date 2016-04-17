# coding=utf-8
from channels.routing import route
from chat.consumers import ws_message, ws_connect, ws_disconnect, msg_consumer

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", msg_consumer),
    route("websocket.disconnect", ws_disconnect),
]
