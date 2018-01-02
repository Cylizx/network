#!/usr/bin/env python3

from network.messages import *
from pow.fullnode import *
from pow.pow import *
import json
def handle_message(obj):
    # TODO: jas0n1ee
    # receive an message object
    # return an object as a response
        if isinstance(obj,BlocksMessage):
            block_hash = save_block(obj.blocks[0])
            save_block_transaction_info(block_hash,obj.blocks[1])
            Fullnode.restart_mining(block_hash)

        elif isinstance(obj,TxMessage):
            Fullnode.add_transaction(obj.tx)

    return
