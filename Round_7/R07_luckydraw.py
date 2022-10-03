import json

import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x6f1f3379538ee17642b50c8e72ad5b5763f27105
# Random number request Tx: https://goerli.etherscan.io/tx/0xa1708b51824f46c01014ea8766589d3044ac8a226b9565b88df9e04bdce6791b#statechange
# The last random number is: 0xbc7d485591040d6f4e5f5f95a08a0ffa4ce61f21447b2e385f969c391adf0a12
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0xbc7d485591040d6f4e5f5f95a08a0ffa4ce61f21447b2e385f969c391adf0a12)

# Read staking snapshot
signup_df_reduce = pd.read_csv('R07_weighted_table_reduced.csv')
signup_df_reduce = signup_df_reduce.T.to_dict()

# Assign raffle tickets to everyone qualified
total_ticket : int = 0
reverse_ticket = dict()
ticket_pool = list()
for cur in signup_df_reduce:
    cur_amount = signup_df_reduce[cur]['amount_token']
    cur_addr = signup_df_reduce[cur]['owner']
    if cur_amount > 999.999:
        for cur_i in range(int(cur_amount)):
            total_ticket += 1
            reverse_ticket[total_ticket] = cur_addr
            ticket_pool.append(total_ticket)

# Random shuffle tickets
random.shuffle(ticket_pool)


# Reveal the first 100 tickets as lucky tickets
pprint(ticket_pool[0:100])

# Show addresses and prizes:
cnt_dict = dict()
for cur_prize in ticket_pool[0:100]:
    if cnt_dict.get(reverse_ticket[cur_prize]) is None:
        cnt_dict[reverse_ticket[cur_prize]] = 0
    cnt_dict[reverse_ticket[cur_prize]] += 1

pprint(cnt_dict)
print(json.dumps(cnt_dict))
