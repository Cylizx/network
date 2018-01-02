#!/usr/bin/env python3

import client
import peers
from server import Server


def init(port=10086):
    peers.init_peers(port)
    server = Server(port=port)
    server.start_server()


def broadcast_message(msg):
    for peer in peers.get_known_peers():
        if peer != peers.get_local_peer():
            sender = client.Sender(peer)
            sender.send_message(msg)


if __name__ == '__main__':
    init(10088)
