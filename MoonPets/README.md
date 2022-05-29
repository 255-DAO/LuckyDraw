# 255 DAO 2555 GLMR LuckyDraw MoonPets

## Procedure

1. We took the snapshot of Round 627 for delegator staking amounts.
2. We joined staking amounts with the sign-up table of this giveaway event, the resulting table (address, amount) is stored here as `ERWL_signup_table_reduced.csv`
3. We deployed standard Chainlink VRF random generator (using the sample code given in their documentations) on Rinkeby Network at `0x69a922218413d7c8473e40f5de20c336b759f10f`
4. We requested random numbers (Tx: https://rinkeby.etherscan.io/tx/0x7578a2c04a03a4db861c658e0c2638dff9e139770a6da34d375e0e36f1f607ce#statechange), and take the last one as the random seed in our lucky draw: `0xd9ac1dd4ec9d3416d12f95e9f3ebfee031451c03915ed96546c032119eb6c380`
5. All registered delegators are sorted by their address lexicographically, delegators without a 1000 GLMR staking are disqualified. We then assigned consecutive integers as their raffle tickets. Assigned tickets are also added to the pool in the meantime.
6. The whole raffle ticket poll is shuffled (using random seed as specified in Step 4), and we took a sufficient number of tickets out as lucky tickets.
7. We then deduplicated people receiving the rewards based on their information in the sign-up table. 

To reproduce the lucky draw results, run:

```
python3 MP_luckydraw.py
```

## 抽奖过程

1. 按规则，我们选取了627轮的质押快照来决定委托人的彩票数量。
2. 我们整合了抽奖活动注册表格和质押快照，结果存放在 `ERWL_signup_table_reduced.csv` 文件中。
3. 我们在Rinkeby网络上部署了标准的使用Chainlink VRF生成随机数的合约，合约地址是`0x69a922218413d7c8473e40f5de20c336b759f10f`。
4. 我们使用刚刚部署的合约从Chainlink预言机请求了随机数（交易地址：https://rinkeby.etherscan.io/tx/0x7578a2c04a03a4db861c658e0c2638dff9e139770a6da34d375e0e36f1f607ce#statechange ），然后用得到的最后一个随机数（`0xd9ac1dd4ec9d3416d12f95e9f3ebfee031451c03915ed96546c032119eb6c380`）当作我们抽奖程序的随机数种子。
5. 我们对所有注册过抽奖活动的委托人按地址的字典序进行排序，质押数量不足的委托人会被取消资格。然后对于符合资格的委托人我们分配给他们连续的整数作为他们的彩票，同时把彩票放进一个彩票池里。
6. 我们随机打乱了彩票池，这个随机过程的种子使用的就是我们在步骤4中得到的随机数。我们抽取了足够数量的奖券。
7. 然后我们去除了重复的中奖者，得到了最终的中奖名单。

你也可以轻松复现我们的抽奖结果：

```
python3 MP_luckydraw.py
```