#!/usr/bin/env python3

import pickle


class TooLongMessage:
    pass


class MessageTypeNotSupported:
    pass


def message_wrap(serialization):
    if type(serialization) == str:
        content = bytes(serialization, 'utf-8')
    elif type(serialization) == bytes:
        content = serialization
    else:
        raise MessageTypeNotSupported
    content_length = len(content)
    if content_length >= 10 ** 9:
        raise TooLongMessage
    return bytes('%010d' % content_length, 'utf-8') + content


def wrap_message(msg):
    return message_wrap(pickle.dumps(msg))


def decode_from_bytes(serialization):
    return pickle.loads(serialization)


if __name__ == '__main__':
    class TestClass:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def output(self):
            print(str(self.a) + ' ' + str(self.b) + ' ' + str(self.c))


    test = TestClass(123, 'abc', [3, 2, 1])
    print(wrap_message('hello'))
