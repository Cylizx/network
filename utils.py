#!/usr/bin/env python3


def receive(socket, target_length):
    now_target_length = target_length
    content = b''
    while now_target_length > 0:
        content_temp = socket.recv(now_target_length)
        now_target_length -= len(content_temp)
        content += content_temp
    return content


def get_local_ip():
    # TODO
    return '0.0.0.0'
