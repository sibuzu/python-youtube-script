### Article Summary

#### Themes:
- Momentum trading strategies.
- Comparison of momentum vs. mean reversion.
- Importance of backtesting and risk-adjusted returns.

---

#### Trading Products/Assets:
1. **SP 500 Index** (First strategy).
2. **Bitcoin** (Second strategy).
3. **Four Asset Class Rotation System** (Third strategy):
   - SPY (S&P 500 ETF)
   - TLT (Long-term Treasuries ETF)
   - EFA (Developed Markets ETF)
   - EEM (Emerging Markets ETF)

---

#### Indicators:
1. **First Strategy**:
   - 100-day high of the close.
   - Lowest close in the last 100 days.

2. **Second Strategy**:
   - New 25-day high of the close.

3. **Third Strategy**:
   - Performance ranking over the prior three months (monthly bars).

---

#### Strategy Details:

1. **First Momentum Strategy**:
   - Entry Signal: Close crosses above the 100-day high.
   - Exit Signal: Close crosses below the lowest close in the last 100 days.
   - Long-only strategy.

2. **Second Momentum Strategy** (Bitcoin):
   - Entry Signal: Bitcoin sets a new 25-day high.
   - Exit Signal: Close is lower than the entry price.
   - Intended for assets with significant price spikes.

3. **Third Momentum Strategy**:
   - Sector Rotation System:
     - Monthly rebalancing based on performance of four asset classes (SPY, TLT, EFA, EEM).
     - Selects the best-performing asset to hold for the next month.
     - Simple rotation strategy with low complexity.

---

#### Backtest Performance:

1. **First Strategy**:
   - SP 500 (1960–Present):
     - Starting Capital: $100,000.
     - Final Value: ~$5.5 Million (60 years).
     - Annualized Return: ~6.5% (excluding dividends) / ~8.5% (including dividends).
     - Time in Market: 69%.
     - Max Drawdown: Half of Buy and Hold.

2. **Second Strategy**:
   - Bitcoin (Performance partially explained by Bitcoin's rise):
     - Starting Capital: $100,000.
     - Final Value: ~$3.6 Million.
     - Time in Market: 13.9%.

3. **Third Strategy**:
   - Four Asset Class Rotation System (2002–Present):
     - Starting Capital: $100,000.
     - Final Value: ~$1.4 Million.
     - Annualized Return: ~13.1%.
     - Max Drawdown: 34%.

---

#### Conclusions:
- Momentum strategies can deliver solid risk-adjusted returns across various asset classes.
- These strategies often keep investors out of major bear markets, reducing drawdowns compared to Buy and Hold.
- Performance varies by asset and time frame, so backtesting is essential.
- Combining momentum with other indicators or time frames (e.g., daily bars for entry) can enhance results.

---

#### Additional Notes:
- Momentum trading requires disciplined backtesting and simulation in a demo account before live execution.
- The article emphasizes the importance of using standalone trading platforms or coding tools like Python for strategy development.
- Future topics include mean reversion strategies.
