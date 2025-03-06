所描述的交易策略是一种使用两个移动平均值的趋势跟随方法：9个周期指数的移动平均线（EMA）和30个周期的加权移动平均线（WMA）。 这是一个简明的摘要：

1. **成分** ：
   - **9 period EMA** ：代表短期趋势。
   - **30周期WMA** ：代表长期趋势。

2. **条目规则** ：
   - Buy when the 9-period EMA crosses above the 30-period WMA.
   - Sell when the 9-period EMA crosses below the 30-period WMA.

3. **进行回测结果** ：
   - Average gain per trade: 0.85%.
   -与买卖策略相比，表现不佳（4.6％比9.2％）。
   - Modified backtest with additional rules showed similar performance, with 4.5% annual returns versus 9.2% for Buy-and-Hold.

4. **风险调整后的回报** ：
   - Time spent in the market: 60%, suggesting lower risk due to reduced exposure during non-trending periods.

有关更多详细信息，请访问 [量化策略](https://quantifiedstrategies.com).