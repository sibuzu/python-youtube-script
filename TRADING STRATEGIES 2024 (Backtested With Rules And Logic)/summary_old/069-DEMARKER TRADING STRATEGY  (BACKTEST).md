The trading strategy involves using a market indicator to identify overbought and oversold levels. After optimizing on SPY, the optimal parameters were identified: a 5-day lookback period with a buy threshold at 5% and a sell threshold at 80%. However, this initial approach resulted in significant drawdowns. To improve performance, two modifications were made:

1. **Sell Condition**: Instead of solely relying on the indicator hitting 80%, trades are now closed when:
   - The close crosses above yesterday's high (indicating strength).
   - The close falls below yesterday's low (indicating weakness).

2. **Trend Line Check**: An additional condition was added where trades are either held or closed based on whether the price breaks above or below a trend line.

The equity curve shows that these modifications reduced drawdowns and improved overall profitability, resulting in a more robust strategy. The final approach is to buy when the indicator hits 5% and sell under the specified conditions related to price strength and trend line breaks.
