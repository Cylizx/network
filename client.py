#!/usr/bin/env python3

import socket
import sys

from network.messages import *
from network.utils import receive
from network.wrapper import decode_from_bytes, object_to_message

if 'peers' not in sys.modules:
    import peers


class Sender:
    def __init__(self, peer):
        self.peer = peer
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def send(self, obj):
        if not self.connected:
            self.s.connect((self.peer.ip, self.peer.port))
            self.connected = True

        content = object_to_message(obj)
        self.s.send(content)
        content_length = int(receive(self.s, 10))
        return decode_from_bytes(receive(self.s, content_length))

    def __del__(self):
        self.s.close()


if __name__ == '__main__':
    sender = Sender(peers.Peer('127.0.0.1', 10086))
    print(sender.send(HeartbeatMessage()).timestamp)
