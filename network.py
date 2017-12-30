#!/usr/bin/env python3

from network.peers import init_peers
from network.server import Server


def init():
    init_peers()
    server = Server()
    server.start_server()


def broadcast(obj):
    # TODO
    pass
