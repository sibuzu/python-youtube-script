### TRADING STRATEGIES 2024 (Backtested With Rules And Logic) (中文)

---

<details>
<summary>001. Overnight Trading Strategy (+Backtest) | NIGHT TRADING</summary>

[[Youtube]](https://www.youtube.com/watch?v=-ML4YWkC6to&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

the交易策略涉及在SPY ETF上進行隔夜交易，該間諜ETF跟蹤標準普爾500指數。這是一個簡單的摘要：

1. **進入信號** ：
   - Buy at the close if today is the third consecutive lower close.

2. **退出信號** ：
   - Sell at the open of the next trading day.

3. **性能指標** （從1993年到現在）：
   - Total Trades: 643
   - Average Gain Per Trade: 0.13%
   - Win Rate: 65%
   - Maximum Drawdown: 8%

4. **改進選項** ：
   - Exit at the close instead of the open, resulting in:
     - Higher average gain (0.24% vs. 0.13%)
     -較低的獲勝率（60％比65％）
     - Double the maximum drawdown (17% vs. 8%)

5. **考慮因素** ：
   - The strategy can generate significant returns given SPY's price level.
   - A variant with higher average gain (0.35%) exists but involves fewer trades.

有關更多詳細信息或代碼，請訪問其網站。
</details>

<details>
<summary>002. 3 SIMPLE Trend Following Trading Strategies (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=0kJ_fWP5fKU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略集中在 **趨勢跟隨**，旨在捕獲擴展的市場趨勢，而無需預測特定的價格點。 這是一個簡明的摘要：

### 趨勢的核心概念如下：
- 無論是向上還是向下，都專注於駕駛持續的市場趨勢。
- 避免試圖預測市場頂部或底部。
- 利用基於移動平均值和其他指標的簡單規則來生成買賣信號。

### 提出的關鍵策略：
1. **每月移動平均策略：** 
   - Uses the 12-month Simple Moving Average (SMA) on the S&P 500.
   -規則：
     - Go long when the current month's close crosses above the SMA.
     - Sell and hold cash when it crosses below.
   - Performance:
     - Annual return ~6.6% vs. Buy & Hold’s 7%.
     - Drawdowns lower at 26%.
     - Risk-adjusted Return: 9.6%.

2. **黃金交叉策略：** 
   - Uses the 50-day and 200-day Moving Averages.
   - Rules:
     - Buy when 50-day SMA crosses above 200-day SMA (bullish signal).
     - Sell when it crosses below (bearish signal).
   - Performance:
     - Annual return ~6.6%.
     -投資約69％的時間。
     - Risk-adjusted Return: 9.5%.

3. **超級趨勢指標策略：** 
   - Based on weekly bars, using a median price with bands.
   - Rules:
     - Buy when close crosses above the Super Trend line.
     - Sell when it crosses below.
   - Performance:
     - Annual return ~6%.
     - Invested ~62% of the time.
     - Risk-adjusted Return: 9.5%.

### 趨勢的優勢如下：
- **簡單：** 易於實現明確的規則。
- **低維護：** 需要最少的日常管理。
- **風險調整後的回報：** 與購買和持有相比，降低較低，提供更好的風險獎勵比率。

### 缺點：
- **鞭子：** 頻繁的虛假信號會導致市場校正期間的損失。
- **低獲勝率：** 許多交易可能導致虧損，依靠一些有利可圖的收益。
- **需要紀律：** 必須避免削減勝利者，儘管失敗了，但仍要堅持規則。

### 結論：
趨勢遵循的策略為購買和持有提供了可行的替代方法，特別是吸引那些喜歡系統性，非預測方法的人。 但是，由於依賴大幅收益抵消了許多較小的損失，因此他們要求耐心和紀律。
</details>

<details>
<summary>003. Death Cross Trading Strategies (Backtested+Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=12al7KQInww&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

死亡交叉交易策略是一種技術分析工具，用於識別股票市場潛在的看跌趨勢。 這是基於視頻的策略的簡明摘要：

1. **定義和力學** ：
   - The Death Cross occurs when a shorter-term moving average (e.g., 50-day) crosses below a longer-term moving average (e.g., 200-day). This signals a potential downtrend.

2. **滯後指示器** ：
   - It is a lagging indicator, meaning it confirms trends after they have started, rather than predicting future price movements.

3. **進行回測結果** ：
   - Historical backtests since 1960 show poor performance during Death Cross periods, with minimal growth despite spending only 30% of the time in the market. This highlights the risk of missing out on market gains.

4. **限制** ：
   - Infrequent occurrence (only 32 instances since 1960) and potential for long-term underperformance due to keeping investors out of the market during upward trends.
   - Applicability varies across different markets, requiring individual backtesting.

5. **實施注意事項** ：
   - Use as part of a diversified strategy with other indicators or risk management techniques.
   - Psychological discipline is crucial, as waiting for entry signals (like the Golden Cross) can be challenging during market rises.

6. **結論** ：
   - While the Death Cross can signal significant downturns, its reliance on historical data and lack of adaptability to external factors make it a useful but limited tool. It may be more effective when combined with other strategies rather than used in isolation.
</details>

<details>
<summary>004. Friday 13th Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=22GwTbRFrzE&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

提出的交易策略結合了迷信和技術分析的要素。 這是一個簡明的摘要：

 **策略概述：** 
- **客觀的：** 在13日（星期五）左右利用市場行為，並確定潛在長位的趨勢。

 **規則1（13日，星期五）：** 
- 如果日期是13日星期五，請在前一天評估標準普爾500指數的表現。
- **行動：** 
  - Go LONG if the prior day's closing price was higher than the opening price.
  - Stay out of the market if the prior day ended lower.

 **規則2（趨勢遵循）：** 
- 如果規則1不適用，請評估在過去三周中，標準普爾500指數是否已上升趨勢。
- **行動：** 
  - Enter a LONG position on Fridays if an uptrend is confirmed.
  - Do nothing otherwise.

 **理由：** 
- 13日（星期五）對市場的本質上並不是不幸的，歷史數據顯示出與其他星期五相似的表現。 該策略利用了這些日期的前一天的價格行動。
- 趨勢分析旨在在三周內捕捉持續的向上運動，提供長期的觀點。

該策略將迷信（13日星期五測試）與技術分析（趨勢之後）融合在一起，以告知交易決策。
</details>

<details>
<summary>005. MULTIPLE Time Frame Trading Strategy (+Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=2fASgIgUPrw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

所描述的交易策略是 **多時間交易策略** 旨在在短期撤回期間進入交易時利用長期趨勢。 這是一個簡明的摘要：

### 關鍵組件：
1. **長期趨勢過濾器** ：關閉必須高於250天前的關閉。
   - This ensures that the asset is in an uptrend over the long term.

2. **中間趨勢過濾器** ：閉合必須高於22天前的關閉。
   - This confirms that the asset is trending upward on a medium-term basis.

3. **短期回調條目** ：今天的結束必須是封閉的三天低點。
   - This means entering the trade when the price pulls back to a short-term support level.

4. **退出規則** ：當收盤價高於昨天的收盤價時，賣出。
   - This exit rule aims to lock in profits as soon as the price moves upward from the entry point.

### 例子：
該策略應用於 **XLP ETF**，跟蹤消費者主食，並取得以下結果：

- **交易數量** ：316
- **平均每次交易** ：0.28％
- **獲勝率** ：73％
- **最大減收** ：-10％
- **利潤因子** ：2

### 策略評估：
該策略表現出合理的性能，並具有不錯的獲勝率和利潤率。 但是，每次交易的平均增長相對較低，這可能表明該策略依賴於頻繁的小勝利而不是偶爾的大收益。

### 結論：
該策略結合了多個時間範圍，以使條目與長期趨勢保持一致，同時使用短期回調進行條目。 它似乎適合XLP ETF，但可能需要對其他資產和市場狀況進行測試。 有關更多詳細信息，您可以參考來源或聯繫創建者。
</details>

<details>
<summary>006. The #1 Reason Traders Fail!</summary>

[[Youtube]](https://www.youtube.com/watch?v=3aN9r9vAcq4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

要確定您是否有盈利策略，必須遵循以下步驟：

1. **定義您的策略** ：清楚概述您的交易規則和方法。

2. **量化您的策略** ：將您的想法轉換為可衡量的參數，例如進入/退出點和資金管理規則。

3. **回顧您的策略** ：使用歷史數據來測試您過去策略的執行方式。 這有助於確定諸如過度擬合的問題，並確保您的策略在不同的市場條件下具有牢固的穩定性。

4. **評估統計預期** ：計算關鍵指標，例如贏率，風險回報比和夏普比率，以評估您的策略的盈利能力和風險調整後的回報。

5. **模擬交易** ：使用演示帳戶或紙質交易來測試您的策略，而無需冒險實際資本。

6. **審查和調整** ：不斷地檢查您的結果，並根據績效和不斷變化的市場條件進行必要的調整。

通過遵循以下步驟，您可以確定您的策略是否有可能獲得盈利，並確保您將精力集中在正確的領域。
</details>

<details>
<summary>007. No Way These Returns Are True!  | Trading A Few Days a Month</summary>

[[Youtube]](https://www.youtube.com/watch?v=4iAHRyUuW5g&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中提出的交易策略是基於季節性模式，在一個季節性模式下，股票往往在一個月末和新月的前幾天集會。 這是該策略的摘要：

1. **入口點** ：
   - Buy the S&P 500 on the fifth last trading day of the current month.

2. **出口點** ：
   - Sell on the third trading day of the new month.

3. **投資期** ：
   - The strategy involves being invested for only seven trading days per month (approximately 33% of the time).

4. **表現** ：
   -年收益約為7％，略高於購買和持有的策略，該策略的收益約為6.9％。
   - Drawdowns are significantly smaller, at 27% compared to 56% for a buy-and-hold approach.

5. **權益曲線** ：
   - The equity grows linearly over time with fewer market fluctuations compared to being invested all the time.

6. **改進** ：
   - The strategy has been optimized by reducing the investment period from 33% to 23% of trading days while still achieving an annual return of approximately 6.7%. These improved trading rules are available for subscribing members who pay a small fee.

7. **附加信息** ：
   - The video mentions that more strategies, including swing strategies, will be provided in future videos.
   - Subscribers can access these strategies monthly for a fee, while non-subscribers are encouraged to wait for free content in upcoming videos.

總體而言，該戰略旨在利用本月特定部分的市場趨勢，同時最大程度地減少投資時間和提取的時間。
</details>

<details>
<summary>008. 2 Inverted Yield Curve Strategies (Rules and backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=573OfvS1foc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

倒的收益曲線交易策略涉及使用倒的收益曲線作為進行交易的信號。 該策略進行了兩次測試，當曲線倒轉並在250天後出售時，第一次購買，平均收益約為7.3％，類似於典型的年收益。 第二種策略使用平均值和RSI指標，每次交易的平均增長率為2.5％。 總體而言，研究表明，該策略對於盈利交易並不是特別有用。
</details>

<details>
<summary>009. Trading the SANTA CLAUS Christmas Rally (Seasonal Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=60CKmOTmb70&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

貿易策略利用了金價觀察到的聖誕老人拉力賽現象，假設黃金在年底左右的季節性上升與股票相比，季節性上升更強。 這是該策略的結構化摘要：

### 策略概述：
- **購買信號** ：在12月期權到期日結束時進入黃金的長位置。
- **賣出信號** ：將於12月31日或1月的第一個交易當天在市場上退出該職位。

### 要點：
1. **歷史表現** ：
   -自2000年以來，該策略的平均每個交易平均回報率超過2％。
   
2. **期權到期日** ：
   - Utilizes volatility and potential price movements associated with options traders adjusting positions, which can create buying pressure.

3. **市場心理學** ：
   - Capitalizes on investor optimism at year-end, similar to the Santa Claus rally observed in stocks but applied to gold.
   
4. **新聞通訊提及** ：
   - The strategy is part of a service offered through Quantified Strategies, with more details available via their newsletter.

### 考慮和分析：

- **風險管理** ：圍繞期權到期的潛在波動； 可能需要停止損壞機制。
- **執行問題** ：請注意，12月31日市場關閉可能會影響貿易執行。
- **外部因素** ：黃金價格受到經濟指標，地緣政治事件和利率的影響，這可能會覆蓋季節性趨勢。
- **進行回測方法** ：理解如何計算歷史回報以確保精確和缺乏櫻桃挑選的重要性。
- **多元化和投資組合擬合** ：評估該策略如何與更廣泛的投資方法集成。

### 結論：

儘管該策略顯示出有希望的歷史回報，但建議進一步分析以評估其在各種市場條件（包括潛在異常和外部影響）之間的魯棒性。 潛在的交易者應考慮訂閱新聞通訊以獲取其他見解，但在沒有徹底驗證的情況下對任何過度解放的主張保持謹慎。
</details>

<details>
<summary>010. SECTOR ROTATION strategy  (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=6GfsFt5Wxzw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

所描述的交易策略是一種基於動量的部門旋轉方法，涉及在四個ETF之間旋轉：間諜（標準普爾500指數），TLT（長期財政部），EFA（非美國發達市場）和EEM（新興市場）。 這是策略和考慮因素的結構化摘要：

### 策略概述：
1. **部門旋轉** ：該策略涉及根據其最近的績效在不同資產類別或ETF之間切換投資。
2. **每月排名** ：每個月，ETF根據上個月的表現進行排名。
3. **選擇和持有** ：選擇具有最佳性能的ETF以在一個月的持有期間長期進行。 此過程每月重複。

### 關鍵功能：
- **多樣化** ：ETF涵蓋了我們的股票，債券，國際發達市場和新興市場，可提供對不同資產類別的風險。
- **表現** ：進行回測的年收益率為10.1％，每次交易平均收益為1.3％，直到2022年的表現都很好。

### 考慮和問題：
1. **交易成本** ：頻繁的交易可能會產生可觀的費用，從而可能降低盈利能力。 這些成本對策略收益的影響尚不清楚。
2. **決勝局** ：未指定ETF（例如，決勝局）之間處理均等性能的過程。
3. **投資組合結構** ：該策略沒有提及持有現金； 它總是擁有ETF，這可能會導致表現不佳時期的強迫投資。
4. **風險管理** ：除了切換ETF之外，缺乏明確的風險管理，如果ETF在持有期間崩潰，則可能將投資組合暴露於大量下降。
5. **市場周期和下降** ：該策略在不同市場周期（例如熊市）之間的策略尚未詳細介紹，並且沒有解決回報的波動。
6. **與其他策略進行比較** ：尚未將策略與購買和持有的方法或其他方法等方法進行比較。 諸如Sharpe比率之類的指標將為風險調整後的收益提供更深入的見解。
7. **實施詳細信息** ：提及 "email broker" 尚不清楚，但它可能是指適合頻繁交易的經紀帳戶。
8. **生存偏見** ：進行回測結果的潛在問題，沒有考慮不包括不包括的表現不佳的策略。

### 結論：
該策略通過每月輪換利用跨資產類別的動力，提供多樣化的福利和歷史表現。 但是，它提出了有關各種市場條件的交易成本，風險管理和可持續性的問題。 需要進一步的分析來評估其在不同環境中的魯棒性和有效性。
</details>

<details>
<summary>011. 3 Momentum Trading Strategies (Backtests &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=6NWcKpupjJo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

交易視頻討論了三種不同的勢頭交易策略，每個策略都針對不同的資產和市場條件量身定製。 這是涵蓋的要點的摘要：

### 1。**第一動量策略：100天高/低關閉** 
   - **規則** ：
     - Go long when the closing price crosses above the highest close in the past 100 days.
     - Sell when the closing price crosses below the lowest close in the past 100 days.
   - **回測結果** ：
     - Applied to the S&P 500 from 1960 to present.
     - Starting capital of $100,000 grows to $5.5 million over 60 years, yielding ~6.5% annualized returns (excluding dividends; ~8.5% with dividends).
   - **表現** ：
     - Engages in the market only 69% of the time.
     - Low drawdowns and risk-adjusted returns, outperforming a "Buy & Hold" 主要熊市中的策略。

### 2。**第二動量策略：價格峰值的資產25天高關閉** 
   - **規則** ：
     - Buy when the closing price sets a new high over the past 25 days.
     - Sell when the closing price drops below this high.
   - **回測結果** ：
     - Applied to Bitcoin, showing significant growth (though results are influenced by Bitcoin's overall rise).
     -市場參與率很低（佔時間約為13.9％），但性能仍然具有競爭力 "Buy & Hold." 
   - **表現** ：
     - Low drawdowns and solid risk-adjusted returns, suitable for volatile assets like Bitcoin.

### 3。**第三動量策略：部門旋轉系統** 
   - **規則** ：
     - Monthly rebalancing by ranking four ETFs (S&P 500 (SPY), Long-Term Treasuries (TLT), Developed Markets (EFA), and Emerging Markets (EEM)) based on their prior three-month performance.
     - Invest in the top-performing asset each month.
   - **回測結果** ：
     - Starting capital of $100,000 grows to ~$1.4 million over 20 years (~13.1% annualized returns).
   - **表現** ：
     - Drawdowns are manageable (e.g., ~34%), with relatively low correlation to the stock market.
     - Slowed performance in recent years, likely due to market changes.

### 動量策略的關鍵要點
- **動量與平均逆轉** ：強調購買強度而不是弱點。
- **最佳設置** ：
  - Time frames: 3 to 12 months for stocks; other assets may vary (e.g., daily or weekly).
  -資產類別：在包括股票和商品在內的各種班級中有效。
- **成功因素** ：
  - Backtesting is crucial.
  - Combine with indicators (e.g., using momentum with a monthly time frame but entering on daily pullbacks).
  - Use demo accounts for testing before live trading.

### 閉幕說明
該視頻通過鼓勵觀眾探索自己的策略，並建議查看網站以獲取其他資源。 下一個視頻將重點介紹平均回歸策略。
</details>

<details>
<summary>012. Limit Order Trading Strategy (Rules +Backtest )</summary>

[[Youtube]](https://www.youtube.com/watch?v=7b9dU8tDYtQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

在此交易策略視頻中，重點是比較市場訂單和限制訂單，以證明不同的訂單類型如何導致截然不同的結果。 這是關鍵點的摘要：

1. **了解限制訂單** ：限制訂單用於以特定價格或更高的價格購買或出售證券。 它包括一個 "limit price" 指定購買購買或最低銷售價格的最高價格。

2. **進行回測策略** ：
   - A mean reversion strategy was backtested using a market order on NASDAQ 100. The results showed an average gain of 89% per trade, translating to a compounded annual return of 10.4%. However, the strategy only had an 18% investment utilization rate, meaning the capital was idle for long periods.
   -當修改相同的策略以使用限制順序作為購買信號（以弱點為單位）時，交易數量大大減少了一半以上。 儘管如此，每次交易的平均增長率從89％增加到12％。 但是，總體複合年收益率下降到7.6％，這主要是由於錯過的交易機會。

3. **交易的權衡** ：使用限制順序可以提高每次交易的平均增長，但可能會導致交易較少，總回報率降低。 這突出了理解不同訂單類型和策略參數之間權衡取捨的重要性。

4. **結論** ：視頻強調，在調整策略以使用限制訂單可能會提高個人貿易盈利能力，但它也可以降低總體回報潛力。 它鼓勵觀眾在決定訂單類型或策略時考慮其目標，風險承受能力和交易目標。

該視頻通過邀請評論以進一步討論該策略的可能改進或變化。
</details>

<details>
<summary>013. Williams %R Strategy: (Rules Revealed + Backtest))</summary>

[[Youtube]](https://www.youtube.com/watch?v=7hrpH-b_2es&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

威廉士百分比R交易策略是一種技術指標，用於識別市場中的過分購買和超賣條件。 這是該策略的摘要：

1. **定義** ：指示器在指定時期內測量電流相對於最高高的接近，範圍從0到-100。 以上讀數為-20表示過多的狀況，而低於-80的讀數則表明超出了售出。

2. **策略規則** ：
   - Enter a long position when the indicator crosses below -90.
   - Exit the trade when the indicator crosses above -30 or if the close exceeds yesterday's high.

3. **進行回測結果** ：
   - The strategy has an annual return of 11.5% over 580 trades, outperforming a Buy and Hold approach (e.g., S&P 500) during periods like the 2008 financial crisis and the COVID-19 pandemic.
   - It operates with only 22% market exposure, reducing risk.

4. **缺點** ：該策略的最大減速為177％，因此考慮交易成本和風險至關重要。

5. **結論** ：威廉士百分比r是一個簡單而有效的工具，尤其是在市場動蕩期間，但應使用歷史數據進行測試，並可能使用分數份額來管理風險。
</details>

<details>
<summary>014. 3 ETF Trading Strategies (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=8EmDCJUgnrw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻討論了三種ETF交易策略，每種策略都有特定的規則和績效指標。 這是每種策略的摘要：

1. **周期策略** ：
   - **條目規則** ：如果比周五關閉，則在周一關閉時購買標準普爾500指數（間諜）。
   - **退出規則** ：賣出當收盤價高於昨天的高點或五個交易日期。
   - **表現** ：100,000美元的投資增長到約220萬美元，平均每次交易，只有24％的投資時間。 與買入相比，降價明顯降低（約23％）。

2. **降低低點和降低高高策略** ：
   - **條目規則** ：在連續三天的低點和高潮都較低時購買。
   - **退出規則** ：在上升一天購買兩天後，售出比昨天更接近。
   - **表現** ：提供約8％的年收益，增長$ 10萬美元至$ 60萬美元。 在2000  -  2003年市場中經歷了31％的跌幅，但此後表現良好。

3. **動量旋轉策略（MEB Faber）** ：
   - **資產** ：間諜（S＆P 500），GLD（黃金），TLT（債券）。
   - **條目規則** ：投資3個月的移動平均值高於10個月MA的資產，將三分之二分配給每個ETF。
   - **表現** ：〜〜8％的年收益，最大值最高。 策略在資產類別之間具有多元化。

 **關鍵要點** ：
- 沒有一個 "best" 戰略; 跨不同策略，時間範圍（長期與短期）和市場方向（長和短暫）多樣化。
- 與單個股票相比，ETF提供的風險降低，但不太可能獲得大量贏家。
- 初學者應從演示帳戶和測試策略開始至少一年才能實時交易。
- 通常更適合零售商人的時間範圍（每日/每周/每月酒吧）。
</details>

<details>
<summary>015. Fabian Timing Model Strategy (Trading Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=8gH33k5W334&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

fabian的時機模型是Richard Fabian在1960年代中期制定的一種定量趨勢跟蹤策略。 這是基於這樣的觀察結果，即標準普爾500指數，道瓊工業平均水平和公用事業部門傾向於一起移動。 這是該策略的摘要：

### 交易規則：
1. **購買信號** ：
   - The strategy signals a "buy" 對於標準普爾500指數，當所有三個指數（標準普爾500指數，道瓊工業平均水平和公用事業部門）都高於其各自的39周移動平均值時。

2. **賣出信號** ：
   -它發出信號 "sell" 當兩個或多個索引低於其各自的39周移動平均值時。

### 回測結果（從2000年使用間諜ETF）：
- 該模型表現優於 "buy and hold" 策略，產生7％的回報率和5％的買入和持有率。
- 它僅投資了56％的時間，表明在市場上大量時間。
- 該策略是為長期投資而不是短期收益而設計的。

### 關鍵說明：
- **長期重點** ：Fabian的時機模型不是用於快速利潤的，而是數十年來持續增長。
- **耐心和時間** ：與策略一致需要耐心和時間才能看到積極的結果。
- **進一步閱讀** ：有關更多詳細信息，請考慮閱讀連結的文章或探索網站上的其他資源。

該戰略旨在通過僅在條件良好的情況下保持投資來利用長期趨勢，從而有可能隨著時間的推移提高投資回報。
</details>

<details>
<summary>016. Value Investing vs Growth Investing Rotating Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=9UlOnc-3Uck&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中提出的交易策略重點是根據其相對績效在價值和增長股票之間旋轉投資。 這是關鍵點的摘要：

1. **價值與增長股票** ：
   - **價值投資** ：涉及購買低估的股票具有強大的基本面，希望市場能夠意識到它們的真正價值隨著時間的流逝。 這些股票通常更穩定，揮發性較小。
   - **增長投資** ：專注於預計將以比整體市場更快增長的股票增長。 由於其增長潛力，這些股票通常具有較高的估值，但可能會更加波動。

2. **歷史表現** ：
   - Value stocks have historically outperformed growth stocks over the long term, though growth stocks can outperform in the short term, especially during periods of economic growth or rising interest rates (e.g., post-2008 financial crisis).

3. **旋轉策略** ：
   - The strategy involves using ETFs that track value and growth stocks: IUSV (value) and IUSG (growth).
   - A momentum ratio is calculated by dividing the price of IUSG by IUSV.
   - 10-day and 40-day moving averages are used to determine short-term momentum trends.

4. **執行** ：
   - When value stocks outperform growth stocks, investors sell growth ETFs (IUSG) and buy value ETFs (IUSV).
   - Conversely, when growth stocks outperform, investors sell value ETFs and buy growth ETFs.
   - This rotation aims to capitalize on the relative strength of each asset class.

5. **表現** ：
   - The strategy claims an annual return of 9%, outperforming both value-only (7.4%) and growth-only investments.
   - It also reduces price variation, thereby lowering risk compared to holding individual stocks.

6. **批評** ：
   - Critics argue that market timing is difficult and advocate for a "Buy and Hold" 相反，多樣化的方法。

該策略利用價值和增長ETF的相對性能動態調整持有量，旨在通過基於動量信號旋轉來捕獲優越的回報。
</details>

<details>
<summary>017. Currency Trading Strategies - &quot;From Carry Trades to Curve Trades&quot;</summary>

[[Youtube]](https://www.youtube.com/watch?v=9ZuBES1XZ4k&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

總結的交易策略稱為 "Curvy Trades," 在研究論文中引入的，標題為 *來自Carry Trades到Curvy Trades *。 這種方法代表了從傳統的隨身攜帶貿易策略的轉變，這些策略僅依賴於短期利率差異，該策略是通過收益曲線（尤其是尼爾森 - 耶和華因素）中的其他信息來納入短期利率差異的。

彎曲交易的主要特徵包括：

1. **較高的風險調整後收益** ：與傳統的攜帶交易相比，該策略提供了更好的尖銳比率，這表明更加一致，波動性較小。

2. **撞車風險降低** ：與通常涉及日元或瑞士法郎等貨幣的傳統攜帶交易不同，彎曲交易不太容易受到突然的市場逆轉或崩潰風險的影響。

3. **不同的市場動態** ：研究表明，標準定價因素（例如匯率波動率）沒有充分解釋彎曲的貿易申報表，這意味著它們可能是由不同的市場動態驅動的。

4. **產量曲線見解** ：產量曲線中的高曲率因素標誌著短期利率的較高未來路徑，這可能會對貨幣施加上壓力，從而為交易決策提供了寶貴的見解。

總之，彎曲的交易將利用收益曲線信息到潛在地徹底改變貨幣交易策略，為投資者提供創新的方法，以實現更好的風險調整後的回報並導致市場複雜性。
</details>

<details>
<summary>018. 3 MACD Trading Strategies 2024 (Backtested With Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=9h46J1xanfk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 交易策略的摘要：

該視頻介紹了三種基於MACD的交易策略，每個策略都有特定的規則和進行回測結果。 這是每種策略和關鍵要點的有組織摘要：

---

#### **1. First Strategy: MACD Histogram Mean Reversion** 
- **機制** ：當MACD直方圖連續四天從四天前低於零以下的水平下降時，購買。
- **表現** ：
  - Annual return: ~5% (doesn't beat S&P 500's buy-and-hold).
  - Win rate: 89% (very high).
  - Drawdown: 16% (low).
  - Time in market: 5% (allows trading other strategies).
- **結論** ：由於降低率較低和獲勝率很高，但收益有限。

---

#### **2。第二策略：用布林帶的MACD直方圖** 
- **機制** ：當直方圖橫穿下孔帶以下時輸入長時間； 當它越過上部樂隊上方時出售。
- **表現** ：
  - Return: $1.15M from $100K investment (8.4% annual).
  - Win rate: Solid, though not detailed.
  - Drawdown: 44% (high).
  - Time in market: 64%.
- **結論** ：混合性能； 儘管有良好的回報，但大幅下調可能會導致交易者放棄該策略。

---

#### **3. Third Strategy: Best Performing Strategy (Members Only)** 
- **機制** ：涉及RSI，只有一個買賣規則。
- **表現** ：
  - Return: $1.5M from $100K investment.
  - Drawdown: 15% (low).
  - Time in market: 21% (low).
  - Annual return: Nearly as good as buy-and-hold.
  - Risk-adjusted return: 43% (annual return / time invested).
- **結論** ：最佳策略，低收納，高回報和可管理的滑倒。

---

### 關鍵要點：
1. **MACD與RSI** ：雖然MACD不是最佳指標，但在與均值歸還或與RSI一起使用時，它在某些情況下可以有效。
2. **市場適合性** ：MACD由於其均值回復的性質而在股票/股票ETF中運行良好，尤其是用於搖擺交易（每日或每周酒吧）。
3. **最佳設置** ：較短的回顧期（幾天）和每日條是MACD分析的理想選擇。
4. **策略選擇** ：第三個策略（帶有RSI）是最有效的，但是交易者應評估其在市場上的風險承受能力和時間。

---

### Final Note:
內容強調，這些策略不是投資建議，並鼓勵觀眾在實施之前對策略進行徹底測試。
</details>

<details>
<summary>019. Multiple Days Up (MDU) And Multiple Days Down (MDD). - Larry Connors</summary>

[[Youtube]](https://www.youtube.com/watch?v=9j20XPfOcgQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

拉裡·康納（Larry Connor）第六章中描述的交易策略 "High Probability Trading" 被稱為「上升數天」和「下降」策略。 這是一個摘要：

 **客觀的** ：確定ETF經歷了明顯的下降勢頭時，可以確定潛在的購買機會。

 **關鍵組件** ：
1. **進入信號** ：該策略表明，當ETF在過去五個交易日中至少有四個下降時，進入較長的位置（購買）。 這是由特定指標指示的，即從低到高的波動，信號降低了許多天。
   
2. **進入條件的條件** ：
   - The ETF's price must be above its 200-day moving average (to ensure it's not in a long-term downtrend).
   - The closing price must be below the 5-day moving average (indicating recent weakness).

3. **輸入時間** ：在滿足支持條件之一的一天結束時輸入交易。

4. **退出信號** ：當ETF關閉其5天移動平均線以上時退出貿易（賣出），這表明潛在的逆轉。

5. **風險管理** ：在這種策略中沒有使用停止損失，這會增加風險，但旨在捕捉趨勢一旦逆轉。

 **進行回測結果** ：
- 從2000年開始，對20種不同的股票市場ETF進行了回測。
- 在各個ETF之間的結果差異很大。
- 當作為投資組合測試，每個信號分配20％（一次最多持有五個ETF），由於在市場上花費的時間很少，該策略會產生較低的年收益。
- 在間諜和QQQ上也進行了測試，每個股權分配了50％，但結果表現不佳，表現出不穩定的性能。

 **結論** ：該策略的結果並不是特別令人印象深刻，創建者建議探索其網站上可用的其他策略以取得更好的成果。 與往常一樣，交易帶來風險，並鼓勵觀眾在實施任何策略之前進行徹底的研究。

該摘要簡要概述了視頻中提到的策略，其機制和回測結果。
</details>

<details>
<summary>020. Money Flow Index Strategy | MFI Trading Indicator (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=9qmYEqzA7HI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略基於貨幣流量指數（MFI）指標，該指標結合了價格和數量數據以衡量買賣壓力。 這是一個簡明的摘要：

1. **什麼是MFI？** 
   - The MFI oscillates between 0 and 100, indicating overbought (above 80) or oversold (below 20) conditions.
   - It helps predict potential price reversals by showing money flow into or out of a security.

2. **策略規則：** 
   - Use a short look-back period (tested with 2 days).
   - Buy when the MFI is below 10 and close at the end of the second day.
   -當收盤價超過前一天的高價時出售。
   - Time stop set to 10 trading days.

3. **表現：** 
   - Backtesting from 1993 showed a significant return, turning $100k into over $2M (a 20x increase).
   - Annualized return of ~10.5% vs. buy-and-hold at ~9.7%, with the strategy being invested only 35% of the time.

4. **注意事項：** 
   - Combining MFI with other indicators can enhance effectiveness but requires careful backtesting to avoid curve fitting.
   - Limitations include sensitivity to volatility and potential false signals, which are part of trading risks.

5. **結論：** 
   - The strategy is simple, effective, and suitable for novice traders. Backtesting is recommended to customize settings based on specific assets.

該策略利用了MFI識別過分購買/超賣條件的能力，旨在利用短期價格變動，同時保持方法直接易於執行。
</details>

<details>
<summary>021. Trade the High - Short Interest Indicator (Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=A6WIwn58sd4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的交易策略圍繞分析股票的短暫興趣。 這是一個簡明的摘要：

1. **簡短興趣的定義** ：
   - Short interest is the percentage of a company's outstanding shares that have been sold short.
   - Example: If a company has 1 billion shares and 50 million are shorted, the short interest is 5%.

2. **短利率** ：
   - This measures how many days it would take for short sellers to cover their positions, based on average daily trading volume.

3. **績效分析** ：
   - The video references a study showing that stocks with high short interest (top deciles) tend to underperform in the subsequent year.
   - Conversely, stocks with low short interest outperform the market average.

4. **離群值和軼事數據** ：
   - While exceptions like GameStop exist (where short squeezes lead to massive price increases), these are rare.
   - The strategy advises against relying on such outlier cases for making investment decisions.

5. **結論** ：
   - High short interest is generally associated with weaker future returns, suggesting it's "bad" 用於庫存性能。
   -如果投資者的目標是尋找下一個多袋子，則應專注於低興趣的股票。

該視頻強調避免軼事數據，並著重於做出明智的交易決策的歷史趨勢。
</details>

<details>
<summary>022. Gold Overnight Trading Strategy – Make Money While Sleeping</summary>

[[Youtube]](https://www.youtube.com/watch?v=AofDVmSjQjY&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略側重於黃金和黃金礦工部門，特別是利用GDX（Gold Miners ETF）和GLD（Gold Price ETF）等ETF。 關鍵想法圍繞著一夜之間，從下一個開放而不是盤中的市場圍繞持有頭寸。

### 要點：
1. **隔夜邊緣** ：
   - The strategy highlights that holding positions overnight in GDX and GLD has historically shown a consistent upward trend, resulting in steady gains.
   - Conversely, buying at the open and selling at the close (intraday) has often resulted in losses.

2. **歷史一致性** ：
   - The equity curve for GDX shows a stable upward slope when held overnight, whereas intraday trading has been less successful.
   - Similarly, GLD's performance from close to next open has outperformed compared to intraday returns, which have been slightly negative on average.

3. **策略增強** ：
   - While the overnight edge alone may not be significant enough for standalone trading, adding one or two other variables can enhance the strategy.
   - The video mentions a specific "Gold Overnight Strategy" 對於包含其他變量的GLD，在近二十年中導致斜率上升和穩定的性能。

4. **產品** ：
   - The content creator provides subscribers with access to courses and strategies like this one through their website.

### 結論：
該策略強調了在與黃金相關的ETF中持續一oight夜的重要性對於盈利交易的重要性，這表明將隔夜持有與其他變量相結合可以創造出強大而一致的方法。 對於那些有興趣的人，可以在創建者的網站上獲得更多詳細的信息。
</details>

<details>
<summary>023. Testing A Random Entry Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=CDw5HhC9Lc8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

這 "Work Trading" 策略是一種有趣的方法，依賴於每年進行12次隨機交易，每年進行了四天。 這是關鍵點的簡明摘要：

1. **策略概述** ：該策略涉及完全根據機會選擇12個交易，而無需使用指標或分析。 每次交易持續四天。

2. **性能指標** ：
   - **平均每次交易** ：大約0.37（單位未指定，可能的PIP或百分比）。
   - **利潤因子** ：1.7，表明利潤多於損失。
   - **最大減收** ：大約12％，這是相對易於管理的。

3. **懷疑和考慮因素** ：
   - The reliance on randomness in trading is unconventional, as typically a systematic approach with analysis is preferred for sustainability.
   - Despite positive metrics, the strategy's long-term viability is questioned due to market efficiency and unpredictability.
   - Risk management practices, such as position sizing, are crucial to avoid significant losses.

4. **結論** ：儘管該策略顯示出不錯的績效指標，但其對隨機性的依賴引起了對其可持續性的懷疑。 它可以用作實驗方法，而不是可靠的長期方法。 有關貿易選擇和執行的更多詳細信息對於全面評估至關重要。

從本質上講，儘管該策略具有一些吸引人的結果，但由於其隨機性質，建議謹慎，並且可能更適合作為非常規方法的測試，而不是主要交易方法。
</details>

<details>
<summary>024. What Happens To Stocks When Bonds Go Down?</summary>

[[Youtube]](https://www.youtube.com/watch?v=Dw1pit-dC8Y&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點關注債券與股票之間的關係，特別是研究債券下降時股票的情況。 這是一個簡明的摘要：

1. **關鍵洞察力** ：該策略基於股票與利率之間的反比關係。 當利率上升（債券下降）時，持有股票等風險較高的資產就會降低。

2. **策略概述** ：
   - **進入信號** ：當債券價格（使用TLT，20年美國國庫券的ETF）低於其移動平均水平時，購買股票（使用間諜作為代理）。
   - **退出信號** ：賣出股票價格上漲以上時出售股票。

3. **進行回測結果** ：
   - The strategy was backtested using different moving averages (5 to 100 days).
   - For the 15-day moving average, the strategy showed weak performance compared to SPY's historical returns.
   - Annual return was less than 1%, with a maximum drawdown of 50%.

4. **有趣的觀察** ：扭轉買入/銷售信號（債券時債券上升和銷售時購買時，債券下跌）會產生更好的結果，這將在隨後的視頻中進行探討。

該策略旨在利用股票與債券之間的反相關關係，但在進行回測的成功有限，這表明了改進或替代方法的潛在空間。
</details>

<details>
<summary>025. Sell The Rip Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=EHj846zWHLY&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略稱為 "Sell The Rip," 這是基於金融市場在波浪，上升和下降的概念上。 該策略的重點是銷售資產達到高估水平，旨在捕獲市場高價的利潤。

### 策略的要點：
1. **傳統的平均歸還策略** ：
   - Uses the 3-day RSI (Relative Strength Index) as a signal.
   - Buys when the RSI drops below 30 and sells when it reaches 70.
   - Results in erratic performance with high drawdowns (reaching 35% twice), making it difficult for traders to stick with.

2. **改進"Sell The Rip"信號** ：
   - Sells when the closing price exceeds yesterday's high, indicating potential overvaluation.
   - Improves performance significantly compared to the original strategy:
     - Reduces drawdowns (only twice exceeding 20%).
     - Maintains competitive annual returns while keeping the invested time low (~27% of the time).

3. **性能指標** ：
   - Generates consistent returns with lower risk.
   - Annual returns are comparable to a "Buy and Hold" 策略，但在市場上的時間更少。

4. **市場適合性** ：
   - Works best for stock markets, where mean reversion is more common.
   - Less effective for commodities and forex, which tend to trend rather than revert.

### 結論：
改進 "Sell The Rip" 戰略為尋求利用高估資產的交易者提供了可行的方法。 但是，請重新測試每個特定市場的策略以確定其有效性。 儘管它在所有市場上都沒有普遍起作用，但它為具有平均回歸特徵的環境提供了一個可靠的框架。
</details>

<details>
<summary>026. CANDLESTICKS Patterns Trading Strategies - Which One Is Best?</summary>

[[Youtube]](https://www.youtube.com/watch?v=G6kvcga6zPQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點是利用燭臺模式進行知情交易。 這是一個簡明的摘要：

1. **燭臺分析** ：該視頻引入了燭臺作為可視化金融市場價格變動的工具，這表明它們可以有效地產生利潤。

2. **進行回測和量化** ：該策略不依賴軼事證據，而是涉及通過進行回測的所有燭臺模式進行量化。 此過程將基於績效指標（如利潤因子）等性能進行排名。

3. **性能結果** ：在過去的30年中，使用至少50次交易的前10個燭臺模式，該策略獲得了20倍的回報，表現優於買入和持有的方法。 它還需要更少的時間投資（佔期限的28％）。

4. **下降和風險管理** ：該策略的最大降低低於15％，明顯好於同一時期的55％的55％的下降。 它提供了不相關的回報，即使在衰退中也表現良好（例如，2008年的 +23.7％，2022年為 +2.2％）。

5. **實際應用** ：該研究以中等費用可用，包括邏輯解釋，交易結果以及諸如Metatrader和Tradestation等平臺的代碼。

6. **結論** ：該策略結束時強調燭臺模式的有效性，並邀請觀眾訂閱更多有關趨勢跟隨策略的內容。

這種方法將技術分析與系統進行回測，以提供數據驅動的交易方法。
</details>

<details>
<summary>027. Last Day Of The Month Trading Strategy - Ultimo Effect (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=H7asjNMQ0OU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的交易策略稱為 "Turn of the Month" 戰略。 這是一個摘要：

1. **概念** ：策略利用 "end-of-the-month effect," 由於薪金支付，餘額調整和儲蓄增加等因素，股票往往會在每個月末接近。 這種效果通常會溢出到新月的前幾天。

2. **規則** ：
   - Buy the S&P 500 on the close of the fifth trading day of the month.
   - Sell on the close of the third trading day of the following month.

3. **期間** ：該策略涉及每月任職大約7天，從而騰出時間進行其他活動。

4. **表現** ：
   - It outperforms the traditional Buy and Hold strategy with an annual return of 7.1% compared to 6.9%, using the same exposure period.
   - Drawdowns are lower; while the Buy and Hold strategy has a maximum drawdown of -56%, the Turn of the Month strategy tops out at -27%.

5. **靈活性** ：可以根據個人經驗和市場條件來調整交易規則，以提高收益。

該視頻強調，這種策略使交易者能夠以最少的時間投資獲得一致的每月利潤，這使其成為那些在交易活動中尋求效率的人的有吸引力的選擇。
</details>

<details>
<summary>028. Turnaround Tuesday Trading Strategy (Trading Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=HClGJJgzv4U&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的交易策略稱為 "Turnaround Tuesday" 策略是基於在股票市場觀察到的季節性影響的。 這是該策略的摘要：

1. **概念** ：這個想法是，如果股票市場在周一的下降日期，則市場可能會扭轉其趨勢並在周二大幅上升。 相反，如果周一市場上升，則周二往往會變平或下降。

2. **交易規則** ：
   - If today is Monday and the closing price of the current trading day (Monday) is lower than Friday's close, buy at the close.
   -退出交易時，要麼收盤超過前一天的高點（與星期一的高點相比，周二的閉幕式）或最多持有五天。

3. **表現** ：
   - When tested on SPY (an ETF tracking the S&P 500), the strategy produced an impressive equity curve with relatively small drawdowns.
   - The maximum drawdown was short-lived, and other drawdowns were in single digits.
   - The annualized return of the strategy is 10.6%, which is lower than the 99.8% return from a long-term buy-and-hold strategy on SPY over a period starting in 1993.

4. **與買賣的比較** ：
   - While the Turnaround Tuesday strategy has lower returns, it involves being invested only about 24% of the time, keeping 76% of the capital in cash.
   - This cash can be used for other complementary strategies.

5. **改進** ：
   - The strategy can be tweaked to improve results, which is available to paying subscribers.

6. **考慮因素** ：
   - It's important to do thorough research and ensure that this or any strategy aligns with your financial goals.
   - The strategy is not presented as investment advice, and viewers are encouraged to perform their own due diligence.

該視頻結束時，邀請觀眾訂閱更多內容，並建議在頻道網站上查看其他策略。
</details>

<details>
<summary>029. Bullish Reversal Trading Strategy – (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=IF7-Ne2BV5k&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點是識別和資本化 "reversal days" 在市場上。 這是一個簡明的摘要：

1. **看好逆轉日策略** ：
   - **狀況** ：
     - Today's low is lower than yesterday's low.
     - Today's close is higher than yesterday's close.
     - The 5-day RSI (Relative Strength Index) must be below 35, indicating oversold conditions.
   - **執行** ：
     - Enter the trade on the reversal day (green arrows).
     - Exit after holding for up to 24 days based on backtesting results in Gold (GLD), which showed optimal performance with an average gain of 2.02% when exited after 24 days.
   - **表現** ：
     - The strategy demonstrated a positive profit factor across multiple exit points, suggesting reliability.

2. **看跌逆轉日策略** ：
   - **狀況** ：
     - Today's high is higher than yesterday's high.
     - Today's close is lower than yesterday's close.
     - The 5-day RSI must be above 65, indicating overbought conditions.
   - **執行** ：
     - Enter the trade on the reversal day (green arrows).
     - Exit after holding for up to 24 days.
   - **表現** ：
     -雖然有利可圖，但回報顯著低於看漲的戰略。 這種表現不佳的部分歸因於黃金的長期向上偏見，這使得從短職位的利潤中充滿挑戰。

3. **結論** ：
   - The bullish reversal day strategy performed better in backtesting.
   - The bearish strategy faced difficulties due to the asset's (Gold) inherent upward trend.
   - Both strategies are part of a broader offering for subscribers, including courses and resources available on the provider's website.

該視頻強調了在實施此類策略之前，嚴格進行重新測試和了解市場動態的重要性。
</details>

<details>
<summary>030. VOLATILITY Trading Strategy - ATR Bands (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=LXVwz2KE6O8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

the討論的交易策略是一種基于波動率的方法，已經使用了將近十年。 它在各種ETF和期貨合約中都表現良好，在納斯達克100上的歷史表現最佳。主要功能包括：

- **表現** ：該策略提供一致的回報，平均每年約為13％，但最少的下降，除了2008年的金融危機期間（最大降低18％）之外，沒有巨大的損失。 它在牛市和熊市都表現良好。

- **風險調整後的回報** ：儘管僅投資了約11％的時間，並且平均持有交易少於五天，但該策略可提供近120％的高風險調整回報。

- **多樣化** ：雖然它跨多個索引工作，但它在NASDAQ 100上很出色。它在標準普爾500指數和消費者主食ETF（XLP）上也顯示出積極的結果，儘管收益可能會有所不同。

- **規則** ：該策略採用了三個進入規則：波動率，價格行動和趨勢過濾，其中一條規則是退出。 它旨在最大程度地減少由於每年的交易數量少而減少滑倒和佣金。

該策略可用於中等費用，這反映了其可感知的價值鑑於其性能及其維護所需的努力。
</details>

<details>
<summary>031. Magical RSI Trading Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=LsLv-m1AAK4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

所討論的交易策略採用相對強度指數（RSI）來利用股票市場的平均值。 這是一個簡明的摘要：

### 策略概述：
1. **客觀的** ：通過低購買和銷售高價來利用短期價格校正（平均歸還）。

2. **進入信號** ：
   - **健康）狀況** ：輸入RSI低於20以下時，表明狀況超出。
   - **理由** ：價格可能會從被低估的水平反彈。

3. **退出信號** ：
   - **狀況** ：當滿足以下任何一個時退出：
     -RSI上升到60以上（過高的狀況）。
     - The current close exceeds the previous day's high.
   - **理由** ：價格可能已經達到高峰或趨勢向上趨勢，促使出口。

4. **樂器** ：主要應用於Spy（S＆P 500），XLP（消費者主食）和XLV（醫療保健）等ETF，具有其他資產。

### 性能指標：
- **回測結果（1993–2023）** ：
  - **交易數量** ：351貿易。
  - **平均每次交易** ：〜0.8％。
  - **年回報** ：〜9.2％，略低於買入和持有的（〜9.7％）。
  - **獲勝率** ：78％的交易盈利。
  - **投資時間** ：每年16％，表示短期內。
  - **風險調整後的回報** ：56％，按年收益計算為投資時間。
  - **最大減收** ：23％。

### 主要注意事項：
- **進入/退出級別** ：該策略使用20和60的RSI水平，比通常引用的30和70更緊密。這可能會減少錯誤的信號，但也可能限制參與強大的趨勢。
- **執行** ：如果價格迅速趨勢，可能會較早出現，可能會缺少長時間的價格變動。
- **下降風險** ：該策略的最大降低為23％，突出了風險管理的重要性。

### 結論：
該策略對於旨在捕獲市場平均恢復的短期交易者有效。 它可以平衡性能與減少曝光時間，並提供競爭性風險調整後的回報。 但是，它需要仔細考慮進入/退出水平以及長時間趨勢或價格較慢的潛在局限性。
</details>

<details>
<summary>032. Ranging Trading Strategies (NR7) Since 1990</summary>

[[Youtube]](https://www.youtube.com/watch?v=MHbAliaJo-c&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

由託尼·克拉比爾（Tony Crabbill）於1990年制定的NR7交易策略是一種基于波動率的方法，旨在在低波動期間進入市場，並在波動性增加時退出。 這是一個簡明的摘要：

### 關鍵功能：
- **進入信號** ：在一天結束時輸入長位置，當時每日範圍（高 - 低）是前六個交易日中最低的。
- **退出信號** ：如果當天的收盤價超過前一天的高價，則將退出交易。
- **進行回測結果** ：
  -從1993年到現在對間諜ETF進行了測試。
  - Starting with $1,000,000, the strategy resulted in:
    - Average gain per trade: ~26%
    - Max drawdown: ~25%
    - Annual return: ~7.6%
- **比較** ：年收益略低於買入和持有的（9.7％），但提供了更好的風險調整後收益（約20％）。
- **改進** ：添加200天的移動平均趨勢濾波器將最大跌幅降低到約15％，而不會影響平均增益。

### 結論：
NR7是一種有效的策略，對於試圖利用較低波動率時期的貿易商，並改善了風險管理。
</details>

<details>
<summary>033. Why You Should Love A Bear Market! (Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=MbT5H87uxio&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中突出顯示的交易策略，稱為 "Bare Market Trading," 專注於使用技術指標組合在熊市期間利用機會。 這是一個結構化的摘要：

1. **市場定義** ：
   - A bull market occurs when stocks trade above their 200-day moving average.
   - A bear market is identified when stocks are below this same moving average.

2. **策略概述** ：
   - The strategy employs mean reversion, anticipating that prices will return to an average after deviation.
   -在2天的時間內利用相對強度指數（RSI）； 當RSI降至10以下時，進入長位置，表明條件過多。
   - Exits trades when the closing price exceeds the previous day's high, signaling strength.

3. **應用程式上下文** ：
   - Trades are executed exclusively during bear markets, filtered by QQQ (NASDAQ 100 ETF) being below its 200-day moving average.

4. **性能指標** ：
   - Since 2000, the strategy has yielded an average gain of 1.3% per trade during bear markets, outperforming bull market strategies.
   -在諸如.com崩潰，金融危機和2022年低迷之類的重大熊活動中取得了成功。

5. **成功背後的理由** ：
   - Higher volatility in bear markets leads to inefficiencies, providing opportunities for profit.
   - Despite initial declines due to market problems, solutions often drive price recovery, benefiting long positions.

6. **簡短銷售筆記** ：
   - Short selling strategies are more effective during bear markets due to increased volatility but are exclusive to paid members.

從本質上講，該戰略利用了熊條件下的平均恢復和市場效率低下，與牛市策略相比提供了違反直覺但有利可圖的方法。
</details>

<details>
<summary>034. 4 Bond Trading Strategies (Rules and Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=N7PnyY132fk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻討論了四種債券交易策略，由於其較低的相關性，將債券作為與股票的補充資產類別。 要點包括：

1. **粘結特性** ：債券的風險低於股票，因為債券持有人是在破產股東面前支付的，並且表現出較少的價格波動。

2. **策略** ：
   - **策略1** ：在本月的第七個交易日購買TLT（20年期財政部ETF），並在月底出售，每年收益率為5.45％。
   - **策略2** ：在月底上進行簡短的TLT，並在下個月的第七個交易日進行覆蓋，儘管債券價格上漲，但每年收益率為4.41％。
   - **策略3** ：將策略1和2結合起來，以獲得更高的回報（每年10.25％），投資時間更少（61％），提供多元化的收益。
   - **策略4** ：使用價格行動和季節性變量的長期債券策略，每年回報率為4.8％。

3. **多樣化的好處** ：將債券納入投資組合可以增強收益並減少唯一的策略。

4. **結論** ：債券提供低風險的替代方案和多元化的好處，使其成為交易投資組合的寶貴補充。 該視頻強調這些策略是例子，過去的表現並不能表示未來的結果。
</details>

<details>
<summary>035. Averaging Down Trading Strategy (Backtest+Performance)</summary>

[[Youtube]](https://www.youtube.com/watch?v=NBOGY39woyA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

這是描述的交易策略的簡明摘要：

 **平均降低交易策略：** 

1. **客觀的：**   


2. **隨著價格降低，股票價格下跌的利潤。**   
   - Buy additional shares at lower prices to reduce the average cost per share.
   - Example: 
     - Buy 100 shares at $10 each.
     - Price drops to $8; buy another 100 shares.
     - Average cost per share becomes $9.

3. **機制：**   
   - Use a rationale (e.g., technical indicators like RSI) to decide when to average down.
   -在示例策略中：
     - Enter when 5-day RSI drops below 50.
     - Add to position if daily RSI falls at least 5 points and remains below 50.

4. **風險管理：**   
   - Allocate 50% of capital initially, with the option to add the remaining 50% under specific conditions.
   - Reduces maximum loss exposure compared to a standard strategy.

5. ****   
   - Slightly lower overall profits but improved risk-adjusted returns (Profit Factor: 55% vs. 39%).

6. **性能指標：**   
   - Averaging down can be controversial due to increased exposure, but it may enhance risk-adjusted performance.
   -策略自定義和回測至關重要。

 **結論：**
</details>

<details>
<summary>036. Backtest Trading Strategies Using CHATGPT &amp; AI</summary>

[[Youtube]](https://www.youtube.com/watch?v=NOOKxAMHpGU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略涉及利用OpenAI開發的AI CHAT GPT來協助產生和進行回測思想。 這是一個簡明的摘要：

1. **客觀的** ：探索CHAT GPT是否可以通過產生和進行回測策略來成為獲得交易優勢的工具。

2. **訓練AI** ：
   - The user needs to guide Chat GPT on what they want it for, i.e., trading.
   - Provide basic trading ideas to prompt the AI's creativity.

3. **進行回測過程** ：
   - A Bollinger Band Mean Reversion strategy was chosen for backtesting.
   -參數集：偏差係數為2的20周期布林帶。
   - The strategy involves buying when the price closes below the lower band and selling when it closes above the upper band.

4. **執行** ：
   - Chat GPT was used to write Python code for backtesting using libraries like pandas, numpy, yfinance, and matplotlib.
   - The generated code was run without modifications.

5. **結果** ：
   - The strategy showed an annual return of 3.2% with 326 trades.
   - The equity curve appeared reasonable, indicating potential as a starting point for further development.

6. **結論** ：
   - Chat GPT is not a trading platform or financial advisor but can be a valuable tool for brainstorming ideas and generating backtests.
   - AI tools like Chat GPT are expected to become integral parts of quantitative models, revolutionizing the trading landscape.

該視頻強調，儘管聊天GPT可能無法提供 "killer strategy," 它為交易者提供了一個有用的起點，可以建立自己的模型。
</details>

<details>
<summary>037. 9/30 Trading Strategy |  (Backtest And Example)</summary>

[[Youtube]](https://www.youtube.com/watch?v=NRUyND6zzF4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

所描述的交易策略是一種使用兩個移動平均值的趨勢跟隨方法：9個周期指數的移動平均線（EMA）和30個周期的加權移動平均線（WMA）。 這是一個簡明的摘要：

1. **成分** ：
   - **9 period EMA** ：代表短期趨勢。
   - **30周期WMA** ：代表長期趨勢。

2. **條目規則** ：
   - Buy when the 9-period EMA crosses above the 30-period WMA.
   - Sell when the 9-period EMA crosses below the 30-period WMA.

3. **進行回測結果** ：
   - Average gain per trade: 0.85%.
   -與買賣策略相比，表現不佳（4.6％比9.2％）。
   - Modified backtest with additional rules showed similar performance, with 4.5% annual returns versus 9.2% for Buy-and-Hold.

4. **風險調整後的回報** ：
   - Time spent in the market: 60%, suggesting lower risk due to reduced exposure during non-trending periods.

有關更多詳細信息，請訪問 [量化策略](https://quantifiedstrategies.com).
</details>

<details>
<summary>038. Bullish Harami Candlestick: Definition, Trading Backtest</summary>

[[Youtube]](https://www.youtube.com/watch?v=NWK8JPbD2P0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

貿易策略討論了圍繞看漲的哈拉米燭臺模式，該模式用於識別下降趨勢中的潛在逆轉。 這是一個簡明的摘要：

1. **看漲聖地模式** ：
   - **結構** ：由兩支蠟燭組成。
     - The first candle is a large bearish (red) candle with a long body, indicating strong selling pressure.
     - The second candle is a small bullish candle (often a doji), completely engulfed by the first candle, showing market indecision.
   - **語境** ：出現在下降期間。

2. **模式識別** ：
   - Confirmed in a downtrend with a large bearish candle followed by a small bullish candle within its body.

3. **解釋** ：
   - Suggests a potential reversal as the small bullish candle indicates possible buyer interest and shifting momentum.

4. **策略規則** ：
   - Enter a trade when both the Bullish Harami is formed and the 5-day RSI is below 40.
   - Exit after holding for a specified number of days (e.g., 10 trading days).

5. **表現** ：
   - Historical backtesting on the S&P 500 showed an average gain per trade of approximately 0.95% when held for 10 days.
   -勝率從55％到70％不等，由於股價隨著時間的推移而上漲，持有期間的較長時間不斷提高。

6. **考慮因素** ：
   - Use with caution, as patterns can provide false signals. Combine with other indicators like RSI for better reliability.

該策略利用了看漲的哈拉米模式和RSI指標來利用下降市場的潛在看漲逆轉。
</details>

<details>
<summary>039. 7 Algo Trading Strategies (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=NojfYk31_xI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻討論了七種算法交易策略，強調了系統和定量方法可以有效地進行交易。 這是關鍵點的摘要：

1. **策略概述** ：
   - **動力和趨勢跟隨** ：MEB Faber的動量策略之類的策略涉及遵循間諜，TLT和GLD等ETF的趨勢。
   - **平均歸還** ：一種基於平均回歸原則的標準普爾500標準普爾500的策略。
   - **Fabian定時模型** ：由理察·法比安（Richard Fabian）開發的這種長期趨勢範圍的策略使用標準普爾500，道瓊瓊斯和公用事業部門指數之間的市場間信號。
   - **自動化和系統交易** ：自動化多種策略的能力是一個關鍵優勢，使交易者可以專注於開發系統而不是執行交易。

2. **算法交易的優勢** ：
   - **效率** ：自動執行，減少對恆定監視的需求。
   - **專注於戰略制定** ：允許交易者專注於創建和完善模型。
   - **行為錯誤減少** ：通過引入決策和執行之間的一層，它可以最大程度地減少情緒幹擾。

3. **挑戰** ：
   - **編碼和技術技能** ：需要在Python等程式語言中進行策略實施知識。
   - **反覆試驗** ：制定成功的策略通常涉及重大實驗和從失敗中學習。
   - **策略維護** ：需要定期維護和適應以確保持續性能。

4. **結論** ：
   - Algorithmic trading doesn't need to be overly complex; simplicity can lead to long-term profitability.
   - Emphasizes the importance of a systematic mindset and understanding statistical principles like the law of large numbers.

該視頻通過鼓勵觀眾探索更多策略，並強調定量交易中持續學習的價值。
</details>

<details>
<summary>040. CARRY TRADE Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=PqE3eM2eJio&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略是外匯通常使用的攜帶貿易。 這是一個簡明的摘要：

1. **機制** ：借用低利率的貨幣，並將其轉換為另一種利率較高的貨幣。 目標是從利率差異中獲利。

2. **關鍵組件** ：
   - **槓桿作用** ：用於擴大回報，但也會增加風險。
   - **貨幣對** ：通常涉及日元和美元之類的對，一個人的利率低，另一個具有更高的利率。

3. **風險** ：
   - **高波動性** ：貨幣可能會發生重大波動，從而導致潛在的大損失。
   - **負偏度** ：正如納西姆·塔勒布（Nassim Taleb）強調的那樣，該策略容易產生尾巴風險，這意味著它很容易受到可能造成巨大損失的隨機衝擊。

4. **結果** ：雖然該策略可能會帶來許多小勝利，但由於槓桿作用和市場波動，它帶來了罕見，災難性損失的高風險。

總而言之，攜帶貿易利用利率差異，但使貿易商面臨貨幣變動和槓桿作用的重大風險。
</details>

<details>
<summary>041. Supertrend Indicator Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=PvPsrjGW2tI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

超級趨勢指標是一種趨勢跟隨工具，旨在捕獲重要的市場趨勢，同時最大程度地減少趨勢。 這是基於回測結果的策略的簡明摘要：

1. **指標概述** ：
   - The Super Trend indicator uses a median price with added and subtracted average true range (ATR) bands. It generates signals when the price crosses above or below these bands, indicating potential trend changes.
   - The indicator simplifies to a single signal line that switches between upper and lower bands based on market conditions.

2. **交易策略** ：
   - **進入信號** ：當價格超過超級趨勢指標時，購買。
   - **退出信號** ：賣出價格低於超級趨勢指標時出售。
   - **參數** ：通常使用具有10桿回溯期的每周杆和三個ATR乘數，儘管可以調整這些條件。

3. **進行回測結果** ：
   - Tested on S&P 500 from 1960 to present.
   - Starting capital of $100,000 grew to approximately $4 million, producing a 44% gain in one example trade.
   - Annualized return of nearly 6% (excluding dividends).
   -最大降低為24％，而買入和持有量為56％，導致風險調整後的回報率約為9.4％，高於購買和持有的〜7％。

4. **主要考慮因素** ：
   - Requires a long-term mindset as it doesn't trade frequently (only 38 trades since 1960).
   - The indicator is not very active, keeping you invested only about 63% of the time.

該策略旨在有效地平衡風險和回報，使其適合患者的長期投資者。
</details>

<details>
<summary>042. 3 RSI Trading Strategies - Relative Strength Index (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=Qo62oiT0xdg&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻討論了三種RSI交易策略，每種策略都有特定的規則和測試結果。 這是一個簡明的摘要：

1. **為期兩天的RSI策略** ：
   - **入口** ：購買兩天的RSI越過10以下時。
   - **出口** ：賣出為期兩天的RSI越過80以上。
   - **表現** ：從100,000美元開始，資本在〜30年內增至120萬美元，每年收益率為8.5％。 該策略有27％的時間活躍。

2. **改進的策略（QS退出）** ：
   - **入口** ：與上面相同。
   - **出口** ：賣出當結束時高於前一天的高點。
   - **表現** ：資本增長到95萬美元，交易平滑和較小的跌幅（最高損失23％，很少比12％少）。 在市場上的活動時間少10％，提供了更好的風險調整後收益。

3. **RSI動量策略** ：
   - Uses a 100-day lookback period and 14-day RSI.
   - **入口/出口** ：在公牛政權（RSI> 50）中長時間退出。
   - **表現** ：產生了很少的信號，只有兩個虧損交易。 但是，它的表現不足前兩種策略。

 **關鍵要點** ：
- RSI最好用作用於股票/ETF短期交易的平均歸還指標。
- 最佳設置：2-3天的回顧期和每日酒吧。
- 與其他指標結合可以提高性能。

主持人更喜歡第二種策略，這是由於更好的風險調整後收益和更順暢的抽獎。
</details>

<details>
<summary>043. PMI and the Stock Market - Strategy To Trade The ISM Index</summary>

[[Youtube]](https://www.youtube.com/watch?v=RU8Ic_YUClc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

the視頻中提出的交易策略涉及使用ISM製造指數（PMI）作為宏觀經濟指標，以指導標準普爾500指數的投資。這是一個簡明的摘要：

1. **指標** ：ISM PMI，反映了美國製造業的健康狀況，讀數超過50，指示擴展，低於50表示收縮。

2. **戰略** ：
   - When the PMI reading is above 50 (economic expansion), buy the S&P 500 at the month's opening.
   - Sell at the next month's opening, holding for one month each time.
   
3. **表現** ：
   - The strategy is invested approximately 72% of the time.
   - Annualized return is 7.3%, slightly below the S&P 500's 8.5% but with reduced drawdowns.

4. **延長的持有期** ：
   - Backtesting shows that holding for longer periods (e.g., 12 months) can enhance returns, with an average gain of 10.99% per trade and higher exposure (86%).

5. **結論** ：
   - The strategy leverages economic expansion phases indicated by PMI readings above 50 to capture superior returns.
   - Extending holding periods during these expansions can further improve performance.

這種方法旨在利用製造業健康與市場績效之間的相關性，從而根據宏觀經濟條件優化投資時間。
</details>

<details>
<summary>044. 4 VIX Trading Strategies (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=SoqRHI5ldXs&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻討論了以VIX指數為中心的交易策略，通常稱為 "fear index," 這意味著在標準普爾500指數市場中暗示波動。 這是關鍵點的摘要：

1. **了解VIX** ：
   - The VIX is inversely related to the stock market; when it rises, the stock market tends to fall, and vice versa.
   - High VIX readings indicate fear or uncertainty, while low readings suggest complacency.

2. **進行回測策略** ：
   - **策略1** ：比較當VIX高於或低於其20天移動平均線時，標準普爾500標準普爾500的每日回報。 結果顯示VIX上升時的回報較高。
   - **策略2** ：使用VIX和Bollinger樂隊。 該策略涉及購買標準普爾500標準普爾500，如果VIX超過其10天的上班樂隊，則基於最近的價格行動的退出規則。 它產生了穩定的股本曲線，但表現不佳的購買回報。
   - **策略3** ：結合VIX HIGH和RSI（相對強度指數）的突破策略。 該策略的性能比上一個策略稍好。
   - **策略4** ：一種持續的策略，將職位保留24小時。 這種方法旨在利用短期市場的轉變，但表現不佳的購買回報仍然不足。

3. **關鍵要點** ：
   - The VIX can be a useful tool for identifying potential trading opportunities, particularly during periods of fear or uncertainty.
   - While the strategies tested do not outperform buy-and-hold in absolute terms, they offer lower drawdowns and risk-adjusted returns, making them attractive options depending on risk tolerance.

4. **結論** ：
   - The video emphasizes the importance of using the VIX to identify trading opportunities, especially during periods of market stress. It concludes with a quote highlighting that buying when there's fear in the market can be profitable, aligning with the idea of contrarian investing.

總體而言，該視頻探討了將VIX納入交易策略的各種方法，旨在利用市場波動和投資者的情緒。
</details>

<details>
<summary>045. 10 Trading Strategies (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=T2J8x9xlZKc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

摘要概述了十年來證明有效的十種交易策略，利用了技術指標和市場異常。 關鍵要點包括專注於既定的指標，利用季節性模式，確認沒有策略是萬無一失的，以及測試和適應性的重要性。 結論強調通過這些要素建立強大的系統，以在金融市場上長期成功。

---

 **交易策略摘要：** 

1. **威廉士％r指標** ：一種平均回歸策略，數十年來一直表現出色，儘管市場波動，但仍表現出可靠的回報。

2. **聖誕老人集會** ：在12月14日之後的第一個星期五購買標準普爾500指數，並在1月初銷售，以最少的投資時間提供高收益。

3. **月底交易** ：購買羅素2000股票接近月底並持有直到下個月結束，提供一致的增長，但在2010年之後的績效較弱。

4. **季節性短策略** ：在9月下旬打擊標準普爾500指數，歷史上對於股票來說是一個糟糕的一周，儘管有挑戰性執行，但仍提供了平均收益。

5. **比特幣動量策略** ：長期比特幣超過其25天的關閉且跌至低於其低於其25天的關閉時，每年的收益率很高，但獲勝率較低，但可管理的縮水量。

6. **羅素2000個月末交易** ：自1987年以來一直在增長資本，儘管2010年後的績效較弱，但仍然積極。

7. **市場異常和季節性模式** ：利用特定的日曆事件以及資產中的季節性弱點或強度可能導致高回報，風險很小。

8. **風險管理** ：儘管有策略的優勢，但不可避免的是逐漸減少，需要有效的風險管理。

9. **適應性和測試** ：基於新數據的持續完善策略對於長期成功至關重要，即使市場條件發展。

10. **結合元素** ：建立具有時間測試方法，對異常的理解和適應性的基礎的建築系統，可以導致強大的交易系統。

---

 **結論：** 

通過整合這些要素（對驗證指標的依賴，市場異常的開發，審慎的風險管理和適應性），交易者可以開發不僅持久而且在動態金融景觀中壯成長的系統。
</details>

<details>
<summary>046. IBS - Internal Bar Strength Trading STRATEGY (Statistic &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=URPUON-P3zY&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中引入的交易策略圍繞內部條形強度（IBS）指標，該指標被計算為（今天的關閉 - 低） /（今天的高低）。 該指標在0到1之間波動，低值表明在每日低和高值附近較弱的接近，表明在每日高點附近近距離接近。 該戰略旨在利用平均回歸原則來利用短期市場的回調。

概述了三種具體策略：

1. **第一個策略** ：在IBS低於0.1時購買並在超過0.9時出售。 在QQQ（NASDAQ-100 ETF）上進行了重新測試，儘管僅投資了38％的時間，但從2000年到2023年，年增長率超過12％。

2. **第二個策略** ：使用IBS指標為期兩天的平均值。 當平均水平低於0.25時購買，並在超過0.75時出售。 對XLP（消費者主食ETF）進行了重新測試，導致穩定增長，從2000年開始，每年6.3％的收益率為6.3％，僅投資了33％。

3. **第三策略** ：將IBS指示器與三天的RSI結合在一起。 當RSI低於30，IBS低於0.2時購買； 當價格超過昨天的高價或IBS超過0.9時出售。 對間諜（標準普爾500 ETF）進行的回測表現出了強勁的表現，自1993年以來的年度回報率為9.6％，只有18％的投資時間，最大降低為23％。

總體而言，IBS指標被強調為短期交易的強大工具，適當使用時提供了相對較低風險的大量回報。 這些策略強調了簡單性和有效性，使他們可以使用易變市場的系統方法的交易者使用。
</details>

<details>
<summary>047. 3 Index Trading Strategies (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=UURZzdzdxTQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻介紹了三種指數交易策略，每個策略都有特定的規則和設置。 這是每個摘要：

1. **商品與公平率策略** ：
   - Compares the performance of commodities (using the Goldman Sachs Commodity Index) against equities (S&P 500).
   - Uses a short moving average (21 days) to generate trading signals.
   - Produces an annual return of nearly 9%, outperforming the S&P 500, though it is volatile.

2. **價值和生長旋轉策略** ：
   - Trades between value (IUSV ETF) and growth (IUSG ETF) indices based on a moving average crossover system.
   -與單個指數相比，年收益率近9％，波動性較小。

3. **平均歸還策略** ：
   - Focuses on the S&P 500 (SPY ETF) with a simple buy and sell rule.
   - Generates significant returns (15.5% annually) by being invested only 35% of the time, with a modest maximum drawdown.

該視頻強調跨策略，市場和資產類別的多元化，並建議觀眾在實時交易之前使用演示帳戶。 它還指出，指數交易通常比外匯或商品的波動性較小，並且可以與個人股票交易相結合，以進行更廣泛的敞口。
</details>

<details>
<summary>048. 3 MEAN REVERSION TRADING STRATEGIES</summary>

[[Youtube]](https://www.youtube.com/watch?v=UkoTdKV65yk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

這是提出的交易策略的簡明摘要：

1. **概述** ：該視頻介紹了三種對不同ETF進行測試的平均回歸交易策略，旨在提高交易績效。

2. **平均歸還定義** ：該策略假設資產價格在巨大偏差後恢復到其平均值。 它涉及購買超賣資產並出售過多的資產。

3. **討論了策略** ：
   - **第一策略（XLP ETF）** ：重點關注消費者主食，每天通過基於價格下跌和實力的規則進行交易。 性能與風險較低的購買和持有回報相匹配。
   - **第二策略（FXI ETF）** ：針對中國市場的目標，使用IBS指標進行平均歸還。 它的表現優於購買和持有的，但由於市場的上升偏見而具有挑戰性。
   - **第三策略（間諜ETF）** ：Traders S＆P 500具有一個簡單的規則 - 在五天的低點下，以更高的關閉或五天後出售。 儘管參與較低，但收益類似於購買和持有的收益。

4. **表現** ：所有策略均顯示出強大的風險調整回報，前兩個勝過勝過的買賣，第三個與之匹配。

5. **最佳條件** ：由於較高的波動率，平均恢復在熊市期間最有效。 長位置通常比短職位更好。

6. **結論** ：雖然不優於趨勢跟隨策略，但平均恢復是一種可行的方法，尤其是對於那些尋求較低風險和一致回報的人來說。

該視頻結束時，鼓勵觀眾加入策略代碼，並提示即將到來的趨勢關注內容。
</details>

<details>
<summary>049. What Happens When Stock Markets Are Overbought?</summary>

[[Youtube]](https://www.youtube.com/watch?v=V8lL3DBl44E&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點是使用相對強度指數（RSI）作為關鍵指標來確定股票市場中的過高條件。 這是該戰略的簡明摘要：

1. **理解超買和卑鄙的回歸** ：該策略是基於平均恢復原則，在該原理中，與趨勢的強大偏差預計將恢復到平均水平。 當市場在確定的時期（例如，幾天，幾周或幾個月）中經歷顯著增長時，就會發生過多的條件。

2. **使用RSI指標** ：RSI用於識別過高的條件。 在95個以上的RSI信號表明市場過高的兩天RSI。

3. **交易規則** ：
   - Buy (entry) the S&P 500 at the close when the two-day RSI is above 95.
   - Sell (exit) at the close after a specified number of days, depending on the strategy's parameters.

4. **進行回測結果** ：反測試顯示，短期內（前五天）的回報低於長期平均水平（每天約0.05％）。 但是，隨著時間的流逝，回報傾向於與長期平均值保持一致，表明平均恢復。

5. **結論** ：該戰略強調了過分承擔的條件可能會導致短期收益降低，但由於預期的平均值，可以為長期投資者提供機會。

這種方法旨在通過利用統計分析和RSI等技術指標來幫助交易者做出明智的決定。
</details>

<details>
<summary>050. Martingale Trading Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=VlvO82W6QlA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

martingale交易策略是一種經常用於賭博的高風險方法，由於其重大缺點，通常不建議用於金融市場。 這是一個簡明的摘要：

1. **策略概述** ：
   - The strategy involves doubling the bet size after each loss, aiming to recover all previous losses with a single win.
   - It assumes a 50% chance of winning each trade and relies on eventually recovering losses through one successful trade.

2. **它如何工作** ：
   - Start with an initial bet (e.g., $100).
   -每次損失之後，將投注大小加倍：$ 200，然後是400美元，等等。
   - Theoretically, a win should cover all previous losses and yield a small profit.

3. **金融市場的風險** ：
   - **概率問題** ：在實際市場中，獲勝的可能性不是50％。 延長的損失條紋會迅速耗盡資本。
   - **收回問題** ：即使發生獲勝的交易，它也必須抵消所有以前的損失，這需要比先前的損失之和更大的勝利。

4. **實際例子** ：
   - Tested on the S&P 500 with specific rules (e.g., using RSI indicators), the strategy showed an annual return of 8.7% but was underutilized.
   -修改僅使用部分權益會惡化績效，降低增長並增加潛在損失。

5. **結論** ：
   - The Martingale strategy is risky and unsuitable for most traders due to its high dependency on luck and the probability of significant account losses.
   - It's more fitting for gambling scenarios rather than serious trading.

總而言之，儘管Martingale策略理論上可以收回損失，但它在金融市場上構成了重大風險，這對於尋求可持續收益的交易者來說是一個糟糕的選擇。
</details>

<details>
<summary>051. 3 Simple LITECOIN Crypto Trading Strategies | Crypto</summary>

[[Youtube]](https://www.youtube.com/watch?v=X3J7x3AUEaw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

交易策略討論了關注Litecoin，這是一種以快速交易時間而聞名的加密貨幣。 概述了三種不同的方法：

1. **短期趨勢遵循策略** ：該策略使用20天簡單的移動平均線（SMA）來生成買賣信號。 如果收盤價超過了SMA，則將佔據很長的位置； 如果下降到以下，則啟動了短職位。 與購買和持有的方法相比，它表現出卓越的性能，平均每次交易的平均增長率為8.4％，年收益率為114％。

2. **長期趨勢遵循策略** ：利用100天和250天的SMA，當較短的SMA越過較長的SMA並在反向發生時提示賣出時，該策略標誌著很長的條目。 儘管樣本量較小（7次交易），但每年的收益率為66％，表現優於買入和持有的收益。

3. **動量策略** ：這種方法檢查今天的收盤價是否高於決定長時間還是短的25天的價格。 憑藉129筆交易，每次交易的平均收益為9.6％，年收益率為70％，又超過了買入和持有的收益。

每種策略都利用市場行為的不同方面（包括期限趨勢，長期趨勢和動力）來利用萊特幣的波動。 該視頻強調測試和適應策略以適合個人交易方式和市場狀況的重要性。
</details>

<details>
<summary>052. END OF MONTH Trading Strategy (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=XJp8E3HmqG8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

the概述的交易策略是基於標準普爾500標準普爾500的每月交易信號的系統方法。這是一個簡明的摘要：

1. **入口點** ：該策略在每個月底的第五交易日結束時進入了較長的職位。

2. **出口點** ：它在下個月的第三交易日結束時退出了職位。

3. **投資頻率** ：該策略大約在33％的時間內投資，每月約有三分之一的職位。

4. **表現** ：儘管投資較少，但自1960年以來，它已經匹配或超過了購買和持有策略的回報，每年的收益約為7％。

5. **風險管理** ：最大縮水幅度明顯較小，是購買和保持方法的一半，從而降低了波動性風險。

6. **股權增長** ：股票曲線隨著時間的流逝而顯示出一致的增長，表明穩定的回報沒有超出預期市場行為的重大波動。

該策略旨在通過受控的進入和出口點來捕獲市場增長，同時減輕下行風險。
</details>

<details>
<summary>053. 3 Bollinger Band Trading Strategies (+Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=ZErni3FA24w&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

交易策略總結的重點是使用Bollinger Bands（一種流行的技術指標）來識別趨勢，衡量波動率並找到潛在的突破或平均歸還機會。 這是關鍵點的細分：

1. **了解布林樂隊** ：
   - Composed of three components: a middle band (simple moving average), an upper band, and a lower band.
   - The upper and lower bands are typically two standard deviations away from the middle band.
   - They help measure market volatility; widening bands indicate high volatility, while tightening bands suggest low volatility.

2. **通用交易技術** ：
   - **平均歸還策略** ：當價格關閉下方以下（兩個標準偏差）時輸入長時間，然後在中間頻段上方越過時退出。 對SPX進行的重新測試顯示出不同的結果，但由於大量下降而無法交易。
   - **布林樂隊擠壓** ：當頻帶擰緊（表明較低的波動率）時，它可能會標誌著爆炸性的移動。 但是，反測試發現整個資產的有用性有限。
   - **趨勢交易** ：使用布林樂隊通過觀察價格與樂隊的相互作用來識別潛在的突破或逆轉。

3. **平均歸還策略（優化）** ：
   - Use a 5-day moving average and reduce bands to 1.5 standard deviations.
   - Buy when SPX closes below the lower band and sell on strength when closing above the previous day's high.
   - This strategy achieved an annual return of 9% since 1993, with a win rate of 76%, invested only 25% of the time.

4. **優點和缺點** ：
   - **優點** ：易於理解，提供波動的見解，可以指示趨勢方向。
   - **缺點** ：基於樂隊的規則可能導致大量的縮減； 資產特定的行為需要量身定製的方法。

5. **常見錯誤** ：
   - Blindly following signals without considering the broader market trend or context.
   - Overlooking the need for backtesting and adapting strategies to different assets.

6. **其他考慮因素** ：
   - Different types of Bollinger Bands (e.g., percentage, bandwidth) exist but weren't detailed here.
   - Combining with other indicators can enhance effectiveness, but thorough backtesting is essential.

總而言之，儘管布林樂隊提供了寶貴的見解，但他們的成功取決於仔細的策略設計，進行回測以及對不同市場條件和資產的適應。
</details>

<details>
<summary>054. 3 Stochastics Trading Strategies 2024 (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=_PGzHyatvLI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻介紹了三種隨機交易策略，每種策略都有特定的規則和經過回頭測試的績效。 這是每種策略的簡明摘要：

1. **第一個策略** ：
   - Uses a 2-day fast stochastic value.
   - Buys when the close is at 25 or lower.
   - Sells on strength if the close exceeds yesterday's high.
   - Backtested on NASDAQ 100, yielding an average gain of 76% per trade and a 26% investment time.

2. **第二個策略** ：
   - Adjusts the lookback period from 2 to 3 days.
   - Buys when the fast stochastic crosses below 20.
   -使用與第一個策略相同的賣出觸發器。
   - Backtested on TLT (long-term treasury bonds ETF), resulting in a lower average gain compared to NASDAQ.

3. **第三策略** ：
   - Similar to the second but lowers the buy threshold to 15.
   - Applied to XLP (Consumer Staples ETF).
   - Produces fewer trades with a high average gain of 76%, low max drawdown of 12%, and high risk-adjusted return of 40%.
   - Invests only 8% of the time.

這些策略旨在滿足不同的投資方式，並根據風險承受能力和交易頻率提供選擇。 該視頻邀請觀眾參與評論部分進行進一步討論。
</details>

<details>
<summary>055. 3 Dual Momentum Trading Strategies</summary>

[[Youtube]](https://www.youtube.com/watch?v=_QN7zq1-elU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻討論了三種雙重動量交易策略，每個交易策略都具有不同的資產對和交易規則。 這是一個摘要：

1. **股票與債券（間諜和TLT）：** 
   - **交易規則：** 在每個月結束時，投資過去三個月表現更好的ETF（間諜或TLT）。
   - **表現：** 該策略的年度回報率為11.5％，最大降低為30％。 它的表現不足2020年後，但在市場穩定期間的表現通常都勝過。

2. **股票與黃金（間諜和GLD）：** 
   - **交易規則：** 與第一個策略類似，在三個月內投資了表現更好的資產。
   - **表現：** 該策略顯示出希望，尤其是在市場波動期間，具有更高回報的潛力，但在下降期間的風險也增加了。

3. **股票與現金（間諜和現金）：** 
   - **交易規則：** 分配監視如果超過現金； 否則，請保持現金。
   - **表現：** 該策略旨在平衡增長和安全。 與其他人相比，回報是適中的，但提供了一種保守的方法，並提供較低的縮水。

 **要點：** 
- 雙重動量策略依賴於資產對之間的相對性能。
- 它們易於實施，但不能保證產生利潤。
- 避免市場時機，減輕壓力和潛在的錯誤。
- 下降可能很重要，尤其是在市場崩潰期間。

該視頻強調了徹底的研究並將策略調整到個人投資目標的重要性。 它還強調，儘管這些策略很簡單，但它們並非沒有風險，需要仔細考慮。
</details>

<details>
<summary>056. 4 Overnight Trading Strategies (Night Trading)</summary>

[[Youtube]](https://www.youtube.com/watch?v=_XVib3RF9sU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

the視頻討論了一個針對Spy的隔夜交易策略，該策略是跟蹤標準普爾500標準普爾500的ETF。這是一個簡明的摘要：

1. **隔夜策略概述** ：
   - The strategy involves holding the S&P 500 from the market close to the next open.
   - Historical data shows that most gains occur during this period, providing an edge for overnight trading.

2. **第一交易規則** ：
   - If today is the third consecutive lower close, buy at close and sell at the next day's open.
   - Performance: 661 trades with an average gain of 0.13%, translating to annual returns of 2.8%. Only 8% investment time.

3. **通過保持關閉來改進** ：
   - Selling at the next day's close instead of open doubles gains, increasing the average gain to 0.24%.

4. **基於RSI的策略** ：
   - Buy if 2-day RSI drops below 10; sell at next open.
   - Performance: 741 trades, 62% win rate, average gain of 0.14%. 
   - Holding till close improves performance significantly due to compounding.

5. **結論** ：
   - Strategies can be tweaked for better results.
   - SPY's high price ($400+) helps offset costs like slippage and commissions.
   -該視頻邀請觀眾對建議發表評論。

總體而言，這些策略利用了過夜的回報和歷史模式，並具有自定義的空間。
</details>

<details>
<summary>057. Valentine&#39;s Day Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=_c09_6BV6sw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

提出的交易策略是基於 "Valentine's Day Rally," 這表明股票市場表現出截至2月14日的正常正回報。 這是該策略的摘要：

1. **進入和退出規則** ：
   - Enter long positions in February when the calendar day is the 10th or later.
   - Exit the trade on February 14th (Valentine's Day) at the market close, or on the first trading day after if February 14th is not a trading day.

2. **表現** ：
   - The strategy shows an upward equity curve in the S&P 500 since 1960.
   -在大約三個交易日內，每個交易的平均增長率約為0.35％，高於隨機的三天期。
   - Emerging Markets (e.g., ETF EEM) have shown stronger performance, with an average gain of 1.4%.

3. **結論** ：
   - The strategy suggests that markets, particularly emerging ones, tend to rally around Valentine's Day, potentially offering profitable opportunities for traders.

該演講鼓勵觀眾喜歡並訂閱更多的季節性交易模式，並提及基於學習規則的策略和課程的其他資源。
</details>

<details>
<summary>058. RAMADAN Trading Strategy (Muslim holiday Stock Market Effect)</summary>

[[Youtube]](https://www.youtube.com/watch?v=aUkSakgFVY0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

在齋月期間討論的交易策略涉及分析這個聖月期間的股票市場績效。 這是一個摘要：

1. **齋月概述** ：齋月是一個重要的穆斯林假期，每年在格裡高利日曆中有所不同。 該戰略著重於齋月廣泛慶祝的國家，例如沙烏地阿拉伯，土耳其和埃及。

2. **戰略** ：
   - If Ramadan starts on a weekend, buy the S&P 500 (or ETFs representing countries celebrating Ramadan) on the following Monday.
   - Sell after the holiday ends.
   -理由是在此期間利用潛在的市場發展。

3. **表現** ：
   - In the U.S., the strategy yielded an annual return of approximately 1.1%, slightly better than a "Buy and Hold" 方法，但沒有顯著優越。
   - When tested on ETFs from Saudi Arabia (KSA), Egypt (EGPT), and Turkey (2R), the performance was flat over 15 years.

4. **結論** ：
   - The strategy shows modest returns in the U.S. but lacks strong performance in Muslim countries.
   - It is presented as one of many strategies available on their website, encouraging viewers to explore further.

該策略可能不是高效的，但為在特定假期期間對市場行為感興趣的交易者提供了另一種方法。
</details>

<details>
<summary>059. 3 Top Bitcoin Trading Strategies (Backtest Results)</summary>

[[Youtube]](https://www.youtube.com/watch?v=cSHNnwcMIO8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻介紹了三種比特幣交易策略，每種策略基於不同的原則：

1. **MACD直方圖策略** ：此策略使用MACD（移動平均收斂差異）直方圖生成買賣信號。 直方圖計算為MACD線和信號線之間的差異。 當直方圖呈正變量時，產生了買入信號，並且當它變成負面時，會觸發賣出信號。 進行回測的表明，該策略的表現優於購買和持有的方法，年收益率為77％，而61％的收益僅為54％。

2. **25天的突破策略** ：這種基於勢頭的策略涉及購買比特幣的價格超過前25天的收盤價，並且在該水平以下時出售。 該策略的獲勝率較低（約43％），但仍然產生可靠的回報，平均年收益高於持有比特幣。 它使交易者僅投資56％的時間。

3. **季節性模式策略** ：該策略是基於在一個月的第五到持久的交易日購買比特幣，並在下個月的第三交易日出售。 進行回測的表明表現強勁，平均年收益率近41％，而僅投資23％的時間。 但是，最近的表現一直在變平。

該視頻結束了，邀請觀眾探索其網站上的更多策略，量化策略，並通過喜歡，訂閱和評論來鼓勵參與。
</details>

<details>
<summary>060. 200-Day MA Strategy (Backtest, Rules And Performance)</summary>

[[Youtube]](https://www.youtube.com/watch?v=dEZ6Wy_EYmU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該交易策略總結了使用200天的移動平均線（MA）作為關鍵指標，其靈感來自Paul Tudor Jones。 這是一個簡潔的崩潰：

1. **趨勢遵循策略** ：
   - **進入信號** ：當標準普爾500指數高於其200天MA時，投資。
   - **退出信號** ：當指數低於此平均水平時出售。
   - Performance: Since 1960, excluding dividends, this strategy has yielded a 6.75% annualized return versus buy-and-hold's 7%. It notably reduces drawdowns (28% max vs. 56% for buy-and-hold) by avoiding severe market crashes, such as the 2008 financial crisis.

2. **過濾短期交易** ：
   - **平均歸還策略** ：交易者可以使用標準的平均回歸方法，例如，當RSI低於35且出售50以上時購買。
   - However, this strategy has a high max drawdown (29%), making it challenging for traders to adhere to.

3. **與200天的MA結合** ：
   - Adding the 200-day MA as a filter improves returns by reducing volatility and increasing the win rate. Trades are taken only when above the MA, leading to fewer trades but higher average gains per trade and better win rates.

4. **性能比較** ：
   - Traders below the MA experience more erratic performance due to higher volatility, which is less favorable for sustained trading success.

5. **結論** ：
該策略利用簡單性和趨勢範圍來提高風險調整後的回報。 雖然它在原始回報中可能不會超越購買和持有的效果，但其較低的跌幅提供了一種更安全的方法，具有更複雜的收益。 200天的MA既是趨勢指標，也是均值回歸策略的過濾器，使其成為交易者的多功能工具。

該策略強調了與市場趨勢保持一致的重要性，同時降低波動性，強調了交易系統中簡單性的價值。
</details>

<details>
<summary>061. Oversold Trading Strategy (What Happens When Stock Markets Are Oversold?)</summary>

[[Youtube]](https://www.youtube.com/watch?v=few_gh6Td8E&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點是使用相對強度指數（RSI）指標來確定股票市場中的超售條件。 這是關鍵點的摘要：

1. **過多的狀況** ：該策略將超售市場定義為經歷了一段時間價格下跌的市場，通常在每日交易框架上進行五天。

2. **RSI指標** ：RSI用於測量價格變動的速度。 當RSI值低於20時，它表明條件過多，表明證券被低估和潛在的向上移動。

3. **交易規則** ：
   - **入口** ：當三天的RSI低於20時，在關閉時購買SPX（S＆P 500）。
   - **出口** ：在N天或第二天的價格高於昨天的高點時出售，以先到者為準。

4. **後退測試結果** ：
   - The strategy shows steady equity growth from $100,000 to $1.3 million over the tested period.
   - Annualized returns of 9.14% with low drawdowns.
   - Risk-adjusted return calculated as 54 (annual return divided by time in the market).

5. **結論** ：該策略表明，在超售條件下可以預期較高的短期回報，這是希望利用平均歸還的交易者的潛在有效方法。

該摘要強調了一種基於超售條件和RSI的系統交易方法，旨在通過選擇性的市場參與來最大化風險調整後的收益。
</details>

<details>
<summary>062. 6 Larry Connors Trading Strategies</summary>

[[Youtube]](https://www.youtube.com/watch?v=gX8FjjKR7ec&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略基於拉裡·康納斯（Larry Connors）及其團隊開發的交易策略，並進行了修改以提高績效。 這是每種策略的簡明摘要：

1. **雙五交易策略** ：
   - Enter when the close is above the 200-day moving average (DMA) and at a five-day low.
   - Exit when the close is at a five-day high.
   - Produces more trades than the original Double Seven, with an average gain of 0.65% and moderate drawdowns.

2. **多天和多天下降** ：
   -在200-DMA上方，在5-DMA以下，並在過去五天中至少四個下降後輸入。
   - Exit when the close is above the previous high or low.
   - Offers a 4.8% annual return with limited market exposure.

3. **RSI 30/50策略** ：
   - Enter when above the 200-DMA and the 5-day RSI is below 30.
   - Exit when the 5-day RSI crosses above 50.
   - Provides a strong risk-adjusted return of 52% with high win rates.

4. **三天的高/低策略** ：
   - Enter when above the 200-DMA and both high and low have trended lower for three consecutive days.
   -進入後的下一個關閉，或者關閉時間低於前一天的關閉。
   - Results in a 3.6% annual return with minimal market exposure.

5. **關鍵要點** ：
   - Mean reversion strategies (buying dips) have been effective since 1985.
   - The 200-DMA effectively filters out Bull and Bear markets, limiting drawdowns to around 14% for all strategies.
   - Strategies often remain on the sidelines, allowing potential for complementary trading.
   - Avoid combining all six strategies into a portfolio due to similarity, which can reduce effectiveness.

These strategies emphasize紀律性、風險管理，並依賴於歷史數據的有效性。 在實施前，建議進行充分的測試和評估。
</details>

<details>
<summary>063. 3 Profitable Trading Strategies (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=j1qjX0Zxpd0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻介紹了三種交易策略，每種交易策略都採用獨特的方法，並突出了將它們組合為多元化投資組合的好處。 這是一個簡明的摘要：

1. **橡皮筋策略（均值歸還）：** 
   - **機制：** 當價格低時購買並在高價時出售。
   - **表現：** 顯示到2015年的強勁回報，投資價值為10萬美元，增長了87萬美元以上，年收益率為7.4％。 風險調整後的回報率為51％，僅在14％的時間內活躍。

2. **黃金交叉戰略（趨勢之後）：** 
   - **機制：** 使用50天和200天的移動平均值來表示趨勢變化。
   - **表現：** 與買賣相比，下降較低，收益略低，但在熊市中的風險大大降低。

3. **結合策略：** 
   - **方法：** 結合了標準普爾500指數和納斯達克100的兩種策略，增強了回報，而不會增加降低。
   - **表現：** 獲得了更高的年收益（例如，13.6％vs. 9.1％），積極交易的時間約為71％。

 **關鍵要點：** 
- 跨策略和資產類別的多元化對於持續的盈利能力至關重要。
- 沒有策略永遠存在； 持續監控和適應至關重要。
- 避免曲線擬合，這會導致現實世界中的性能不佳。

該視頻強調了一種多元化的方法，使用具有不同市場暴露，時間範圍和方向的多種策略來優化回報，同時管理風險。
</details>

<details>
<summary>064. Stairs Trading Strategy (A Trend &amp; Pullback Combo) | +Backtest</summary>

[[Youtube]](https://www.youtube.com/watch?v=jk2RxsVKA6Y&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

此摘要概述了 "Stairs Trading Strategy" 作為複雜交易方法的更簡單替代品。 這是一個簡潔的崩潰：

1. **概念** ：該策略是基於資產價格以樓梯狀模式移動的想法，每個步驟都代表關鍵支持或阻力水平。

2. **規則** ：
   - **進入條件** ：
     - Close must be above the 200-day moving average.
     - Close must be below the 25-day moving average.
     - Enter at the close when both conditions are met.
   - **退出條件** ：當價格超過25天移動平均線時退出。

3. **表現** ：
   - Annual return of 6.1% compared to a Buy and Hold strategy's 7.7%.
   - Lower drawdowns (consistently below 20%) with an investment time of only 23% of the period.

4. **執行** ：
   - The trading strategy code is available for free on their website.
   - Additional resources, including another video, are recommended for further learning.

5. **打電話給行動** ：鼓勵觀眾喜歡，訂閱並參與將來的內容以獲得更多的交易策略。

該策略旨在通過專注於移動平均值和降低複雜性來簡化交易，從而通過有限的市場參與來提供較低的風險。
</details>

<details>
<summary>065. 5 Swing Trading Strategies 2024 (Backtest And Settings)</summary>

[[Youtube]](https://www.youtube.com/watch?v=kWgUlIFAwqg&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻介紹了五種經過驗證和經過驗證的搖擺交易策略，每個策略都有不同的規則和績效指標。 這是一個簡明的摘要：

1. **第一個策略** ：當每日範圍低於前六天時購買，並關閉超過200天移動平均線。 離過去高高的接近距離。 它的年收益率為14.1％，股權從$ 10萬美元增長到530萬美元，只有三年的損失年（2011年，2015年，2018年）。

2. **第二個策略** ：涉及購買高點是一個新的10天峰值，而IBS <0.15。 股票曲線顯示出一致的增長，而最小的下降。

3. **第三策略** ：利用範圍和移動的平均過濾器進入交易，在低收納下，年收益率為3.24％。

4. **第四策略** ：結合了多個進入的指標，但專注於相同的退出信號，從而導致了中等數量的交易和一致的回報。

5. **第五策略** ：結合了IBS和高過濾器以進入交易，每次交易的平均增長率為0.6％，而投資時間很少。

合併後，所有五種策略一次一次分配給一個職位，產生了令人印象深刻的結果：10萬美元增長到530萬美元，只有三年損失的年份，並且表現優於傳統的買入和投資，尤其是在2008年和2022年的動蕩市場中。

該視頻結束時強調結合提高性能的策略的力量，並建議在其網站上探索其他策略。

有關每種策略的更多詳細信息或訪問其他資源，請訪問其網站。 祝您好運交易！
</details>

<details>
<summary>066. 3 Swing Trading Strategies 2024 (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=lKzoUptU2io&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

提出的交易策略是標準普爾500指數的一種搖擺交易方法，涉及三種不同的策略合併為投資組合。 這是一個簡明的摘要：

1. **策略一** ：賣出今天的關閉時，賣出比昨天的高點，此後連續兩個下關閉。

2. **策略二** ：出售如果今天的關閉設置為新的5天低點，而IBS指標低於0.25； 當今天的閉幕超過昨天的高點時退出。

3. **策略三** ：出售如果今天的盤中高點低於前一天的10天高，而IBS不到0.15； 當今天的關閉超過昨天的高點時退出。

結合這些策略會導致投資組合的表現優於購買和持有的投資，而活躍的投資僅為27％。 網站上也有類似的策略。
</details>

<details>
<summary>067. Simple VOLATILITY Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=lPhVdBHQfHE&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

有關的交易策略圍繞利用市場波動，並利用200天的移動平均線作為市場制度過濾器。 這是一個簡明的摘要：

1. **市場制度過濾器** ：200天移動平均線用於確定市場是看漲（高於平均水平）還是看跌（低於平均水平）。

2. **波動性考慮** ：該策略承認，在熊市期間，波動率往往會增加，這與股價下降相關。

3. **績效分析** ：對測試表明，與低波動性相比，該策略在高波動率時期的表現更好。

4. **交易方法** ：而不是專注於是否基於市場制度（Bull還是Bear）購買還是出售，而是遵守該戰略產生的交易信號。 這些信號旨在解決市場狀況，因此不需要明確調整公牛或熊市。

從本質上講，該戰略強調遵循預定義的交易信號，而沒有過度複雜的市場方向決定，因為系統適應了不同的波動水平和市場制度。
</details>

<details>
<summary>068. Gold Trading Strategy (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=mic1SPbN7cA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點是利用黃金和黃金開採部門的隔夜優勢。 這是一個簡明的摘要：

1. **大體時間** ：該策略涉及從市場接近到第二天開放的職位，通常不到24小時。

2. **涉及的資產** ：
   - GDX: ETF tracking gold miners.
   - GLD: ETF tracking gold prices.

3. **表現** ：
   - From close to next open, both GDX and GLD show positive trends with a stable upward slope.
   - Conversely, buying at market open and selling at close results in losses, as the intraday returns have been slightly negative on average.

4. **邊緣細節** ：
   - The overnight edge is small but consistent.
   - It's not large enough to trade on its own but serves as a solid foundation for more robust strategies.

5. **增強** ：
   - By adding two variables, the strategy demonstrates a rising slope and has been consistently profitable for nearly two decades.

6. **結論** ：
   - The strategy is provided to paying subscribers.
   - Encouragement to visit their website for more details.
   - Final message includes a call to action for likes and subscriptions, with good luck trading wishes.

這種方法強調了利用市場中較小但一致的邊緣的重要性，再加上其他變量以提高盈利能力。
</details>

<details>
<summary>069. DEMARKER TRADING STRATEGY  (BACKTEST)</summary>

[[Youtube]](https://www.youtube.com/watch?v=o_rgI0h9Qs8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

交易策略涉及使用市場指標來識別過分買賣的水平。 優化間諜後，確定了最佳參數：5天的回顧期為5％，賣出閾值為80％。 但是，這種初始方法導致了大量的下降。 為了提高性能，進行了兩個修改：

1. **出售狀況** ：而不是僅僅依靠指標達到80％，而是關閉交易，當時交易已關閉：
   - The close crosses above yesterday's high (indicating strength).
   -關閉量低於昨天的低點（表明弱點）。

2. **趨勢線檢查** ：添加了一個額外的條件，即根據趨勢線以上還是低於趨勢線的價格下跌或關閉交易。

股票曲線表明，這些修改減少了縮減並提高了整體盈利能力，從而實現了更強大的策略。 最終的方法是在指標達到5％並在與價格強度和趨勢線路中斷有關的指定條件下出售時購買。
</details>

<details>
<summary>070. The Failed Bounce Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=oh07KVESvjk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略稱為 "Failed Bounce" 戰略。 這是其要點的摘要：

1. **條目規則** ：
   - Yesterday's IBS (Internal Bar Strength) must be at least 0.6 or higher.
   - Yesterday's low should be lower than the lowest low from the previous five days.

2. **退出規則** ：
   - Exit when today's close is higher than yesterday's high.

3. **表現** ：
   - The strategy has been tested on stocks since the late 1980s.
   - Out of 204 trades, 77% were winners with an average return of 0.86% per trade.
   -淨利潤為450％，導致每年5.8％的收益。

4. **風險調整後的回報** ：
   - The strategy is invested only 8.5% of the time, yielding a risk-adjusted return of 67%.

5. **適用性** ：
   - Works on ETFs based on stocks but not Commodities or bonds.
   - Performed well on QQQ with a 1% average per trade.

6. **其他信息** ：
   - The IBS indicator is emphasized as highly underrated.
   - Strategy codes and backtests are available on the website's resource library.

該策略對於短期交易似乎有效，專注於根據特定的內部槓鈴標準確定潛在的價格變動。
</details>

<details>
<summary>071. Golden Cross Trading Strategy (Guide+Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=okJHlykwQYo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略基於金交叉指示器，該指示器涉及使用超過200天移動平均線的50天移動平均線，以發出看漲的突破（買信號），並在其下方交叉以發出看跌的突破（賣出信號）。 該策略旨在最大程度地減少熊市市場期間的損失，並最大程度地利用牛市的收益。

摘要的要點：
1. **金交叉指示器** ：
   - A short-term moving average (50-day) crossing above a long-term moving average (200-day) indicates a bullish trend, prompting a buy.
   -相反，如果50天的交叉點低於200天，它標誌著看跌趨勢，促使賣出。

2. **表現** ：
   - Backtested on the S&P 500 from 1960 onwards, resulting in 32 trades held for approximately 350 days each.
   - 78% of trades were winners with an average gain of 15.4% and an annual return of 6.6%.
   - The strategy was only active 69% of the time compared to buy-and-hold, which is active 100% of the time.

3. **風險調整後的回報** ：
   - Lower drawdowns (33%) compared to buy-and-hold (56%), leading to a better risk-adjusted return of 9.5%.
   -該戰略旨在減少熊市市場期間的損失，同時利用牛市的增長。

4. **其他策略** ：
   - Mentioned the short-term NR7 strategy as another system that complements this approach.

有關更多詳細信息，包括代碼和其他策略，消息人士建議訪問量化strategies.com。
</details>

<details>
<summary>072. Doji Reversal Trading Strategy (Backtest + Candlesticks Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=p3St7_mOOOI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的交易策略圍繞著利用Doji燭臺模式來確定市場上的潛在逆轉。 這是一個結構化的摘要和分析：

1. **Doji燭臺** ：這些特徵是小物體和長上下陰影，表明買賣雙方之間的猶豫不決。 有四種類型：中性，墓碑，蜻蜓和長腿的Doji。

2. **交易策略** ：
   - **進入信號** ：在出現四種DOJI模式之一時購買。
   - **初始退出規則** ：在五個交易日期後出售，導致每次交易的平均收益為0.28％，略高於隨機時期。
   - **改進的退出規則** ：
     - Sell if the close is higher than yesterday's high, exploiting mean reversion.
     - Incorporate a 5-day RSI filter (below 50) to buy only when the market is oversold.

3. **表現** ：
   - The initial strategy showed an average gain of 0.28% with holding periods up to five days.
   - Adding an exit rule based on closing prices higher than yesterday's high improved performance but didn't linearize the equity curve, indicating potential volatility.
   - Implementing the RSI filter reduced trade frequency but increased average gains to 0.54%, though it didn't notably improve the equity curve.

4. **考慮和關注** ：
   - **反測試限制** ：有過度適應歷史數據的風險，可能會降低現實世界的可靠性。
   - **交易成本** ：頻繁的交易可能會產生大量的費用和滑倒。
   - **波動和縮減** ：該策略可能涉及大量的市場波動和下降，從而影響風險承受能力。
   - **市場狀況** ：在不同的市場環境中有效性可能會有所不同（例如，趨勢與市場趨勢）。
   - **機會成本** ：持有65％的現金可能意味著會錯過強勁上升趨勢的較大收益。

5. **結論** ：
儘管該策略通過系統的規則和超越隨意的結果表現出希望，但考慮到現實世界中的因素，例如交易成本，波動性和不同市場狀況，這一點很重要。 對不同資產和時間表進行歷史績效和測試的進一步研究可以提供更深入的見解。 將此策略與其他指標相結合可能會提高可靠性，但增加了複雜性。

總而言之，基於DOJI的策略提供了一種結構化的交易方法，但交易者應注意其在現實世界應用中的局限性和潛在風險。
</details>

<details>
<summary>073. EASTER Trading Strategy (Holiday Effect in The Stock Market)</summary>

[[Youtube]](https://www.youtube.com/watch?v=pL9F9DSIOVg&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中提出的交易策略重點是在復活節相關的假期中利用市場趨勢，特別是耶穌受難日和聖周四。 這是提到的兩種策略的摘要：

1. **復活節策略** ：
   - **入口** ：在耶穌受難日之前在周五關閉。
   - **出口** ：在幾天後四個交易的聖周四結束時出售。
   - **表現** ：超過63年，該策略的平均每行業增益為0.77％，自2000年以來顯著提高到1.49％。與收益相比，損失相對較小。

2. **神聖的星期四策略** ：
   - **入口** ：在復活節周的周三結束時購買。
   - **出口** ：第二天結束時出售，這是神聖的星期四。
   - **表現** ：該策略僅持有24小時，但已經過63次交易測試，平均收益為0.35％，獲勝率為68％，利潤係數為4.1。

該視頻表明，這兩種策略均基於歷史數據顯示在這些假期期間的積極表現，這使與復活節相關的交易機會是一年中最佳的美國股票交易的日子。
</details>

<details>
<summary>074. Closed-End Fund Strategy: Lower Risk, Higher Reward</summary>

[[Youtube]](https://www.youtube.com/watch?v=qL9gnzI5Akc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

所討論的交易策略是為封閉式基金（CEF）設計的，並著重於減少市場敞口，以最大程度地減少虧損，同時旨在獲得可觀的回報。 這是一個簡明的摘要：

1. **策略概述** ：
   - The strategy uses the daily price-to-NAV ratio of CEFs and applies a 2-day Relative Strength Index (RSI) to determine entry and exit points.
   
2. **進入和退出規則** ：
   - Enter a long position when the 2-day RSI of the price-to-NAV ratio crosses below 10, indicating potential undervaluation.
   -當2天的RSI越過60以上時，退出貿易，表明高估。

3. **性能指標** ：
   - Backtesting with fund ticker EtG resulted in 212 trades, an average gain of 48%, and a time spent in the market at 133% (indicating limited holding periods).
   - Maximum drawdown was 26%, significantly lower than buy-and-hold's 74%.

4. **客觀的** ：
   - To reduce market exposure by holding positions only when signaled, aiming for higher returns with lower risk compared to a passive approach.

5. **考慮因素** ：
   - RSI signals may fail in trending markets; strategy specificity to CEFs suggests possible limitations outside this asset class.
   - Backtest results do not guarantee future performance.

本質上，該戰略試圖利用使用動量指標來利用與NAV相對於NAV的短期價格差異，旨在有效地進行風險降低的有效交易。
</details>

<details>
<summary>075. These Are The Worst Stocks To Buy - Keep Away</summary>

[[Youtube]](https://www.youtube.com/watch?v=qqiONddSlOs&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

總結的交易策略是避免投資於市場價值較低且波動較高的股票，因為自從總統約翰·甘迺迪（John F. Kennedy）上任以來，這些股票的表現不佳。 具體而言，該策略強調了遠離具有不確定商業模式的一分錢股票和小型股票的轉向，這些股票通常會產生負收益。 建議是專注於排除這種波動和冒險的投資，以提高整體投資組合績效，與納西姆·塔萊布（Nassim Taleb）的想法保持一致，即避免壞事與尋求善良一樣有價值。
</details>

<details>
<summary>076. 8 Quantitative Trading Strategies | (Backtests, Settings and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=rlSkRMmycWo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

該視頻介紹了八種定量交易策略，每個策略都有自己的一組規則，示例和回測結果。 這是每種策略的簡明摘要：

1. **羅素重新平衡策略** ：
   - Buys Russell 2000 on the first trading day after June 23rd and sells it on the first trading day of July.
   - Average return: 1.3% per trade, with consistent performance.

2. **長期財政債券季節性策略** ：
   - Trades long-term treasury bonds using a specific ETF (TLT).
   - Annual returns: 9.8%, doubling buy-and-hold at 4.5%. 
   -僅投資56％的時間，表現出色。

3. **間諜定量交易策略** ：
   - Focuses on SPY (S&P 500 ETF) with a systematic approach.
   - Annual returns: 6.1%, with modest drawdowns and limited trading frequency (8% invested time).

4. **納斯達克100定量策略** ：
   - Targets QQQ (Nasdaq 100 ETF).
   - Higher performance than SPY, with annual returns of 11.6%, surpassing buy-and-hold at 8.6%.

5. **長期債券季節性策略** ：
   - Similar to the eighth strategy but focuses on different aspects or timeframes.
   -高回報以大量的投資時間。

6. **定量交易捆綁示例** ：
   - A portfolio combining three long and three short strategies.
   - Annual return: 25% since 2016, with small drawdowns.

### 關鍵要點：
- **優點** ：自動化允許多種策略而無需不斷監視，減少情感決策，並可以有效擴展。
- **缺點** ：需要編碼知識，策略發展經驗以及維護和更新系統的持續努力。

該視頻強調，定量交易是可以訪問的，但需要一種系統的方法和學習意願。 它突出了簡單在策略中對長期盈利能力的重要性。
</details>

<details>
<summary>077. Stocks vs Interest Rates Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=ro4ck8Z1rYw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

提出的交易策略基於債券市場與股票價格之間的反比關係，尤其是專注於美國財政債券（TLT）和標準普爾500 ETF（SPY）。 這是一個簡明的摘要：

1. **關鍵洞察力** ：當長期債券價格上漲（表明利率下降）時，與固定收入證券相比，股價往往會上漲，因為較低的利率使股票更具吸引力。

2. **策略概述** ：
   - **購買信號** ：當TLT超過其15天移動平均線時，進入股票市場。
   - **賣出信號** ：當TLT越過其15天移動平均線以下時退出股市。

3. **進行回測結果** ：
   - The strategy was tested with different moving averages (ranging from 5 to 100 days).
   - The 15-day moving average showed a consistent performance, with an annual return of approximately 8.85% despite being invested only about 54% of the time.
   - Average gain per trade was 0.51%, and the maximum drawdown was 31%.

4. **結論** ：該戰略利用債券與股票之間的反比關係，基於債券價格變動的時機市場參賽和退出，以利用股票可能上升的時期。

這種方法旨在從債券市場與股票績效之間的相關性中獲利，從而通過跟蹤債券趨勢來優化投資決策。
</details>

<details>
<summary>078. OPEX Trading Strategy (Backtest &amp; Results)</summary>

[[Youtube]](https://www.youtube.com/watch?v=sDOfLm6Y6G4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略重點是利用期權到期周（OPEX WEEK）效應，該效應發生在期權到期時發生。 這是關鍵點的簡明摘要：

1. **OPEX周概述** ：
   - Options expire on the third Friday of each month, known as Opex Day.
   - The days leading up to expiration can cause volatility due to traders adjusting positions.

2. **提出的策略** ：
   - **策略1** ：在OPEX周的周一公開賽中購買間諜（標準普爾500 ETF），並在OPEX日結束時出售。 結果顯示，隨著時間的流逝，每周的平均收益高於其他幾周的平均收益。
   - **策略2** ：付費成員獨有，涉及國防部（XLV）和公用事業（XLU）等國防部的交易部門。 它以較小的投資時間和正平均收益取得了良好的表現。
   - **策略3** ：在OPEX Day開放時間諜，並在結束時掩蓋。 該策略利用了到期日的長位置上的潛在弱點，顯示短交易的平均增長。

3. **關鍵概念** ：
   - **引腳風險** ：與即將到期的期權合同相關的風險。
   - **四人女巫日** ：多個衍生合同到期，增加市場波動的一天。

4. **性能指標** ：
   - Strategies vary in returns and investment time, but all show potential profitability when combined with additional parameters.

5. **結論** ：雖然不是獨立的解決方案，但這些策略可以成為OPEX周期間更廣泛的交易方法的一部分，從而通過了解市場行為和波動性為利潤提供了機會。
</details>

<details>
<summary>079. Heiken Ashi Candlestick Trading Strategy: (Backtest + Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=sG6Gsxf0I5o&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的交易策略圍繞著使用Hikanashi（也拼寫為Haikinashi）蠟燭作為趨勢跟隨指標。 這是一個簡明的摘要：

1. **什麼是Hikanashi？**   
   - It’s a charting technique originating from Japan, introduced to the West in the late 1980s.
   - Unlike traditional Japanese candlesticks, Hikanashi uses smoothed average prices (open, high, low, close) to highlight trends and consolidation phases.
   - The open price of each Hikanashi candle is the midpoint of the previous candle's body, eliminating gaps.

2. **關鍵功能** ：
   - It’s a lagging indicator and not based on real-time prices.
   - Useful for smoothing out price noise and identifying directional trends.
   - Best suited for long time frames (e.g., monthly bars).

3. **交易策略** ：
   - **進入信號** ：購買時，山脈蠟燭的結尾在其敞開上方越過。
   - **退出信號** ：賣出閉合點以下時出售。
   - Tested on the S&P 500 index using monthly data from 1960 to present.

4. **性能指標** ：
   - Annual return: ~4.77% (vs. Buy & Hold at ~7%).
   -與購買和持有相比（約53％），最大降低（〜30％）較低，這使其風險降低。

5. **建議** ：
   - Backtest any strategy before risking real money.
   - Combine with other indicators for enhanced results.

總之，Hikanashi可以成為趨勢跟隨策略的寶貴工具，尤其是在較長的時間範圍內，但是要進行回歸併將其與其他技術一起使用以獲得最佳性能。
</details>

<details>
<summary>080. Sugar Futures TRADING STRATEGY (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=sH70Ldu5YOQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略涉及使用350天移動平均線（MA）作為主要指標，並增加了7天的平均真實範圍（ATR）來產生買賣信號。 這是一個簡潔的崩潰：

1. **購買信號** ：當價格超過350天MA加7天ATR時，啟動長位置。
2. **賣出信號** ：退出交易或當價格低於350天MA以下7天ATR時會縮短。

該策略旨在利用趨勢，因為它使用了長期移動平均線，並結合了波動率（通過ATR）來過濾信號。 但是，創造者由於其複雜性和與健康相關和財務的潛在風險而對交易糖表示懷疑。 他們警告不要在沒有徹底研究的情況下使用此策略，並建議訪問其網站以獲取更多信息或訂閱其渠道以進行更新。
</details>

<details>
<summary>081. A SIMPLE Trading Strategy With A 91.03% Win Rate</summary>

[[Youtube]](https://www.youtube.com/watch?v=shgOIrJdj8s&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

所討論的策略稱為Triple RSI交易策略，該策略的重點是在股票市場長期上升趨勢中利用短期回調。 這是一個簡明的摘要：

1. **客觀的** ：
   - The strategy aims to capitalize on short-term price corrections (pullbacks) during an uptrend, leveraging the Relative Strength Index (RSI).

2. **基礎理論** ：
   - The U.S. stock market tends to rise over time due to inflation and productivity gains, but periodic pullbacks present trading opportunities.

3. **樂器** ：
   - Uses the S&P 500 (ETF: SPY) as a proxy for the broader market.

4. **條目規則** ：
   - RSI(5) must be below 30.
   - The RSI reading has been decreasing for three consecutive days.
   - RSI(5) was below 63 trading days ago.
   - The closing price is above the 200-day moving average (as a trend filter).

5. **退出規則** ：
   - Exit when RSI(5) rises above 50.

6. **表現** ：
   - Backtested from 1993 to the present, resulting in 78 trades with an average gain of 1.4% per trade.
   - 91% of trades were profitable, with an average holding period of six days.

7. **結論** ：
   - The strategy is deemed effective for short-term trading within a rising trend, offering consistent profitability and limited holding periods.

有關更多信息或其他策略，請訪問 [jenterifiedstrategies.com](https://quantifiedstrategies.com).
</details>

<details>
<summary>082. Coppock Curve Trading Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=tnUZLLUGpo8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

COPIC曲線策略是一種基於動量指標的交易方法，該方法由經濟學家COPIC在1960年代開發出來。 它使用兩個變化速率值的加權移動平均值（11和14）來確定股票市場的長期趨勢，代表早期和晚期上升階段。

 **關鍵功能：** 
- **指標計算：** 結合了11個周期和14個周期變化率（ROC）指標。
- **交易規則：** 
  - Buy when the Copic Curve crosses above its 10-month moving average.
  - Sell when the Copic Curve crosses below its 10-month moving average.

 **性能亮點：** 
- 從1960年至2023年對標準普爾500指數進行了反測試。
- 平均年收益率為6.11％對標準普爾7.03％。
- 與標準普爾52.56％相比，較低的最大減收率（3.16％）。
- 比標準普爾7.03％的風險調整後的回報率高（8.29％）。

 **結論：** 
Copic曲線策略提供了一種簡單，長期的方法，並降低了風險，使其適合尋求保守而有效策略的投資者。
</details>

<details>
<summary>083. Small Cap Effect Strategy: Outperform 99% Of Investors</summary>

[[Youtube]](https://www.youtube.com/watch?v=vwKX101clTU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略圍繞著 "small cap effect," 這強調了較小的公司在長期內傾向於勝過較大的公司。 這種現象是FAMA法國三因素模型的關鍵組成部分，該模型解釋了庫存根據規模，價值和質量因素的回報。

策略的要點包括：

1. **小上限保費** ：從歷史上看，小型股票的表現優於大型股票，尤其是在避免揮發性最大的小型股問題時。
2. **價值超過增長** ：在小型股票中，自1940年以來，具有價值取向的人（例如，較低的市盈率）在歷史上超過了面向增長的股票。
3. **質量因素** ：通過魯棒性等因素衡量，投資高質量的小型股票，與非質量股票相比，長期收益很高。

該策略強調了長期投資的重要性，並表明，由於這些因素，即使是適度的初始投資也可以隨著時間的推移而大幅增長。
</details>

<details>
<summary>084. Best Bitcoin Trading Strategy (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=xSpWak84AjA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

討論的交易策略是比特幣動量交易方法。 這是一個簡明的摘要：

1. **動量交易基礎知識** ：
   - Involves buying or selling based on the strength of recent price trends.
   - Identifies upward or downward trends to take positions accordingly.

2. **比特幣策略** ：
   - Triggers for trades are determined by whether the closing price crosses above or below a 25-day high of the close.
   - Long position is taken when the close crosses above this threshold, and short when it falls below.

3. **性能指標** ：
   - Backtested results show 179 trades with an average gain of 2.35% per trade.
   - Compound Annual Growth Rate (CAGR) is 55.7%, indicating significant potential profitability.
   - Maximum drawdown is 23%, highlighting the risk involved.

該策略利用比特幣中的價格動力來利用趨勢，並有可能提供可管理的風險概況的大量回報，如所提供的指標所示。
</details>

<details>
<summary>085. Crude Oil Trading Strategies (Backtest &amp; Settings)</summary>

[[Youtube]](https://www.youtube.com/watch?v=xkEKJ7GJnt0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

原油的交易策略涉及四個關鍵步驟：

1. **計算25天平均真實範圍（ATR）** ：ATR是使用每天在25天內的每日高低低價計算的。

2. **特定日子交易** ：交易者只能在星期二和周四執行交易。

3. **確定入口點** ：當今天的收盤價低於昨天的收盤價至少一個ATR時，請進入一個較短的位置。

4. **退出交易** ：在下一個交易日結束時關閉交易。

 **績效分析** ：
- 該策略已使用原油期貨合約對歷史數據進行了測試。
- 這導致了341筆交易，平均每次交易增益為0.25美元。
- 獲勝率為58％，表明盈利和虧損的交易數量均衡。
- 平均獲勝貿易超過了平均損失貿易。

 **進行回測的重要性** ：
- 進行回測，可以使用歷史數據評估策略的有效性，從而幫助交易者做出明智的決定。
- 它確定了優勢和劣勢，可以進行必要的調整以避免昂貴的錯誤。

總而言之，儘管原油交易具有巨大的潛力，但成功需要一項經過深入研究的策略，並得到了徹底的回測。
</details>

<details>
<summary>086. SECTOR ROTATION Trading Strategy (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=yOvQBxyqX2E&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的行業輪換交易策略涉及在過去一個月的相對績效基於四個特定領域（SP 500，長期債券，國際發展股票和新興市場股票）之間進行系統旋轉的投資。 這是該戰略的簡明摘要：

1. **客觀的** ：通過利用部門績效趨勢來產生一致的回報。

2. **專注於行業** ：
   - SP 500 (SPY)
   - Long-term Bonds (TLT)
   - International Developed Stocks (EFA)
   -新興市場股票（EEM）

3. **過程** ：
   - **計算相對強度** ：在過去一個月中評估每個部門的表現。
   - **選擇頂級表現** ：投資與表現最佳部門相對應的ETF。
   - **保持位置** ：維持這項投資一個月。
   - **旋轉** ：保持後，重新計算相對強度並旋轉到新的表現最佳扇區。

4. **情緒超脫** ：該策略依賴於數據，而不是市場預測或情感決策。

5. **進行回測** ：使用歷史數據對其有效性進行嚴格測試。

6. **結論** ：該方法作為一種可靠的，數據驅動的方法，用於尋求系統的行業交易策略的交易者。

該視頻還邀請觀眾探索相關策略，例如範圍交易，並強調證明和測試在交易中的重要性。
</details>

<details>
<summary>087. CCI Trading Strategy (Backtest &amp; Trading Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zFldiNwEsKo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

the討論的交易策略涉及使用商品渠道指數（CCI）指標來確定潛在的趨勢逆轉並在標準普爾500指數上執行交易。這是一個簡明的摘要：

1. **指標** ：CCI用于衡量相對於歷史平均值的價格水平，有助於識別超售出或過高的條件。

2. **設置** ：
   - **回顧期** ：針對標準普爾500指數優化了9天的中期。
   - **進入信號** ：當CCI跌至-90以下時購買。
   - **退出信號** ：當收盤價超過昨天的高價時出售。

3. **表現** ：
   - **股權增長** ：從1993年開始從100,000美元開始，該策略增長到100萬美元以上。
   - **交易數量** ：執行了464筆交易。
   - **平均每次交易** ：$ 253。
   - **獲勝率** ：47％的成功率，這意味著幾乎一半的交易損失了錢。
   - **風險與獎勵比率** ：該策略的有利比率為1.8：1。

4. **結論** ：雖然該策略具有強大的股本增長和良好的風險回報比率，但其較低的獲勝率和大量的損失交易使其在整體盈利能力方面具有挑戰性。
</details>

<details>
<summary>088. Stocks During War And Conflict (Profit from War Stocks)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zJaolkzOkWQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

視頻中討論的交易策略表明，從歷史上看，股票市場在戰爭時期並未經歷大幅下降，在珍珠港等事件之後，最大損失約為20％。 這背後的原因是多方面的：

1. **政府支出和經濟活動** ：戰爭可以刺激政府支出，這可能會促進經濟活動。
2. **市場期望** ：衝突在開始之前經常被預期並定價為市場，減少驚喜和恐慌。
3. **波動率降低** ：有趣的是，與直覺相反，在衝突期間，市場波動往往會減少。

該策略建議投資者考慮以下內容：

- 如果您的當地市場沒有直接參與衝突，則可能是謹慎的 "buy on the sound of cannons" （即，在衝突開始時投資）和 "sell on the sound of trumpets" （即作為和平談判或決議開始出售）。

這種方法是一般規則，投資者應考慮其個人情況並諮詢財務顧問。 有關更詳細的策略，該視頻建議訪問量化策略的網站或YouTube頻道。

### 關鍵要點：
- **歷史表現** ：戰爭期間股市通常沒有大幅下降。
- **原因** ：政府支出，市場預期以及降低波動。
- **戰略** ：考慮在衝突開始時（如果地方市場不受影響）並隨著和平的開始而銷售。

有關個性化建議或更詳細的策略，請訪問 [量化策略](https://www.quantifiedstrategies.com).
</details>

<details>
<summary>089. Relative Vigor Index (RVI) Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zLFujYKDyGA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

提出的交易策略涉及使用相對活力指數（RVI）作為動量指標。 這是該戰略的簡明摘要：

1. **定義和計算** ：
   - The RVI measures price momentum by comparing closing prices to their trading range.
   - It includes a signal line, which is a simple moving average used to smooth results.

2. **策略規則** ：
   - A 5-day lookback period is used.
   - **購買信號** ：當RVI越過信號線和RVI的5天RSI低於50時，執行買入。
   - **賣出信號** ：當RVI越過信號線以下時出售。

3. **表現** ：
   - Tested on GLD (gold ETF), the strategy yielded an average gain of 0.44% per trade with a win rate of 51%, though winners outweighed losers in size.
   - The strategy was not effective on assets like the S&P 500 or bonds, indicating it may work better in specific market conditions.

4. **結論** ：
   - While the RVI is underutilized and showed promise on GLD, its effectiveness can vary across different assets. Further testing and adaptation are recommended for broader applicability.
</details>

