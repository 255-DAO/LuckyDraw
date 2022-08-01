# 255 DAO 2555 GLMR LuckyDraw Round 5

## Procedure

1. We took the snapshot of Round 865 for delegator staking amounts.
2. We joined staking amounts with the sign-up table of this giveaway event (with time bonus and vesting bonus counted), the resulting table (address, amount) is stored here as `R05_weighted_table_reduced.csv`
3. We deployed standard Chainlink VRF random generator (using the sample code given in their documentations) on Rinkeby Network at `0x69a922218413d7c8473e40f5de20c336b759f10f`
4. We requested random numbers (Tx: https://rinkeby.etherscan.io/tx/0x8a5140d40d5c9d76eef0ba5291b59f9313e2dadb79a0a0b9da8ee970e1cd06a1#statechange), and take the last one as the random seed in our lucky draw: `0x87614b89a64eb945ea1635be79195545a4859ba8aef3ac35b87032315b180b54`
5. All registered delegators are sorted by their address lexicographically, delegators without a 1000 GLMR staking are disqualified. We then assigned consecutive integers as their raffle tickets. Assigned tickets are also added to the pool in the meantime.
6. The whole raffle ticket poll is shuffled (using random seed as specified in Step 4), and the first 100 tickets are taken out as lucky tickets.

To reproduce the lucky draw results, run:

```
python3 R04_luckydraw.py
```

## 抽奖过程

1. 按规则，我们选取了627轮的质押快照来决定委托人的彩票数量。
2. 我们整合了抽奖活动注册表格和质押快照（包括质押时间加成和未发放奖励加成），结果存放在 `R05_weighted_table_reduced.csv` 文件中。
3. 我们在Rinkeby网络上部署了标准的使用Chainlink VRF生成随机数的合约，合约地址是`0x69a922218413d7c8473e40f5de20c336b759f10f`。
4. 我们使用刚刚部署的合约从Chainlink预言机请求了随机数（交易地址：https://rinkeby.etherscan.io/tx/0x8a5140d40d5c9d76eef0ba5291b59f9313e2dadb79a0a0b9da8ee970e1cd06a1#statechange），然后用得到的最后一个随机数（`0x87614b89a64eb945ea1635be79195545a4859ba8aef3ac35b87032315b180b54`）当作我们抽奖程序的随机数种子。
5. 我们对所有注册过抽奖活动的委托人按地址的字典序进行排序，质押数量不足的委托人会被取消资格。然后对于符合资格的委托人我们分配给他们连续的整数作为他们的彩票，同时把彩票放进一个彩票池里。
6. 我们随机打乱了彩票池，这个随机过程的种子使用的就是我们在步骤4中得到的随机数。

你也可以轻松复现我们的抽奖结果：

```
python3 R04_luckydraw.py
```