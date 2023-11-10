from pyblock.blockchain.account import Accounts
from pyblock.config import START_TIME, BLOCK_VALIDATOR_CHOOSE_INTERVAL
from pyblock.peers import PEERS
import time
import streamlit as st
from pyblock.peers import *
from pyblock.blockchain.account import *
from pyblock.blockchain.block import *


# Background task that periodically checks if a block can be added


class Background:
    def __init__(self, p2pserver):
        self.time = None
        self.p2pserver = p2pserver

    def can_add_block(block):
        return len(block.votes) >= (0.5 * len(PEERS))

    def run_forever(self):
        while True:
            print("BACKGROUND TASK IS RUNNING")
            current_time = int(time.time())

            if ((current_time - START_TIME.timestamp()) % 30) == 0:
                print("TRUE")
                if self.p2pserver.received_block:
                    if self.can_add_block(self.p2pserver.received_block):
                        self.p2pserver.blockchain.append_block(
                            self.p2pserver.received_block, 
                            self.p2pserver.transaction_pool,
                            self.p2pserver.accounts
                        )

                self.p2pserver.received_block = None
                self.p2pserver.block_proposer = self.p2pserver.accounts.choose_validator(current_time)
                
                #IF WAS ABLE TO CHOOSE A BLOCK PROPOSER
                if self.p2pserver.block_proposer:
                    print("BLOCK PROPOSER CHOSEN: " + self.p2pserver.block_proposer)
                else:
                    print("NO BLOCK PROPOSER CHOSEN.")

                # time.sleep(BLOCK_VALIDATOR_CHOOSE_INTERVAL -
                         #  ((current_time - START_TIME.timestamp()) % BLOCK_VALIDATOR_CHOOSE_INTERVAL))
