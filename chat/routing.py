# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/routing.py
"""
from consumers import ws_connect, ws_disconnect, ws_receive

websocket_routing = {
    # Wire up websocket channels to our consumers:
    'websocket.connect': ws_connect,
    'websocket.receive': ws_receive,
    'websocket.disconnect': ws_disconnect,
}
