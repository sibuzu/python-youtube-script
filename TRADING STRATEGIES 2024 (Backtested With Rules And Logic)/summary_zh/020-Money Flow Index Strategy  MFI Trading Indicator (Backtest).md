讨论的交易策略基于货币流量指数（MFI）指标，该指标结合了价格和数量数据以衡量买卖压力。 这是一个简明的摘要：

1. **什么是MFI？** 
   - The MFI oscillates between 0 and 100, indicating overbought (above 80) or oversold (below 20) conditions.
   - It helps predict potential price reversals by showing money flow into or out of a security.

2. **策略规则：** 
   - Use a short look-back period (tested with 2 days).
   - Buy when the MFI is below 10 and close at the end of the second day.
   -当收盘价超过前一天的高价时出售。
   - Time stop set to 10 trading days.

3. **表现：** 
   - Backtesting from 1993 showed a significant return, turning $100k into over $2M (a 20x increase).
   - Annualized return of ~10.5% vs. buy-and-hold at ~9.7%, with the strategy being invested only 35% of the time.

4. **注意事项：** 
   - Combining MFI with other indicators can enhance effectiveness but requires careful backtesting to avoid curve fitting.
   - Limitations include sensitivity to volatility and potential false signals, which are part of trading risks.

5. **结论：** 
   - The strategy is simple, effective, and suitable for novice traders. Backtesting is recommended to customize settings based on specific assets.

该策略利用了MFI识别过分购买/超卖条件的能力，旨在利用短期价格变动，同时保持方法直接易于执行。