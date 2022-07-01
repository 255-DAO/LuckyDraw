import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x69a922218413d7c8473e40f5de20c336b759f10f
# Random number request Tx: https://rinkeby.etherscan.io/tx/0xdcbd4ee4a4486a48800b96967e23b64e98d5ea013b999ba8e30edc9dceffd8a4#statechange
# The last random number is: 0xd9114ed87e4fffba1a175e7564e285e3133b4f9af87eec2b639e775d0eb270c7
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0xd9114ed87e4fffba1a175e7564e285e3133b4f9af87eec2b639e775d0eb270c7)

# Read staking snapshot
signup_df_reduce = pd.read_csv('R04_signup_table_reduced.csv')
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