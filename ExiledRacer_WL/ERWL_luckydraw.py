import pandas as pd
import random
from pprint import pprint


# Rinkeby VRF consumer contract address: 0x69a922218413d7c8473e40f5de20c336b759f10f
# Random number request Tx: https://rinkeby.etherscan.io/tx/0xa479f7d955586767fbb634ab421d608dc078175b4d77bd18b35f0bd8c4c04768#statechange
# The last random number is: 0xa53a13dae2fd9b3d0aee3f4a0f8031eb58a69f33cff5a0476ab8fcba605d906e
# We use this as seed

# Random seed is obtained from VRF (see process above)
random.seed(0xa53a13dae2fd9b3d0aee3f4a0f8031eb58a69f33cff5a0476ab8fcba605d906e)

# Read staking snapshot
signup_df_reduce = pd.read_csv('ERWL_signup_df_join_reduced.csv')
signup_df_reduce = signup_df_reduce.T.to_dict()

# Assign raffle tickets to everyone qualified
total_ticket : int = 0
reverse_ticket = dict()
ticket_pool = list()

for cur in signup_df_reduce:
    cur_amount = signup_df_reduce[cur]['amount_token']
    cur_addr = signup_df_reduce[cur]['owner']
    if cur_amount > 999.999:
        if cur_amount < 4999.999:
            # 1000~4999: 1 ticket
            for cur_i in range(1):
                total_ticket += 1
                reverse_ticket[total_ticket] = cur_addr
                ticket_pool.append(total_ticket)
        elif cur_amount < 9999.999:
            # 5000~9999: 2 ticket
            for cur_i in range(2):
                total_ticket += 1
                reverse_ticket[total_ticket] = cur_addr
                ticket_pool.append(total_ticket)
        elif cur_amount < 49999.999:
            # 9999~49999: 2 ticket
            for cur_i in range(3):
                total_ticket += 1
                reverse_ticket[total_ticket] = cur_addr
                ticket_pool.append(total_ticket)
        else:
            for cur_i in range(4):
                total_ticket += 1
                reverse_ticket[total_ticket] = cur_addr
                ticket_pool.append(total_ticket)


# Output pool
for cur_ticket in ticket_pool:
    print(str(reverse_ticket[cur_ticket]) + ' : ' + str(cur_ticket))

# Random shuffle tickets
random.shuffle(ticket_pool)


# Reveal the first 20 tickets
# The total number of lucky person is 5, in case a person have multiple lucky tockets, the lucky set will be extended
pprint(ticket_pool[0:20])

# Show addresses and prizes:
cnt_dict = dict()
for cur_prize in ticket_pool[0:20]:
    print(str(reverse_ticket[cur_prize]) + ' : ' + str(cur_prize))
    if cnt_dict.get(reverse_ticket[cur_prize]) is None:
        cnt_dict[reverse_ticket[cur_prize]] = 0
    cnt_dict[reverse_ticket[cur_prize]] += 1

pprint(cnt_dict)
