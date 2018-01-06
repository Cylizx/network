#!/usr/bin/env python3

verbose = 0
info = 1
running = 2
error = 3

debug_level = info


def output(level, content):
    if level >= debug_level:
        print(content)
