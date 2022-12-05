import json

import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x6f1f3379538ee17642b50c8e72ad5b5763f27105
# Random number request Tx: https://goerli.etherscan.io/tx/0x39b64b7e93259ebb5f0568de7476c68e876ccb9fe584ca19c6b3a503f6875027#statechange
# The last random number is: 0x5e2d1b4e8ca49024ea721e255e5cb16de25aeef48e3c2b1913c53d5a0cc24a3e
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0x5e2d1b4e8ca49024ea721e255e5cb16de25aeef48e3c2b1913c53d5a0cc24a3e)

# Read staking snapshot
signup_df_reduce = pd.read_csv('R09_weighted_table_reduced.csv')
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
