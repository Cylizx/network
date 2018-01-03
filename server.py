#!/usr/bin/env python3

from socketserver import ThreadingTCPServer, BaseRequestHandler

import debug
import peers
from handle_message import handle_message
from messages import *
from utils import receive
from wrapper import decode_from_bytes, wrap_message


class Server:
    def __init__(self, ip, port):
        self.server = ThreadingTCPServer((ip, port), UniformRequestHandler)

    def start_server(self):
        self.server.serve_forever()


class UniformRequestHandler(BaseRequestHandler):
    def handle(self):
        debug.output(debug.info, '[server] new connection from ' + str(self.client_address))
        content_length = int(receive(self.request, 10))
        msg = decode_from_bytes(receive(self.request, content_length))
        if isinstance(msg, HeartbeatMessage):
            debug.output(debug.info, msg.timestamp)
            self.request.send(wrap_message(HeartbeatMessage()))
        elif isinstance(msg, GetPeersMessage):
            debug.output(debug.info, '[server] receive %s from ' % str(type(msg)) + str(self.client_address))
            debug.output(debug.info, '[server] send to ' + str(self.client_address))
            self.request.send(wrap_message(PeersMessage(peers.get_known_peers())))
            debug.output(debug.info, '[server] sent to ' + str(self.client_address))
        elif isinstance(msg, PeersMessage):
            debug.output(debug.info, '[server] receive %s from ' % str(type(msg)) + str(self.client_address))
            for peer in msg.peers:
                peers.add_peer(peer)
            self.request.send(wrap_message(HeartbeatMessage()))
        else:
            handle_message(msg)
            self.request.send(wrap_message(HeartbeatMessage()))
        debug.output(debug.info, '[server] exit handle')


class TestClass:
    def __init__(self):
        self.a = 'a'

    pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
