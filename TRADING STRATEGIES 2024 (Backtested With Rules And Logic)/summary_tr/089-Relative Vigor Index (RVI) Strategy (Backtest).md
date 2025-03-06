提出的交易策略涉及使用相对活力指数（RVI）作为动量指标。 这是该战略的简明摘要：

1. **定义和计算** ：
   - The RVI measures price momentum by comparing closing prices to their trading range.
   - It includes a signal line, which is a simple moving average used to smooth results.

2. **策略规则** ：
   - A 5-day lookback period is used.
   - **购买信号** ：当RVI越过信号线和RVI的5天RSI低于50时，执行买入。
   - **卖出信号** ：当RVI越过信号线以下时出售。

3. **表现** ：
   - Tested on GLD (gold ETF), the strategy yielded an average gain of 0.44% per trade with a win rate of 51%, though winners outweighed losers in size.
   - The strategy was not effective on assets like the S&P 500 or bonds, indicating it may work better in specific market conditions.

4. **结论** ：
   - While the RVI is underutilized and showed promise on GLD, its effectiveness can vary across different assets. Further testing and adaptation are recommended for broader applicability.