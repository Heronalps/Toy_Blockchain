# block.py

import hashlib
import uuid
import time

class Block(object):
    def __init__(self, data=None, previous_hash=None):
        
        # uuid depends on epoch second
        self.identifier = uuid.uuid4().hex   
        self.nonce = None                    
        self.data = data                     
        self.previous_hash = previous_hash   
        # Add a pointer to next block for traversal 
        self.next_block = None
        
    def hash(self, nonce=None):
        message = hashlib.sha256()
        message.update(self.identifier.encode('utf-8'))
        message.update(str(nonce).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))

        return message.hexdigest()
    
    # Difficulty Reconfiguation
    def hash_is_valid(self, the_hash):
        return the_hash.startswith('0000')

    def __repr__(self):
        # Add Data field to demonstrate transaction info
        return 'Block<Hash: {}, \n Nonce: {}, \n Data: {}>'.format(self.hash(), self.nonce, self.data)

    def mine(self): 
        cur_nonce = self.nonce or 0
        # Add timestamp for timing
        ts = time.time()
        while True:
            the_hash = self.hash(nonce=cur_nonce)
            if self.hash_is_valid(the_hash):  
                self.nonce = cur_nonce    
                print ("Nonce (Number of loops): ", self.nonce) 
                print ("Is hash valid: ", self.hash_is_valid(the_hash))
                print ("Duration : {0:.4f} seconds ".format(time.time() - ts))
                break                          
            else:
                cur_nonce += 1  