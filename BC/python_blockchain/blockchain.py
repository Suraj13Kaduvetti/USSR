import hashlib
import json
import time

class Block:
    def __init__(self, data, previous_hash, self_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.self_hash = self_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'self_hash': self.self_hash
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # First block: previous_hash is null, self_hash points to itself
        genesis_block = Block(data="Genesis Block", previous_hash=None, self_hash=None)
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(data, previous_hash=previous_block.hash, self_hash=None)
        new_block.self_hash = new_block.hash  # New block's self_hash points to its own hash
        self.chain.append(new_block)

    def get_chain(self):
        return self.chain

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.calculate_hash():
                return False
        return True
