# --- import modules ---
import json
import random
from datetime import datetime
from hashlib import sha256

# --- blackchain class ---
class Blockchain(object):
    # --- contructor creates initial empty list ---
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # --- create genesis block ---
        print("--- creating genesis block ---")
        self.chain.append(self.new_block())
        
    # --- new block responsible for creating blocks, adding to chain ---
    def new_block(self):    
        block = {
            "index": len(self.chain),
            "timestamp": datetime.utcnow().isoformat(),
            "transactions": self.pending_transactions,
            "previous_hash": self.last_block["hash"] if self.last_block else None,
            # --- random 64bit nonsense string ---
            "nonce": format(random.getrandbits(64),"x"),
        }
        
        # --- get hash of this block, add to block ---
        block_hash = self.hash(block)
        block["hash"] = block_hash
        
        # --- reset list of pending transactions ---
        self.pending_transactions = []      

        # --- return the block ---
        return block
    
    @staticmethod
    # --- hashes a block ---
    def hash(block):
        # --- sort dictionary or suffer inconsistent hashes ---
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    # --- gets the latest block in chain --- 
    @property
    def last_block(self):
        # --- return last block in chain (if there are blocks) ---
        return self.chain[-1] if self.chain else None

    # --- valid hash to show proof, check if hash begins with  n zeros---
    @staticmethod
    def valid_block(block):
        return block["hash"].startswith("0000")

    # --- proof of work, create new block, check if valid ---
    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break
            
        self.chain.append(new_block)
        print("--- found new block ---", new_block)

    '''
    # --- add new transaction to list of pending transactions ---
    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "recipient": recipient,
            "sender": sender,
            "amount": amount,
            })
    '''
    
