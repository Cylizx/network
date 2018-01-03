#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

import client
import debug
import peers
from server import Server


def init(port=10086, sync=True):
    peers.init_peers(port)
    if sync:
        start_server_sync()
    else:
        pool = ThreadPoolExecutor(1)
        pool.submit(start_server_sync)


def start_server_sync():
    server = Server(peers.get_local_peer().ip, peers.get_local_peer().port)
    server.start_server()


def broadcast_message(msg):
    for peer in list(peers.get_known_peers()):
        if peer != peers.get_local_peer():
            debug.output(debug.info, '[broadcast] send %s to ' % str(type(msg)) + str(peer))
            sender = client.Sender(peer)
            sender.send_message(msg)
            debug.output(debug.info, '[broadcast] sent %s to ' % str(type(msg)) + str(peer))
            del sender
            debug.output(debug.info, '[broadcast] close connection to ' + str(peer))


if __name__ == '__main__':
    init(10089)
