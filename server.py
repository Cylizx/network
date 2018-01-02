#!/usr/bin/env python3

from socketserver import ThreadingTCPServer, BaseRequestHandler

import peers
from handle_message import handle_message
from messages import *
from utils import receive, get_local_ip
from wrapper import decode_from_bytes, wrap_message


class Server:
    def __init__(self, ip=get_local_ip(), port=10086):
        self.server = ThreadingTCPServer((ip, port), UniformRequestHandler)

    def start_server(self):
        self.server.serve_forever()


class UniformRequestHandler(BaseRequestHandler):
    def handle(self):
        while True:
            content_length = int(receive(self.request, 10))
            msg = decode_from_bytes(receive(self.request, content_length))
            print('new request')
            if isinstance(msg, HeartbeatMessage):
                print(msg.timestamp)
                self.request.send(wrap_message(HeartbeatMessage()))
            elif isinstance(msg, GetPeersMessage):
                self.request.send(wrap_message(PeersMessage(peers.get_known_peers())))
            elif isinstance(msg, PeersMessage):
                print('request is PeersMessage')
                for peer in msg.peers:
                    peers.add_peer_to_known_peers(peer)
            else:
                self.request.send(wrap_message(handle_message(msg)))


class TestClass:
    def __init__(self):
        self.a = 'a'

    pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
