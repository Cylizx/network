#!/usr/bin/env python3

verbose = 0
info = 1
error = 2

debug_mode = info


def output(scope, content):
    if scope >= debug_mode:
        print(content)
