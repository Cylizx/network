#!/usr/bin/env python3

import socket
import sys

from messages import *
from utils import receive
from wrapper import decode_from_bytes, wrap_message

if 'peers' not in sys.modules:
    import peers


class Sender:
    def __init__(self, peer):
        self.peer = peer
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def send_message(self, msg):
        if not self.connected:
            print('sender: try connect to %s' % str(self.peer))
            self.s.connect((self.peer.ip, self.peer.port))
            self.connected = True
            print('sender: connected to %s' % str(self.peer))

        print('sender: send %s to %s' % (str(msg), str(self.peer)))
        content = wrap_message(msg)
        self.s.send(content)
        content_length = int(receive(self.s, 10))
        return decode_from_bytes(receive(self.s, content_length))

    def __del__(self):
        self.s.close()


if __name__ == '__main__':
    sender = Sender(peers.Peer('127.0.0.1', 10086))
    print(sender.send_message(HeartbeatMessage()).timestamp)
    del sender
