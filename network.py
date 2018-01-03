#!/usr/bin/env python3

import client
import peers
from server import Server


def init(port=10086):
    peers.init_peers(port)
    server = Server(port=port)
    server.start_server()


def broadcast_message(msg):
    for peer in list(peers.get_known_peers()):
        if peer != peers.get_local_peer():
            print('broadcast: send %s to ' % str(type(msg)) + str(peer))
            sender = client.Sender(peer)
            sender.send_message(msg)
            print('broadcast: sent %s to ' % str(type(msg)) + str(peer))
            del sender
            print('close connection to ' + str(peer))


if __name__ == '__main__':
    init(10090)
