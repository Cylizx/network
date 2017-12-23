#!/usr/bin/env python3

import time
from datetime import datetime


class HeartbeatMessage:
    def __init__(self, timestamp=datetime.now()):
        self.timestamp = timestamp


class GetBlocksMessage:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


class GetTxMessage:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


class GetHeadersMessage:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


class BlocksMessage:
    def __init__(self, blocks):
        self.blocks = blocks


class TxMessage:
    def __init__(self, tx):
        self.tx = tx


class HeadersMessage:
    def __init__(self, headers):
        self.headers = headers


class GetPeersMessage:
    def __init__(self, maximum=20):
        self.maximum = maximum


class PeersMessage:
    def __init__(self, peers):
        self.peers = peers


if __name__ == '__main__':
    a = datetime.now()
    time.sleep(5)
    b = datetime.now()
    print(a)
    print(b)
