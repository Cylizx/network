#!/usr/bin/env python3

from client import Sender
from peers import init_peers, get_known_peers
from server import Server


def init():
    init_peers()
    server = Server()
    server.start_server()


def broadcast(obj):
    for peer in get_known_peers():
        sender = Sender(peer)
        sender.send(obj)
