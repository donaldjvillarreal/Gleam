# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/routing.py
"""
from channels.staticfiles import StaticFilesConsumer
from consumers import ws_connect, ws_disconnect, ws_receive

websocket_routing = {

    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    'http.request': StaticFilesConsumer(),

    # Wire up websocket channels to our consumers:
    'websocket.connect': ws_connect,
    'websocket.receive': ws_receive,
    'websocket.disconnect': ws_disconnect,
}
