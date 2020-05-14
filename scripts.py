from block import Block
from blockchain import BlockChain
import time
# # Script 1 : Generate block

# block = Block(data='Genesis of Catland Coin')
# print (block)
# print (block.hash_is_valid(block.hash()))

# print (block.hash(1))
# print (block.hash_is_valid(block.hash(1)))

# # Script 2 : Mining

# block = Block(data='Transaction 100 catcoins from Alice to Bob')
# block.mine()
# print(block)

# # Script 3 : Generate block chain

chain = BlockChain()
print(chain)

block = Block(data="Txn 100 catcoins from Alice to Bob")
chain.add_block(block)
print (chain)

# # Script 4 : Chaining 
ts = time.time()
for i in range(6):
    new_block = Block(i)
    new_block.mine()
    chain.add_block(new_block)
print ("====")
print ("Total Duration: {0:.2f} seconds".format(time.time() - ts))

chain.print()