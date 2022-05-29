import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x69a922218413d7c8473e40f5de20c336b759f10f
# Random number request Tx: https://rinkeby.etherscan.io/tx/0x7578a2c04a03a4db861c658e0c2638dff9e139770a6da34d375e0e36f1f607ce#statechange
# The last random number is: 0xd9ac1dd4ec9d3416d12f95e9f3ebfee031451c03915ed96546c032119eb6c380
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0xd9ac1dd4ec9d3416d12f95e9f3ebfee031451c03915ed96546c032119eb6c380)

# Read staking snapshot
signup_df_reduce = pd.read_csv('MP_signup_table_reduced.csv')
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


# Reveal the first 200 tickets as potential lucky tickets
pprint(ticket_pool[0:400])

# Show addresses and prizes:
cnt_dict = dict()
for cur_prize in ticket_pool[0:400]:
    print(cur_prize, ',', reverse_ticket[cur_prize])
    if cnt_dict.get(reverse_ticket[cur_prize]) is None:
        cnt_dict[reverse_ticket[cur_prize]] = 0
    cnt_dict[reverse_ticket[cur_prize]] += 1

pprint(cnt_dict)