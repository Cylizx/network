#!/usr/bin/env python3

from socketserver import ThreadingTCPServer, BaseRequestHandler

import network.peers
from network.handle_message import handle_message
from network.messages import *
from network.utils import receive, get_local_ip
from network.wrapper import decode_from_bytes, object_to_message


class Server:
    def __init__(self, ip=get_local_ip(), port=10086):
        self.server = ThreadingTCPServer((ip, port), UniformRequestHandler)

    def start_server(self):
        self.server.serve_forever()


class UniformRequestHandler(BaseRequestHandler):
    def handle(self):
        while True:
            content_length = int(receive(self.request, 10))
            obj = decode_from_bytes(receive(self.request, content_length))
            print('new request')
            if isinstance(obj, HeartbeatMessage):
                print(obj.timestamp)
                self.request.send(object_to_message(HeartbeatMessage()))
            elif isinstance(obj, GetPeersMessage):
                self.request.send(object_to_message(PeersMessage(peers.get_known_peers())))
            elif isinstance(obj, PeersMessage):
                print('request is PeersMessage')
                for peer in obj.peers:
                    peers.add_peer_to_known_peers(peer)
            else:
                handle_message(obj)


class TestClass:
    def __init__(self):
        self.a = 'a'

    pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
