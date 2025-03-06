### **1. Strategy Overview**
- **Name**: NR7 Volatility Strategy
- **Developer**: Tony Crabill
- **Year of Development**: 1990
- **Objective**: Enter the market during low volatility periods, ride the trend, and exit when market strength is indicated.
- **Definition of Volatility**: Daily range (difference between High and Low).

---

### **2. Trading Logic**
- **Entry Signal**: 
  - If today's daily range is lower than the previous six trading days' ranges, go long at the close.
- **Exit Signal**:
  - Exit when today's close is higher than yesterday's high.

---

### **3. Trading Products**
- **Example Asset**: SP 500 (ETF with ticker code SPY).

---

### **4. Strategy Details**
- **Entry Condition**: Low volatility period (daily range lower than previous six days).
- **Exit Condition**: When the close exceeds yesterday's high.
- **Position Management**: Long positions only.

---

### **5. Backtest Performance** 
- **Backtest Period**: 1993 to Present.
- **Starting Capital**: $1,100,000 USD.
- **Ending Equity Curve**: Upward slope.
- **Average Gain Per Trade**: 20.6%.
- **Maximum Drawdown**: 25%.
- **Annual Return**: 7.6%.
- **Comparison to Buy and Hold**:
  - Annual return slightly below buy and hold (9.7%).
  - Strategy is invested only 37% of the time.
- **Risk-Adjusted Return**: 20%.

---

### **6. Improvements**
- **Trend Filter**: Using a 200-day moving average reduces maximum drawdown to 15% while maintaining the same average gain.

---

### **7. Conclusion** 
- The NR7 strategy shows potential for consistent gains but with significant drawdowns.
- Adding a trend filter (e.g., 200-day MA) improves risk management without affecting returns.
- Performance comparison to buy and hold is favorable in terms of risk-adjusted returns.
