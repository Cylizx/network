#!/usr/bin/env python3

verbose = 0
info = 1
running = 2
error = 3

debug_mode = running


def output(scope, content):
    if scope >= debug_mode:
        print(content)
