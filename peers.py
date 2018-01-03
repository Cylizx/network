#!/usr/bin/env python3

import client
import debug
import messages
import network
from utils import get_local_ip


class Peer:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __str__(self):
        return self.ip + ':' + str(self.port)

    def __eq__(self, other):
        return self.ip == other.ip and self.port == other.port

    def __hash__(self):
        return self.ip.__hash__() * 65536 + self.port


known_peers = set()
known_peers.add(
    Peer('127.0.0.1', 10086)
)

local_peer = Peer(get_local_ip(), 10086)


def get_local_peer():
    return local_peer


def add_peer(peer):
    if peer not in known_peers:
        debug.output(debug.info, '[add_peer] new peer: ' + str(peer))
        known_peers.add(peer)


def get_known_peers():
    return known_peers


def init_peers(port):
    global local_peer
    local_peer = Peer(get_local_ip(), port)
    add_peer(local_peer)
    debug.output(debug.info, '[init_peers] start to look for peers')
    find_peers()
    debug.output(debug.info, '[init_peers] look for peers ended')
    debug.output(debug.info, '[init_peers] broadcast known peers')
    network.broadcast_message(messages.PeersMessage(get_known_peers()))
    debug.output(debug.info, '[init_peers] broadcasted known peers')


def find_peers():
    global known_peers
    for peer in list(known_peers):
        if peer == get_local_peer():
            continue
        debug.output(debug.info, '[find_peers] send GetPeersMessage to ' + str(peer))
        sender = client.Sender(peer)
        peers_message = sender.send_message(messages.GetPeersMessage())
        debug.output(debug.info, '[find_peers] sent GetPeersMessage to ' + str(peer))
        for new_peer in peers_message.peers:
            add_peer(new_peer)
        del sender
        debug.output(debug.info, '[find_peers] close connection to ' + str(peer))


if __name__ == '__main__':
    exit()
