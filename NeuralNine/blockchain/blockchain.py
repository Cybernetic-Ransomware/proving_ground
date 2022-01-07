import hashlib


class RubberCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = '|€|'.join(transaction_list) + '|€|' + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = '#21_Anna transfer 2.6 RCB to #33_Robert'
t2 = '#21_Anna transfer 0.6 RCB to #22_Carmelia'
t3 = '#22_Carmelia transfer 21 RCB to #38_Anthony'
t4 = '#33_Robert transfer 0.5 RCB to #38_Anthony'
t5 = '#38_Anthony transfer 1.2 RCB to #35_Peter'
t6 = '#22_Carmelia transfer 8.5 RCB to #35_Peter'

initial_block = RubberCoinBlock("AAA", [t1, t2])
print('')
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = RubberCoinBlock(initial_block.block_hash, [t3, t4])
print('')
print(second_block.block_data)
print(second_block.block_hash)

third_block = RubberCoinBlock(second_block.block_hash, [t5, t6])
print('')
print(third_block.block_data)
print(third_block.block_hash)
