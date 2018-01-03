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
        print('server: new connection from ' + str(self.client_address))
        content_length = int(receive(self.request, 10))
        msg = decode_from_bytes(receive(self.request, content_length))
        if isinstance(msg, HeartbeatMessage):
            print(msg.timestamp)
            self.request.send(wrap_message(HeartbeatMessage()))
        elif isinstance(msg, GetPeersMessage):
            print('server: receive %s from ' % str(type(msg)) + str(self.client_address))
            print('server: send to ' + str(self.client_address))
            self.request.send(wrap_message(PeersMessage(peers.get_known_peers())))
            print('server: sent to ' + str(self.client_address))
        elif isinstance(msg, PeersMessage):
            print('server: receive %s from ' % str(type(msg)) + str(self.client_address))
            for peer in msg.peers:
                peers.add_peer_to_known_peers(peer)
            self.request.send(wrap_message(HeartbeatMessage()))
        else:
            handle_message(msg)
            self.request.send(wrap_message(HeartbeatMessage()))
        print('server: exit handle')


class TestClass:
    def __init__(self):
        self.a = 'a'

    pass


if __name__ == '__main__':
    server = Server()
    server.start_server()
