#!/usr/bin/env python3

from client import Sender
from messages import GetPeersMessage
from utils import get_local_ip


class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port


known_peers = set()
known_peers.add(
    Peer('127.0.0.1', 10086)
)


def get_known_peers():
    return known_peers


def init_peers(port):
    known_peers.add(Peer(get_local_ip(), port))
    find_peer()


def find_peer():
    global known_peers
    for peer in get_known_peers():
        sender = Sender(peer)
        peers_message = sender.send(GetPeersMessage())
        for new_peer in peers_message.peers:
            known_peers.add(new_peer)


if __name__ == '__main__':
    exit()
