# coding=utf-8
"""
https://github.com/jacobian/channels-example/blob/master/chat/routing.py
"""

# websocket_routing = [
#
#     # This makes Django serve static files from settings.STATIC_URL, similar
#     # to django.views.static.serve. This isn't ideal (not exactly production
#     # quality) but it works for a minimal example.
#     'http.request': StaticFilesConsumer(),
#
#     # Wire up websocket channels to our consumers:
#     'websocket.connect': ws_connect,
#     'websocket.receive': ws_receive,
#     'websocket.disconnect': ws_disconnect,
#
#      include("chat.routing.custom_routing"),
# }


from channels import route
from consumers import ws_connect, ws_receive, ws_disconnect, chat_join, chat_leave, chat_send

websocket_routing = [
    # Called when WebSockets connect
    route("websocket.connect", ws_connect),

    # Called when WebSockets get sent a data frame
    route("websocket.receive", ws_receive),

    # Called when WebSockets disconnect
    route("websocket.disconnect", ws_disconnect),
]

custom_routing = [
    route("chat.receive", chat_join, command="^join$"),
    route("chat.receive", chat_leave, command="^leave$"),
    route("chat.receive", chat_send, command="^send$"),
]
