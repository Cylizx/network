#!/usr/bin/env python3

from network.client import Sender
from network.peers import init_peers, get_known_peers
from network.server import Server


def init(port=10086):
    init_peers(port)
    server = Server(port=port)
    server.start_server()


def broadcast(obj):
    for peer in get_known_peers():
        sender = Sender(peer)
        sender.send(obj)
