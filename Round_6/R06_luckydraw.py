import json

import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x69a922218413d7c8473e40f5de20c336b759f10f
# Random number request Tx: https://goerli.etherscan.io/tx/0x618dd2915b7556cb0b0346444b7340a9cf3762b4d2d1570a8f1213ee41cab536#statechange
# The last random number is: 0x317805e7200695e2755be97a73a9b6da9c603f31d46c141674af776458a7d904
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0x317805e7200695e2755be97a73a9b6da9c603f31d46c141674af776458a7d904)

# Read staking snapshot
signup_df_reduce = pd.read_csv('R06_weighted_table_reduced.csv')
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