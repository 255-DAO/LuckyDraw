import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x69a922218413d7c8473e40f5de20c336b759f10f
# Random number request Tx: https://rinkeby.etherscan.io/tx/0xb4fa8b595bf1a826820a8772b6b63dab3f26e1f9fa290f823f7b094bd1e6645a#statechange
# The last random number is: 0xc7ad3856bb2341cf8c6614b97557226ce487048484177160f9d662ec3bac71ec
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0xc7ad3856bb2341cf8c6614b97557226ce487048484177160f9d662ec3bac71ec)

# Read staking snapshot
signup_df_reduce = pd.read_csv('R02_signup_table_reduced.csv')
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