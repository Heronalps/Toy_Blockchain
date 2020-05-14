class BlockChain(object):
    def __init__(self):
        # Point to latest block
        self.head = None
        # Add tail pointer for genesis block
        self.tail = None
        self.blocks = {} 

    def add_block(self, new_block):
        # For the genesis, record tail block
        if not self.tail:
            self.tail = new_block
        previous_hash = self.head.hash(self.head.nonce) if self.head else None
        new_block.previous_hash = previous_hash

        self.blocks[new_block.identifier] = {
            'block': new_block,
            'previous_hash': previous_hash,
            'previous': self.head,
        }
        # Setup pointer to next block
        if self.head is not None:
            self.head.next_block = new_block
        self.head = new_block
    
    # Add print function to print out the entire chain
    def print(self):
        # Deep copy in Python
        head_ptr = self.tail
        while head_ptr != None:
            print(head_ptr)
            head_ptr = head_ptr.next_block
        print (self.tail)

    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'Blockchain<{} Blocks, Head: {}>'.format(
            num_existing_blocks,
            self.head.identifier if self.head else None
        )