### 1. 主題
- **Golden Cross 貿易策略**：一種基於移動平均線交叉的交易策略。

### 2. 使用指標
- **短期移動平均線（50天）**：用於判斷短期市場趨勢。
- **長期移動平均線（200天）**：用於判斷長期市場趨勢。
- **指數移動平均線（EMA）**：表現優於 simple moving average (SMA)，提升了策略的有效性。

### 3. 策略細則
- **信號生成**：基於移動平均線的交叉點（crossover system）。
- **買賣決策**：
  - 上穿（Golden Cross）：_SHORTING.Signal = True，.buySignal = True。
  - 下穿（Death Cross）：SHORT.Signal = True，.sellSignal = True。

### 4. 回測績效
- **回測結果**：Golden Cross 策略在 historical backtests 中表現穩定。
- **年化報酬率**：
  - Golden Cross：6.6%
  - 買後不賣（Buy and Hold）：6.9%

### 5. 結論
- **策略有效性**：Golden Cross 策略在 historical backtests 中表現穩定，但年化報酬率略低於 Buy and Hold。
- **改进建議**：
  - 搭配其他技術指標（如 RSI、MACD）以增強信號的可靠性。
  - 根據不同市場環境調整移動平均線的天數。
  - 考慮加入風險管理機制（如止损、止盈）。
