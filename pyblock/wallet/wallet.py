from Crypto.PublicKey import RSA
from ..chainutil import ChainUtil
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
# from .transaction import Transaction
# from .transaction_pool import TransactionPool

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyblock.blockchain.blockchain import Blockchain


class Wallet:
    def __init__(self):
        # self.balance = 100
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey().export_key()
        
    def __str__(self):
        return f"Wallet -\n\tpublicKey: {self.public_key}\n\tbalance: {self.balance}"

    def sign(self, data):
        data_hash = SHA256.new(data.encode())
        signature = pkcs1_15.new(self.private_key).sign(data_hash)
        return signature

    def get_public_key(self):
        return self.public_key



