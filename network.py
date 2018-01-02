#!/usr/bin/env python3

import sys

from server import Server

if 'client' not in sys.modules:
    import client

if 'peers' not in sys.modules:
    import peers


def init(port=10086):
    peers.init_peers(port)
    server = Server(port=port)
    server.start_server()


def broadcast(obj):
    for peer in peers.get_known_peers():
        sender = client.Sender(peer)
        sender.send(obj)


if __name__ == '__main__':
    init(10086)
