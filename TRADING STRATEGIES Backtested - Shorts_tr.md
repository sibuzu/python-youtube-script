### TRADING STRATEGIES Backtested - Shorts (中文)

---

<details>
<summary>001. Simple Bond Trading Strategy (Backtest &amp; Rules) #shorts #short</summary>

[[Youtube]](https://www.youtube.com/watch?v=-6g67iQ_sBk&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略旨在利用20年以上的iShares財政債券ETF（TLT）中的季節性模式。 這是一個結構化的摘要：

1. **策略概述** ：
   - The strategy involves buying TLT on the seventh last trading day of each month and then selling short by the end of the month.
   - The short position is closed on the seventh trading day of the following month.

2. **力學** ：
   - **入口點** ：在月中（最後一個交易日）左右購買TLT。
   - **出口點** ：在月底出售短片，並在新月的第七天覆蓋短缺。

3. **表現** ：
   - The strategy claims to grow $100,000 to $735,000 over 20 years, indicating a significant return. This suggests an average annualized return around 8-9%, though compounded growth plays a role.

4. **策略背後的理由** ：
   - Potential seasonal factors include tax selling, institutional positioning, or economic event-driven market movements.
   - The strategy may capitalize on TLT's price behavior related to interest rates and inflation expectations.

5. **考慮和風險** ：
   - **交易成本** ：高頻交易可能會產生可觀的費用。
   - **市場變化** ：隨著市場狀況的發展，季節性模式可能會隨著時間的流逝而失去效力。
   - **槓桿作用** ：雖然沒有明確提及，但槓桿位置可能會放大回報，但也可以風險。

6. **系統與酌情** ：
   - The strategy appears systematic, potentially automatable with strict rules, though its robustness depends on the consistency of underlying patterns.

7. **結論** ：
   - While the strategy has delivered strong historical returns by exploiting seasonal patterns, it requires careful consideration of economic conditions, transaction costs, and the sustainability of these patterns over time.

這種方法基於TLT中觀察到的市場模式利用系統的交易規則，旨在利用重複出現的價格變動，同時管理相關風險。
</details>

<details>
<summary>002. Positional Trading Strategy (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=-aLXtvB74Nw&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略是 **位置交易方法** 這涉及長期持有職位，通常是幾周到幾個月。 它被認為是一種長期策略，但與傳統不同 "Buy and Hold" 方法通過基於性能的定期旋轉合併。

### 策略的關鍵特徵：
1. **涉及的資產** ：該策略側重於四個ETF：
   - SPY (S&P 500)  
   - EFA (MSCI Europe ex-US)  
   - EEM (iShares MSCI Emerging Markets)  
   - TLT (20-Year Treasury Bond ETF)

2. **交易規則** ：
   - At the end of each month, the four ETFs are ranked based on their performance.  
   - The ETF with the best performance is selected and held for one month.  
   - This process is repeated monthly.

3. **表現** ：
   - The strategy generated an average monthly gain of **1.3％**。
   - Annualized returns were **10.1％**。
   - However, it faced significant challenges in 2022, with a loss of **40％**，強調了其在市場低迷時期的脆弱性。

4. **權益曲線** ：公平曲線反映了策略隨著時間的推移的累積性能，顯示了增長和下降時期，尤其是在2022年。

### 結論：
Thi該策略將長期投資的要素與基於資產績效的定期調整相結合。 儘管歷史上已經顯示出有希望的回報，但它對每月輪換的依賴使其對短期市場的波動敏感，這證明了2022年的巨大損失。有關更多詳細信息，您可以訪問 [jenterifiedstrategies.com](https://quantifiedstrategies.com).
</details>

<details>
<summary>003. Rubber Band Strategy (Rules+Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=-j9tlOtDvVw&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

橡皮筋交易策略是一種平均回歸方法，它利用了這樣一種信念，即資產價格將在偏離後的歷史平均水平。 這是一個簡明的摘要：

1. **平均歸還原則** ：該策略假設價格在平均值左右波動，並最終將恢復，使交易者可以以較低的價格（弱點）購買並以較高的價格（強度）銷售。

2. **機制** ：投資者在被低估（低價）期望反彈時購買資產，並在高估（高價）時出售，預計會有更正。

3. **表現** ：到2022年，1993年的100,000美元投資增長到870,000美元，每年收益率為7.4％，包括股息。 這種增長歸因於將近三十年的複雜性。

4. **考慮因素** ：
   - **風險** ：包括定時的挑戰以及價格可能不會迅速恢復的可能性。
   - **成分** ：考慮總回報的資本利得和股息收入。
   - **應用** ：最適合諸如股票，ETF或商品之類的資產，需要長期觀點，並具有頻繁的交易調整潛力。

5. **結論** ：該策略是耐心，系統的，旨在通過利用市場歸還對平均值來實現穩定的複合回報。
</details>

<details>
<summary>004. Russell 2000 Trading Strategy With Rules And Historical Backtest</summary>

[[Youtube]](https://www.youtube.com/watch?v=-m1Bb0XZevY&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

相關的交易策略涉及每月使用Russell 2000指數的月末方法，重點是短期持有期。 這是該策略及其績效的結構化摘要：

1. **策略概述：** 
   - **入口點：** 在每個月的最後五交易日購買。
   - **出口點：** 保持直到下個月的第一個交易日。
   - **持有期：** 相對較短，每個月大約一周，投資持續時間約為28％。

2. **表現：** 
   - **長期增長：** 自1987年成立以來，該戰略一直在發展。
   - **2010年以後的表現：** 雖然仍然積極，但與過去的幾十年相比，回報率削弱了。
   - **與買賣的比較：** 在沒有再投資的股息的情況下，勝過現金指數，表明儘管投資時間有限，但有效的回報率。

3. **成功的潛在原因：** 
   - Captures market movements at month-ends, possibly due to institutional buying or momentum effects.
   -避免長期接觸市場波動，重點關注具有向上趨勢的時期。

4. **注意事項：** 
   - Transaction costs and slippage could impact returns, though they haven't significantly eroded performance until recently.
   - Russell 2000's small-cap nature may contribute to its volatility and sensitivity to economic conditions.

5. **結論：** 
   - The strategy efficiently captures market gains during short holding periods each month, demonstrating resilience over decades with a notable shift in performance post-2010. It offers a balance between active management and reduced market exposure.
</details>

<details>
<summary>005. Small Cap Effect Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=14p0iYO36tI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**小型價值交易策略的摘要** 

1. **小帽效應概述** ：小型股效應或小型股票溢價強調，長期較小的公司傾向於超過較大的公司。 這種現象是FAMA法國三因素模型不可或缺的一部分，該模型解釋了股票通過大小，價值和動量因素的回報。

2. **歷史背景** ：自1940年以來，與小型股生長庫存相比，小型股價值庫存表現出較高的性能。 歷史數據顯示，到2023年，對小型股票股票的100美元投資增長到了276,000美元，在同一時期，標準普爾500指數的增長率顯著超過了38,000美元的增長。

3. **策略組件** ：
   - **目標市值** ：專注於市值低於10億美元的公司。
   - **財務健康** ：在過去五年中，投資於表現出積極回報（ROE）的公司，以確保財務穩定。
   - **投資選擇** ：在跟蹤靈活性的小型股值指數的單個高質量的小型股票或ETF之間進行選擇。

4. **性能示例** ：該戰略的有效性受到歷史回報的強調，說明了專注於較小的財務健康公司的潛在好處。

該策略強調規模和質量，為投資者提供了一種結構化的方法來利用小型股票保費。
</details>

<details>
<summary>006. Paul Tudor Jones - Rejecting Harvard to Making Millions #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=1unef23wdps&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

paul Tudor Jones是一位著名的華爾街交易員，以其成功的戰略而聞名，該戰略結合了技術和基本分析。 他的方法還融合了時區和市場周期的見解，利用他的豐富經驗來有效地瀏覽金融市場。 在二十年中，這一策略在輔導投資公司持續的成功中發揮了作用。
</details>

<details>
<summary>007. Supertrend Indicator Strategy (Backtest And Performance)</summary>

[[Youtube]](https://www.youtube.com/watch?v=1xuNNJaALGA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略採用了超級趨勢指標，這是一種技術分析工具，旨在識別潛在的買賣信號。 這是該策略及其績效的結構化摘要：

### 策略概述：
1. **指標構建** ：
   - The Super Trend indicator calculates a median price by averaging the high, low, and close prices of each candle.
   - Bands are added above and below this median line using a 10-period lookback to determine their position.
   - These bands have a width of three times the average true range (ATR), creating relatively wide boundaries to account for volatility.

2. **條目/退出規則** ：
   - A buy signal is generated when the closing price crosses above the previous value of the Super Trend indicator.
   - Conversely, a sell signal occurs when the closing price crosses below the previous value.

### 性能指標：
- **進行回測結果** ：當應用於標準普爾500指數時，該策略的年收益在38個交易中近6％。
- **貿易故障** ：
  - **贏得交易** ：38分中的11個，導致大約29％的獲勝率。
  - **失去交易** ：38分中的27人，表明損失比獲勝更多。

### 關鍵觀察：
- 該策略依賴於從獲勝行業中獲得更高的平均利潤來抵消眾多損失的損失。 這表明，儘管大多數交易損失，但獲獎者足夠重要，可以為整體回報做出積極的貢獻。
- 使用三次ATR用於頻帶寬度可能會增加信號頻率，但也可能導致更多的鞭子（快速價格逆轉），可能會影響可靠性。

### 注意事項：
- **市場狀況** ：該策略的有效性可能取決於市場趨勢。 強大的上升趨勢可能會產生更少，更可靠的信號，而波濤洶湧的市場可能會增加虛假信號。
- **風險管理** ：隨著大量損失交易的數量，該策略需要仔細的風險管理來減輕潛在的逐漸減少並確保可持續性。

### 結論：
超級趨勢策略是一種趨勢範圍的方法，它使用中位數價格頻段和ATR進行波動率測量。 雖然它提供了體面的年收益，但其較低的獲勝率突出了成功交易中較大利潤的重要性。 考慮此策略的交易者應評估其風險承受能力，並評估其在不同市場條件下的適用性。
</details>

<details>
<summary>008. Valentine’s Day Trading Strategy (Backtest+Performance)</summary>

[[Youtube]](https://www.youtube.com/watch?v=4DqERQgdtHQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

貿易策略利用了市場在情人節（2月14日）周圍（2月14日）經歷異常正面回報的歷史趨勢。 這是一個簡明的摘要：

1. **進入信號** ：在2月的日曆日是第10個或更晚時輸入長位置。
2. **退出信號** ：將於2月14日或第二天的第一交易退出交易，如果2月14日不是交易日。
3. **表現** ：該策略顯示，在大約三個交易日內，平均每筆交易的平均增長率約為0.35％，自1960年以來，標準普爾500指數的上升股票曲線上升。

這種方法利用情人節拉力賽現象在此期間捕捉潛在的市場增長。
</details>

<details>
<summary>009. Trading the SANTA CLAUS Christmas Rally (Seasonal Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=60CKmOTmb70&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略圍繞利用 "Santa Claus Rally" 與過去二十年相比，與股票相比，現象在歷史上表現出更強的黃金價格表現。 這是該戰略的簡明摘要：

1. **入口點** ：在12月的期權到期日結束時購買黃金。
2. **出口點** ：在新年（1月1日）的第一交易日結束時出售黃金。
3. **表現** ：自2000年以來，該策略的平均每個交易的平均回報率超過2％。
4. **回測** ：該策略在視頻中進行了反測試，類似於針對其每周新聞通訊進行的其他分析，可以通過量化策略的網站訂閱。

這種方法利用黃金價格在此特定時間範圍內集會的歷史趨勢，有可能為交易者提供每年可靠的利潤機會。
</details>

<details>
<summary>010. SECTOR ROTATION strategy  (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=6GfsFt5Wxzw&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**行業旋轉交易策略摘要** 

行業輪換策略涉及根據其最近的績效在不同資產類別或ETF之間進行系統切換。 利用四個特定的ETF（SPY（S＆P 500），TLT（長期財政債券），EFA（國際股票）和EEM（新興市場）），該方法按照上個月的表現對這些ETF進行排名。 然後，投資者將一個月的持有期分配給表現最佳的ETF，每個月重複此過程。

從2014年到2022年，使用歷史數據進行對該策略進行了重新測試，表現出強勁的表現，儘管這一年的市場挑戰卻在2022年的年收益率為10.1％。 每個貿易平均收益為1.3％，強調了該戰略的有效性。 股票曲線顯示出一致的增長，表明隨著時間的推移穩健的回報。

有關此策略的更多詳細信息或資源，請訪問QuantifiedStrategies.com。

 **要點：** 
- **策略重點：** 根據ETF性能每月重新平衡。
- **使用的資產：** 間諜，TLT，EFA和EEM。
- **表現：** 在2022年平均每次交易的平均增長率為1.3％。
- **來源以獲取更多信息：** jenterifiedstrategies.com。

該摘要捕獲了戰略，其機制和績效成果的本質。
</details>

<details>
<summary>011. Oversold Trading Strategy Edge (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=6qlDMS8p4n0&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略是基於平均歸還原則，這表明資產價格最終將在極端波動或過度反應的時期後恢復到其歷史平均水平。 這是該策略的摘要：

1. **超售市場** ：該策略將超售市場定義為價格延長的價格，無論是幾天，幾周還是數月。

2. **進入信號** ：交易者進入市場（買）時，當3天的相對強度指數（RSI）低於20時。RSI是一個技術指標，可衡量最近價格變化的幅度以確定過度購買或超售條件。 低於20的值表示條件過多。

3. **退出信號** ：交易者在收盤價高於昨天的高價時退出市場（賣出）。 這表明價格扭轉了他們的下降趨勢並正在向上移動。

4. **表現** ：該策略聲稱，股權表現出穩定的上升增長，這是一個假設的例子，即在此期間從10,000美元增長到130萬美元。 雖然令人印象深刻，但重要的是要注意，由於交易成本，打滑和市場狀況等因素，這種結果可能無法代表現實世界的績效。

### 要點：
- 該策略很簡單，但在很大程度上依賴於技術指標。
- 它假設市場在超賣後將恢復到他們的平均值。
- 當由於最近下降而被低估價格時，將RSI用作進入信號可以幫助識別潛在的購買機會。
- 相對於前一天的高目標，基於收盤價的退出信號旨在捕獲向上的動力。

### 注意事項：
- **風險管理** ：該策略沒有明確提及諸如停止損失訂單之類的風險管理技術，這對於限制潛在損失至關重要。
- **市場狀況** ：該策略的有效性可能會根據市場狀況而有所不同，並且可以在不同時期內進行測試以評估其穩健性。
- **執行費用** ：在實際交易中，交易成本和滑倒會極大地影響回報，尤其是對於需要經常交易的策略。

總體而言，雖然該策略顯得直截了當並聲稱績效很強，但在實時交易環境中實施它之前，必須對其進行歷史數據進行回報，並考慮其他風險管理措施。
</details>

<details>
<summary>012. Simple Swing Trading Strategy That Works (Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=7QfM0JQjiOI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略是標準普爾500指數的搖擺交易方法，旨在利用短期市場的發展。 這是該策略的結構化摘要：

### 關鍵組件：
1. **進入條件：** 
   - Today's intraday high must be lower than the previous day's 10-day High. This suggests a potential downtrend or weakening momentum.
   - The Index Breadth Score (IBS) must be below 0.15, indicating fewer stocks are advancing compared to declining ones, which may suggest market weakness.

2. **退出條件：** 
   - Exit the trade when today's close exceeds yesterday's high, potentially capturing a short-term rally or reversal.

### 策略概述：
- 該策略旨在確定市場動量和廣度較弱的入口點，表明潛在的下行風險。
- 當價格超過先前的高點時，它會退出位置，這可能表明逆轉或強烈的向上移動。

### 注意事項：
- **效力：** 該策略的成功可能會取決於市場狀況，例如上升趨勢，下降趨勢或界限市場。
- **風險管理：** 目前尚不清楚該策略是否包括停止損失訂單，這對於管理潛在損失至關重要。
- **交易成本：** 頻繁的交易會產生成本，影響整體收益。
- **市場周期：** 該策略在各個市場階段可能會有所不同。

### 結論：
該策略使用盤中和更廣泛的市場指標在感知到的弱點期間進入交易，並在看漲信號時退出。 儘管它提供了一種結構化的方法，但其有效性取決於精確的指標定義和實際實施細節。
</details>

<details>
<summary>013. Out of Sample Back Testing: The Key to Trading Profitability</summary>

[[Youtube]](https://www.youtube.com/watch?v=7SAsj3y6GAU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**樣本外進行交易策略的摘要：** 

交易策略涉及將歷史數據分為兩個部分，以進行回測。 第一部分（稱為樣本內（集合）時期）用於制定和完善交易規則，參數和信號。 第二部分（稱為樣本外時期）由以後在開發階段未使用的數據組成。

通過在樣本中訓練策略，然後對樣本外數據進行測試，交易者可以評估該策略在未來，看不見的市場狀況方面的執行方式。 這種方法通過在不適合歷史數據的情況下提供有關其性能的見解來幫助評估該策略的潛在有效性，從而提供了對未來可行性的更可靠的預測。

這種方法對交易者至關重要，因為它允許他們在實現真正的資本之前衡量其戰略的魯棒性，從而減輕與可能在歷史數據上表現良好但在新市場條件下效果良好的策略相關的風險。
</details>

<details>
<summary>014. Bollinger Bands Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=8LcW6V9ppDg&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

討論的交易策略使用布林樂隊來識別趨勢，衡量波動率並檢測潛在的突破。 具體而言，當股價結束兩個標準偏差低於10天平均水平並退出該平均水平時，交易者進入較長的頭寸。 但是，該視頻指出，由於價值急劇下降，所產生的股票曲線使該策略不切實際。
</details>

<details>
<summary>015. ESG Investment Strategies  |  (Backtest And Example)</summary>

[[Youtube]](https://www.youtube.com/watch?v=9Fz7J48gqek&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略討論了圍繞ESG（環境，社會和治理）投資的革命。 這是一個簡明的摘要：

1. **ESG集成** ：這種方法涉及在做出投資決策時考慮ESG因素以及傳統的財務分析。

2. **性能概述** ：
   - Since 2007, non-ESG hedge funds have outperformed ESG funds, with an annual return of 6.1% compared to 5.4% for ESG funds.
   - However, studies suggest that good ESG policies can lead to improved financial performance, potentially helping investors achieve Alpha (excess returns) and downside protection.

3. **結論** ：雖然ESG投資可能並不總是勝過所有策略，但它可以在財務績效和風險管理方面提供好處。 對於投資者而言，在制定任何戰略之前進行徹底研究至關重要。

對於更具體的培訓或與定量投資相關的策略，建議使用網站量化strategies.com。
</details>

<details>
<summary>016. I Made a BITCOIN Trading Strategy Work For An Average Person (myself)  #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=9waF-bYvr5E&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略旨在用於容易出價的資產，例如比特幣。 這是一個結構化的摘要：

1. **進入信號** ：
   - The strategy involves buying an asset when its closing price sets a new 25-day high. This indicates a potential upward trend or momentum.

2. **退出信號** ：
   - The exit condition is less clear in the description but likely involves selling when the price drops below a certain threshold relative to the entry point (e.g., a percentage decrease from the 25-day high). Possible methods include trailing stops, moving averages, or technical indicators like RSI.

3. **表現** ：
   - The strategy resulted in an impressive return, growing $100k to $3.6 million in under four years, suggesting significant compounding and volatility exploitation.

4. **考慮因素** ：
   - Potential risks include entering at resistance levels and facing drawdowns during market corrections.
   - The strategy may involve trend-following, which is effective in trending markets but risky in mean-reverting ones.
   - Transaction costs could impact returns, especially with frequent trading.

5. **評估需求** ：
   - Further details on exit criteria and backtesting performance through different market cycles (e.g., crashes) would be beneficial to assess risk and viability.

總而言之，該戰略旨在通過進入新的高點並根據預定義的較低價格水平退出來利用價格峰值，提供高回報，但具有相關風險。
</details>

<details>
<summary>017. Dark Cloud Cover Pattern (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=AhOit-DEY38&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略採用了烏雲覆蓋燭臺圖案，傳統上是看跌指標，但將其用作買入信號。 這是該策略的結構化摘要：

1. **燭臺圖案** ：利用烏雲覆蓋物，通常是看跌信號，表明逆轉或特定的設置確認。

2. **交易規則** ：涉及嚴格的進入和退出行業的標準。 銷售發生在近距離高於昨天的高位時，可能表明與趨勢延續或風險管理有關的退出條件。

3. **進行回測結果** ：在間諜ETF上進行了測試，該策略產生了一條不錯的股權曲線，減少了下降，這意味著有效的風險管理並限制了市場低迷期間的損失。

4. **力學** ：該策略可能包含燭臺模式以外的其他指標或條件，例如超售級別或支持確認ations，以有效地觸發購買信號。

從本質上講，該策略創造性地適應了傳統上看跌的指標，用於購買機會，使用嚴格的規則來提高盈利能力並有效地管理風險。
</details>

<details>
<summary>018. Santa Claus Rally In Stocks</summary>

[[Youtube]](https://www.youtube.com/watch?v=Az2yNmuXZK0&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

聖誕老人集會交易策略利用了觀察到的現象，在聖誕節期間，股票市場往往會上升。 這是基於分析的結構化摘要：

### 關鍵觀察：
1. **歷史表現：** 
   - The market has shown an average gain of 7% over the last four trading days of the year and the first three days of January, with a 66% win rate.
   - A five-day window around Christmas (two days before, three after) yields a 4.2% average gain and a 60% win rate.
   - The shortest window—1 day before and after Christmas—averages 3.5% gain with a 58% win rate.

2. **戰略選擇：** 
   - **長期持有：** 在12月底附近購買並持有1月份，適合那些喜歡交易較少的人。
   - **有針對性的交易：** 專注於窗戶內的高峰日，例如聖誕節前購買和銷售。
   - **被動投資：** 在假期期間投資500指數ETF以持續收益。

### 注意事項：
- **風險容忍和目標：** 選擇一個與個人風險承受能力和投資目標保持一致的窗口。
- **市場行為：** 集會可能源於影響市場行為的年終樂觀，減稅銷售或機構策略。
- **經濟因素：** 外部事件會影響結果，強調需要謹慎。
- **交易成本：** 頻繁的交易可能會產生減少回報的成本。
- **心理影響：** 投資者的信念可以自我延續市場的發展。

### 結論：
儘管有歷史證據支持聖誕老人拉力賽，但其作為獨立戰略的可靠性尚不確定。 考慮到個人情況並進行全面的盡職調查，建議將其用作多元化方法的一部分。
</details>

<details>
<summary>019. QS Exit - Exit Mean Reversion Strategies With Max Profit #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=Bpx7SWCiSGQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這 "Qs Exit" 貿易策略旨在解決何時退出股票職位的關鍵但經常被忽視的方面，尤其是在均值轉換市場中。 這是該策略的結構化摘要：

1. **客觀的** ：QS退出的主要目標是確定出售股票以鎖定利潤並最大程度地減少潛在拖累的最佳時間。

2. **規則** ：賣出今天的收盤價超過昨天的高價。 這意味著將位置退出最近的向上運動的峰值，預計可能的逆轉或均值逆轉。

3. **理由** ：
   - **平均歸還** ：該策略在資產傾向於在偏差後返回其平均價格的市場有效。 通過以新的高價銷售，交易者的目標是避免在上升趨勢下的潛在下降。
   - **利潤鎖定** ：在峰值上退出可以幫助在可能下降之前獲得收益，即使這意味著要錯過進一步的短期欣賞。

4. **好處** ：
   - **Smooter權益曲線** ：通過退出戰略要點的位置來降低波動，從而導致投資組合增長穩定。
   - **增強的利潤** ：通過避免重大損失並允許資本重新部署，可能會導致更高的總體利潤。
   - **風險管理** ：通過儘早減少損失來最大程度地減少對急劇下降的暴露。

5. **考慮因素** ：
   - **市場狀況** ：在普遍存在的均值回歸的環境中最有效，這可能不是趨勢市場的理想選擇。
   - **使用頻率** ：如果每天滿足條件，則可能涉及頻繁的銷售行動，需要適應市場動態。
   - **與其他策略進行比較** ：通過使用相對參考點（昨天的高）而不是固定或落後指標，不同於落後停止和百分比收益。

6. **實際應用** ：需要測試歷史數據以評估有效性，並考慮可能影響收益的交易成本和稅收。

從本質上講，QS退出策略強調了紀律嚴明的出口點，重點是保留利潤並減輕均值市場中的風險。 它將重點從積累的收益轉變為戰略性退出的立場，以持續盈利。
</details>

<details>
<summary>020. Stocks Go Up When the Failed Bounce Strategy Does This</summary>

[[Youtube]](https://www.youtube.com/watch?v=C-JzTokCmOU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

討論的交易策略稱為 "Failed Bounce Trading Strategy." 這是其關鍵組成部分的摘要：

1. **進入條件** ：
   - Yesterday's Internal Bar Strength (IBS) was at least 0.6 or higher.
   - Yesterday's low is lower than the lowest low during the previous five days.

2. **退出條件** ：
   - Exit when today's close is higher than yesterday's high.

3. **貿易執行** ：
   - Buy on short-term pullbacks and sell on strength.

4. **表現** ：
   - The strategy has been tested on several assets, including Pepsi Cola (with an equity curve since 1976), the XLP ETF tracking consumer staples, and the QQQ (Nasdaq-100 tracker).
   -QQQ可以看到最好的表現，平均每個交易的收益為1％。

該策略似乎專注於交易圖中的識別彈跳模式，使用IBS等特定技術指標來確定進入和出口點。 提供的示例表明，它已經在多個資產類別中進行了幾十年的重新測試，在QQQ中最著名的表現。
</details>

<details>
<summary>021. Historical Returns For The Main Asset Classes?</summary>

[[Youtube]](https://www.youtube.com/watch?v=C8hDgdbyFNQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略強調了五個主要資產類別的長期投資方法：股票，債券，黃金，房地產和現金。 關鍵見解包括：

1. **隨著時間的推移資產績效** ：股票在延長期間的表現高於其他資產。 1928年的100美元投資增長到$ 787,000的股票，而只有10,000美元的黃金。

2. **波動和壽命** ：短期投資（3  -  5年）顯示出不穩定的回報，而潛在的降低，而長期持有通常會給股票帶來更高的回報。

3. **避免市場時機** ：該策略建議不要嘗試計時市場，這是困難的，而且通常適得其反。

4. **保持投資** ：即使在低迷期間，由於耐心和一致性在數十年中傾向於取得更好的成績，因此仍保持持股，尤其是在股票中。

總而言之，該戰略倡導多元化的投資組合，重點是長期持有，尤其是在股票中，以最大程度地提高回報，儘管短期波動率。
</details>

<details>
<summary>022. 2 Tips To Succeed In Trading</summary>

[[Youtube]](https://www.youtube.com/watch?v=COYhuCSyKvk&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略強調了擁有 **積極的統計預期** 作為成功的基礎，而不是僅僅專注於思維方式和風險管理，儘管這些仍然被認為是至關重要的。 要點是：

1. **積極的統計預期** ：這是賺錢交易或投資的最關鍵因素。 它指的是策略隨著時間的推移而產生利潤的可能性。

2. **具有優勢** ：大多數交易者缺乏真正的優勢，這使得無論他們的思維方式或風險管理技能如何，都很難始終如一地獲利。

3. **戰略制定** ：要成功，必須：
   - Quantify and backtest strategies to ensure they have a positive expectancy.
   - Develop the discipline to follow the strategy consistently.

該策略鼓勵有抱負的交易者首先確定和測試與其個性和目標保持一致的潛在策略。 有關更多指導，資源 [量化策略](https://quantifiedstrategies.com) 建議使用數百種經過測試的策略。
</details>

<details>
<summary>023. Larry Connors Double Seven Trading Strategy (Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=Do4_tMhElqI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略基於拉裡·康納（Larry Connor）的雙七種方法，該方法已修改為雙五個策略。 修改版本使用五天來可能增加交易數量，而不是像康納（Connor）的原始方法中使用7天一樣使用7天。 關鍵規則是：

1. **購買信號** ：當收盤價高於200天移動平均線並以五天的低點關閉時。
2. **賣出信號** ：當收盤價處於五天的高度時。

### 策略特徵：
- **交易增加** ：比康納的原始策略產生的交易更多，總計352次交易。
- **盈利能力** ：生成總利潤，平均每個交易的收益為0.65。
- **下降** ：中度的縮水量高達14％，它們是短暫的。
- **適用性** ：跨各種資產（包括股票，ETF和未來）的工作，儘管工具可能表現出相關性，從而導致行為不同。

該策略的目的是在可管理的風險水平下保持穩定的性能。
</details>

<details>
<summary>024. Coppock Curve Trading Strategy (Backtest &amp; Rules) #shorts #short</summary>

[[Youtube]](https://www.youtube.com/watch?v=EIv0yyl0Si8&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

copeland曲線交易策略是一種基於動量的方法，旨在通過將兩個RSI指標與加權移動平均線相結合，旨在確定股票市場的長期趨勢。 這是該策略的結構化摘要：

1. **指標計算** ：
   - The Copeland Curve is calculated as a weighted moving average of the 10-period and 20-period Relative Strength Index (RSI). This combination aims to blend short-term volatility with medium-term momentum.

2. **客觀的** ：
   - The strategy seeks to capture sustained trends by smoothing out RSI signals, potentially offering more reliable buy/sell indicators than using a single RSI period.

3. **表現** ：
   - Since 2012, the strategy has delivered an average annual return of approximately 6.11%, suggesting historical profitability in long-term trend trading.

4. **交易信號** ：
   - The strategy likely generates signals based on the Copeland Curve crossing above or below certain thresholds, indicating upward or downward trends.

5. **優勢** ：
   - Combines two RSIs to reduce conflicting signals and provides a balanced approach by considering both short-term and medium-term momentum.
   -通過加權平均，與僅使用一個RSI相比，通過加權平均進行平衡，可能導致信號較小。

6. **考慮因素** ：
   - The choice of weights for each RSI period is crucial and could impact performance.
   - Potential drawdowns during market corrections require robust risk management.
   - Historical performance does not guarantee future results; forward testing is advisable.
   - Transaction costs and slippage should be factored into expected returns.

總之，Copeland Curve策略通過將兩個RSI指標與加權平均整合在一起，提供了一種獨特的趨勢跟蹤方法。 儘管它顯示出歷史效果，但仔細考慮參數，市場狀況和風險管理對於成功實施至關重要。
</details>

<details>
<summary>025. How Long Should You Backtest Your Trading Strategy? Find the Optimal Timeframe</summary>

[[Youtube]](https://www.youtube.com/watch?v=EYhlJm6iBpA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

概述的交易策略強調了徹底進行回測的重要性，以確保穩健可靠的結果。 這是一個簡明的摘要：

1. **回測持續時間** ：
   - Swing strategies should be backtested over at least 10 years to capture various market conditions, including bull markets, bear markets, and corrections.
   - The duration may vary based on the strategy's time frame: shorter for day trading, longer for long-term strategies.

2. **貿易數** ：
   - Ensure a significant number of trades are included in the backtest to avoid results being influenced by random fluctuations.
   -專注於有效驗證策略的時間長度和觀察次數。

這種方法有助於交易者在不同市場方案中對其戰略的績效建立全面的了解，減少對軼事證據的依賴，並提高對策略可靠性的信心。
</details>

<details>
<summary>026. $100,000 to $5.5 Million Momentum Strategy (Rules Revealed) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=EoFWWb1sNk8&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略旨在通過使用100天高和低關閉價格作為進入和退出信號來捕獲長期趨勢。 這是該戰略的簡明摘要：

1. **進入信號** ：當收盤價超過過去100天的最高收盤價時，該策略在結束時進行了漫長（購買）。
2. **退出信號** ：當收盤價降至過去100天的最低收盤價降至最低價格時，該策略就會出售其頭寸。
3. **績效主張** ：從100,000美元開始，該策略據稱在60年內增長到550萬美元，這意味著年齡約為12.8％。

### 主要注意事項：
- **簡單和有效性** ：該策略使用直接的技術指標，但可能會在市場波動期間產生錯誤的信號。
- **風險管理** ：通過以100天的低點退出，它的目的是限制損失，但如果下降後價格反彈，可能會錯過恢復。
- **市場狀況** ：在不同的資產類別和經濟時期，其有效性可能會有所不同。
- **交易成本** ：隨著時間的流逝，即使少量費用也可能影響盈利能力，需要具有成本效益的交易機制。
- **執行** ：可能使用算法自動化，可以長期執行而無需手動監督。
- **回報的現實主義** ：與典型的市場規範相比，獲得如此高的回報是令人印象深刻的，這表明潛在使用槓桿或最佳條件。

該策略強調了趨勢跟蹤和複雜增長的重要性，但需要仔細考慮其局限性和假設。
</details>

<details>
<summary>027. Paul Tudor Jones - 200 Day Moving Average #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=F9XzIgdGgck&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

the相關的交易策略利用200天的移動平均線（MA）作為過濾器來確定標準普爾500指數的買賣信號。這是一個簡明的摘要：

1. **策略概述** ：該策略涉及在價格高於200天的MA並銷售此指標以下時購買。 這種方法旨在確定市場趨勢並避免出現嚴重的低迷，例如1987年的黑色星期一。

2. **與購買和保持相比** ：根據分析，該策略在幾年內略微削弱了購買和持有的方法約5個百分點。 雖然它可以減輕市場壓力期間的損失，但累積影響會導致總回報較低。

3. **風險管理** ：200天的MA可有效減少縮減和管理風險，使其適合於規避風險的投資者。 它是一種保守的戰略，旨在在動蕩時期保留資本。

4. **提高的考慮** ：將200天的MA與其他指標相結合可能會提高性能。 此外，由於頻繁交易而引起的交易成本可能會影響收益，從而進一步影響該策略的有效性。

5. **結論** ：作為一種獨立的方法，該策略犧牲了一些長期的增長潛力，以支持風險管理。 對於那些尋求最大程度地降低下行風險而不是最大化回報的人來說，這是更合適的。
</details>

<details>
<summary>028. Momentum Rotation Trading Strategy (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=FGNeqvinFzA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

有關交易策略是一種行業輪換動量系統，旨在通過每月轉移選定資產之間的投資來利用市場勢頭。 這是一個結構化的摘要：

1. **策略概述** ：
   - **部門旋轉** ：該策略涉及根據其最近的表現在部門之間進行投資，旨在捕捉某些部門優於其他部門的趨勢。
   - **動力重點** ：它利用了趨勢繼續下去的信念，在過去三個月中投資了表現出強大勢頭的資產。

2. **運營力學** ：
   - **每月重新平衡** ：在每個月結束時，該策略根據前三個月的績效評估四個選定的資產（可能是部門或ETF）。
   - **排名和選擇** ：在此期間，資產對其回報進行了排名。 最佳的資產是在未來月份進行投資的，所有資本都分配給了它。

3. **表現** ：
   - The strategy has demonstrated significant growth potential, as evidenced by a hypothetical $100,000 growing to nearly $1.4 million from 2002 onward. This suggests effective compounding through consistent performance.

4. **考慮和風險** ：
   - **資產選擇** ：雖然該示例使用四個資產，但未詳細介紹用於選擇超出回報的特定標準。 如果多個資產的業績相似，則可能會有決勝局。
   - **交易成本** ：與更頻繁的策略相比，每月重新平衡會降低交易頻率，可能會降低成本，但每月有重大投資組合變化。
   - **市場風險** ：依靠動量會導致損失，如果趨勢突然逆轉或揮發性市場。 該策略可能會經歷下降，並可能通過專注於短期數據而錯過長期趨勢。

5. **比較** ：
   - This strategy contrasts with others that use different time frames or more sectors, offering a concentrated approach that may spread risk less but focus on maximizing returns through momentum.

總而言之，行業旋轉動量系統是一種每月的重新平衡策略，在三個月內選擇最佳資產，旨在實現顯著增長。 它可以平衡潛在的高回報與市場波動和趨勢逆轉有關的風險。
</details>

<details>
<summary>029. MACD And Bollinger Bands Strategy (That Works)</summary>

[[Youtube]](https://www.youtube.com/watch?v=FqELrHYKTmw&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略是一種經過反測試的MACD策略，該策略結合了MACD直方圖上的布林樂隊。 這是一個簡明的摘要：

1. **進入和退出規則** ：
   - Enter a long position when the MACD histogram crosses below the lower Bollinger Band.
   - Sell (exit) when the histogram crosses above the upper Bollinger Band.

2. **表現** ：
   - Starting with $100,000, the strategy grew to $1.15 million, resulting in an annual return of 8.4%.
   - The strategy is described as having a "mixed" 性能，以穩定的勝利率認為其主要的積極屬性。

3. **缺點** ：
   - A significant drawdown of 44% is noted, which could deter many traders from adhering to the strategy despite its overall performance being comparable to a Buy-and-Hold approach.
   - The strategy is only invested 64% of the time, meaning it frequently holds cash during periods when it is not actively trading.

總之，儘管該策略提供了有希望的回報和高的獲勝率，但考慮其長期生存能力的交易者可能會構成挑戰。
</details>

<details>
<summary>030. Index Trading Strategy (Settings + Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=GhKpiq9Wko8&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略是趨勢之後和平均複製的融合，旨在利用市場趨勢，同時利用短期價格偏差。 這是一個結構化的摘要：

1. **市場環境** ：
   - **熊市** ：該策略採用短期平均歸還，假設價格將在偏差後平均恢復到平均值。
   - **牛市** ：該策略採取了較長的立場來捕捉整個上升趨勢。

2. **橡皮筋策略** ：
   - Activated when the 200-day MA is above the 50-day MA, indicating an uptrend.
   -可能涉及平均回歸技術，例如交易價格偏離移動平均值或布林樂隊的偏差。

3. **表現** ：
   - Starting with $100,000, growth to over $2.5 million yields an annual return of 11.2%.
   - Maximum drawdown is 33%, indicating significant potential losses.

4. **實施注意事項** ：
   - Transitions between trend following and mean reversion based on moving average crossovers.
   - Programming in languages like Python with libraries such as Pandas can facilitate strategy testing, considering transaction costs and slippage.

5. **要考慮的要點** ：
   - The strategy's effectiveness may vary across different market cycles.
   - High drawdowns necessitate careful risk management and sufficient capital buffer.

該策略有效地結合了趨勢之後的要素和平均恢復，提供了有希望的回報，但具有明顯的風險。 建議進一步測試和驗證以評估其在各種市場條件下的魯棒性。
</details>

<details>
<summary>031. Swing Trading Strategy (Backtest &amp; Rules) #shorts #short</summary>

[[Youtube]](https://www.youtube.com/watch?v=Hsdnpd6pQOw&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的標準普爾500指數的搖擺交易策略涉及確定潛在的下降趨勢，並使用特定標準決定何時出售。 這是對該策略的明顯細分：

1. **確定下降趨勢** ：尋找連續兩天，每天關閉的時間低於前一天。 這表明看跌趨勢。

2. **第三天評估** ：在第三天（例如，星期一），檢查收盤價是否超過了上一個交易會的高價。

3. **賣出信號** ：如果第三天的結束比前一天高，請出售。 理由是，這表明嘗試恢復失敗，表明繼續向下移動。

該戰略旨在通過在可能下降之前退出位置來利用潛在的下降趨勢。 重要的是要使用歷史數據來評估其有效性並考慮時間範圍和市場狀況等因素。
</details>

<details>
<summary>032. RSI Trading Strategy (Backtest and Rules) #shorts #short</summary>

[[Youtube]](https://www.youtube.com/watch?v=HttcI-BrBeg&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

兩個時期的RSI策略是標準普爾500指數的交易方法，該方法使用為期2天的相對強度指數（RSI）生成買賣信號。 這是一個簡明的摘要：

1. **機制** ：
   - Buys when the 2-day RSI crosses below 10, indicating an oversold condition.
   - Sells when the 2-day RSI crosses above 80, indicating an overbought condition.

2. **表現** ：
   - Backtesting shows a significant return, with $100k growing to $1.2 million over 30 years, suggesting an annualized return of approximately 8.6%.

3. **考慮因素** ：
   - **頻率** ：該策略可能涉及由於RSI時期較短而頻繁的交易，從而導致潛在的交易成本和稅收影響。
   - **可靠性** ：極端閾值（10和80）可能導致信號不可靠，可能丟失移動或引起鞭打。
   - **下降** ：未指定在2008年危機之類的市場糾正期間的績效，這引起了人們對縮減風險的擔憂。
   - **趨勢處理** ：該策略可能會儘早退出趨勢，缺少長時間的收益或損失。

4. **比較** ：
   - Compares favorably to other strategies but may not generalize well beyond the S&P 500 or different timeframes.

總之，儘管該策略顯示出強烈的回測結果，但現實世界的應用需要考慮交易成本，信號可靠性和潛在的下降。 它的有效性取決於在標準普爾500標準普爾（S＆P 500）等趨勢市場中捕獲短期動量波動。
</details>

<details>
<summary>033. Is THIS Meb Faber  Strategy BETTER Than What 99% of Traders Are Using? #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=IrQbXvDTjXQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略是一種涉及三種ETF的動量旋轉方法：間諜（標準普爾500），GLD（Gold）和TLT（債券）。 該戰略由Meb Faber在2015年左右開發，使用每月的酒吧來生成信號。 這是一個簡明的摘要：

1. **信號** ：
   - Invest or stay long when the 3-month Simple Moving Average (SMA) is above the 10-month SMA.
   
2. **分配** ：
   - Allocate one-third of capital to each ETF when a signal is received.
   - If signals occur in two ETFs, invest 66% of equity, keeping 33% in cash.

3. **表現** ：
   - The strategy performed well until 2015 with an annual return of nearly 8% and a modest maximum drawdown of 18%.
   - Since 2015, the annual return has dropped to just under 3%.

4. **當前的市場環境** ：
   - Currently, all three moving averages are above their respective counterparts, indicating an uptrend.
   - Recent market corrections have raised questions about whether the strategy will rebound or if adjustments are needed.

總而言之，這是一種基於動量的方法，它基於移動平均分頻器在股票，債券和黃金之間轉移資本。 儘管歷史上有效，但自2015年以來，其性能一直在逐漸下降，鑑於最近的市場動態，促使人們考慮了潛在的調整。
</details>

<details>
<summary>034. Sell The Rip Strategy (Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=JoLj0vWYLJs&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

the有關交易策略是 "Sell the Rip," 當RSI降至30以下並在達到70時出售時，它在3天的時間內利用RSI指標來發出長時間的信號。這是一個結構化的摘要和分析：

1. **使用的指示器** ：該策略採用3天的RSI，比標準14周期RSI短。 此選擇旨在快速捕獲短期趨勢，但可能會增加波動性和虛假信號。

2. **性能指標** ：
   - Backtested on S&P 500 from 1993 to present.
   - 391 trades, 61% return per trade, 58% win rate.
   -這些指標提出了一種有利可圖的策略，但強調了需要複合分析和風險管理。

3. **市場狀況** ：該戰略的有效性應在不同的市場條件（例如牛市與熊市）之間進行評估，以確保穩健性。

4. **風險考慮** ：
   - Each losing trade's impact on overall profitability needs assessment.
   - Transaction costs and slippage may affect real-world performance, which the backtest might not account for.

5. **驗證和測試** ：
   -檢查有關短期RSI策略的學術研究或現有研究。
   - Stress test the strategy across different assets and time frames to avoid overfitting to S&P 500.

6. **潛在的增強** ：
   - Consider combining with other indicators like volume analysis or trend filters to improve robustness.
   - Evaluate the equity curve growth and risk-adjusted returns for a comprehensive understanding.

總之，而 "Sell the Rip" 策略顯示有希望的回測結果，進一步的驗證以及對評估其實際有效性的其他因素的考慮。
</details>

<details>
<summary>035. Stocks During War And Conflict (When To Buy And Sell) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=KlhfM9fd0bI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

描述的交易策略表明，基於對重大衝突的歷史市場反應採取行動。 這是一個簡明的摘要：

1. **歷史背景** ：市場通常會預期和因素發生戰爭或重大地緣政治事件發生的影響，如珍珠港之前的美國股票下降所示。

2. **策略建議** ：
   - **當市場對衝突負面反應時購買** （例如，在市場下降期間，由戰爭聲音觸發的市場下降）。
   - **市場何時銷售過度集會** （例如，在衝突之後的集會後出售）。

3. **理由** ：該策略是基於這樣的想法：衝突通常在發生之前定價，而市場最初可能會反應過度，從而在過度集會期間價格下跌或出售機會時可能會產生潛在的購買機會。

4. **座右銘** ： "Buy to the sound of cannons, sell to the sound of trumpets," 根據市場對事件的反應而不是直接對衝突本身反應，強調定時交易。

這種方法鼓勵交易者在決策中考慮歷史模式和市場心理學。
</details>

<details>
<summary>036. How To Win In A Bear Market (Trading Strategy Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=KxWSqDfCROc&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這種交易策略是為熊市設計的，其特徵是價格下跌和市場悲觀。 自2000年以來，該策略已表現出一致的有效性，使其成為任何交易系統的可靠補充。 它利用市場衰退期間的機會，為希望在挑戰經濟狀況的交易者提供了一種強大的方法。
</details>

<details>
<summary>037. $7,3 Billion Paul Tudor Jones &amp; His Trading Strategies #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=Lx_pHPhP_rU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

paul Tudor Jones採用了以技術分析和對市場心理學的了解為中心的多方面交易策略。 他方法中的一個關鍵工具是200天的移動平均線，他用它來有效地識別趨勢和時間條目/退出。 儘管與標準普爾500指數的購買和持有策略相比，這種方法的表現略有下降，但它提供了較低的波動性和壓力。 瓊斯還從事全球宏觀交易，以更廣泛的社會和政府轉變為基礎，將自己定位在國際市場中。 他執行積極的管理，不斷評估自己的投資組合，從表現不佳的資產中剝離並投資於更有希望的資產，從而確保了動態和反應迅速的投資策略。
</details>

<details>
<summary>038. Is THIS RSI Strategy BETTER Than What 99% of Traders Are Using? #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=LyFqVMuVRA8&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略可以總結如下：

1. **進入策略** ：
   - Enter a long position ("buy" ）當價格低或顯示出弱點的跡象時，表明可能發生向上移動的潛力。

2. **退出策略** ：
   - Exit the position ("sell" ）使用稱為 "Qs exit," 當收盤價超過前一天的高點時，這涉及出售，這表明向上勢頭強勁。

3. **性能指標** ：
   - The strategy yields an average gain of 0.59% per trade and an overall average return of 8.5%. This suggests that while each trade's profit is modest, compounded returns over multiple trades lead to significant gains.

4. **考慮因素** ：
   - The term "Qs exit" 不清楚沒有其他上下文，可能是指指標或方法。
   - The strategy may follow a trend-following approach, capitalizing on momentum until reversal.
   - Further details on signal frequency and risk management are needed for comprehensive evaluation.

從本質上講，該戰略旨在通過進入低點並退出新高點來利用向上的趨勢，從而通過一致的應用獲得顯著的回報。
</details>

<details>
<summary>039. RSI Pullback Trading Strategy (That Works) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=MVCK6qK1Qqg&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略採用相對強度指數（RSI）作為技術指標來確定潛在的買賣機會。 這是分析的有組織摘要：

1. **策略概述** ：
   - The strategy involves buying assets when RSI falls below 15 (indicating oversold conditions) and selling when it rises above 20 (overbought conditions). This approach aims to capitalize on short-term price reversals.

2. **RSI閾值** ：
   - Using thresholds of 15 for buying and 20 for selling is more aggressive than the standard RSI levels (typically 30 for oversold and 70 for overbought), suggesting a focus on more extreme market conditions to enter trades.

3. **性能指標** ：
   - Annual returns are reported at 4.2%, which is modest, but the risk-adjusted return is noted as 37%. This high figure may indicate a strong Sharpe ratio, though verification of the calculation method is recommended.

4. **潛在問題和考慮因素** ：
   - **假信號** ：頻繁的RSI波動可能導致許多具有有限利潤潛力的交易。
   - **交易成本** ：高交易頻率可能會增加成本，從而影響整體回報。
   - **時間範圍和資產特異性** ：該策略的有效性可能取決於用於RSI計算的時間範圍（例如14天與較短的時期）和資產類別。

5. **市場狀況** ：
   - The strategy's reliance on short-term price reversals might not perform well during trending markets, where RSI could lead to frequent whipsaws.

6. **進行回測和現實應用程式** ：
   - Without specific backtesting details, it's uncertain if the strategy holds up in various market conditions.
   - Costs associated with frequent trading, including commissions and slippage, should be carefully considered.

7. **替代方法** ：
   - Enhancing the strategy with additional indicators or techniques, such as divergence analysis or waiting for pullbacks, might improve its effectiveness.

總而言之，儘管基於RSI的策略為短期交易提供了一種直接的方法，但其成功取決於幾個因素，包括交易成本，市場狀況和徹底的回測。 潛在交易者應在實施該戰略之前評估這些方面。
</details>

<details>
<summary>040. CCI Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=OFHiOeV5zbQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略涉及使用商品渠道指數（CCI）指標來確定潛在的趨勢逆轉和極端市場狀況。 這是一個簡明的摘要：

1. **指標概述** ：CCI衡量安全價格相對於指定時期內平均價格的價格水平，充當動量振蕩器。

2. **進入信號** ：當CCI降至-90以下時，觸發了買入信號，指示過多的條件。

3. **退出信號** ：當收盤價超過昨天高達100,000個單位時（示例中提到的上下文）時，就會發生賣出信號。

4. **性能示例** ：該策略表現出了很大的回報，在一段時間內將權益繁殖十倍，如1993年的例子所示。

這種方法利用技術分析利用CCI來利用市場趨勢和逆轉，以獲取入口點和出口定製目標目標。
</details>

<details>
<summary>041. Friday the 13th &amp; Stocks: Superstition or Reality?</summary>

[[Youtube]](https://www.youtube.com/watch?v=OUf_mov6pVs&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**概括：** 

交易策略通過在股票市場採取逆勢方法來利用圍繞13日星期五的迷信。 基於自1960年以來歷史標準普爾500指數數據，這表明與其他星期五相比，星期五的13個數據並不是特別不幸或不穩定，該策略涉及：

1. **進入信號** ：在一個月的第13個月，在標準普爾500指數期貨或ETF上進行長時間（購買）。
2. **退出信號** ：保持職位，直到市場在同一天關閉。
3. **風險管理** ：使用停止損失命令，以限制必要時限制潛在的損失和滾動位置。

理由是，從歷史上看，13年代星期五的平均收益比其他星期五要好得多或可比，這表明當時股票市場上沒有固有的厄運。
</details>

<details>
<summary>042. The BEST Night Trading Strategies (Rules and Backtest) - (Not what you expect!)</summary>

[[Youtube]](https://www.youtube.com/watch?v=OqKCt_12B2M&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略概述的重點是利用過去30年中標準普爾500指數中觀察到的隔夜偏見。 這是一個簡明的摘要：

1. **隔夜增長** ：該策略強調，標準普爾500指數中的大多數收益都在一夜之間發生，平均收益比第二天開放的市場平均增益為0.04％。

2. **過夜偏見的原因** ：這種趨勢歸因於通貨膨脹和收益增長等因素，這為持有股票的獎勵提供了一夜之間的獎勵。

3. **逆勢方法** ：該策略表明避免短期交易（公開購買和關閉銷售），因為它從歷史上導致了損失。 取而代之的是，它提倡在一夜之間保持位置以捕獲向上的漂移。

4. **努力低** ：與主動交易或市場時機相比，這種方法需要最少的努力，這使那些尋求一種簡單的方式參與股市增長的人具有吸引力。

總體而言，該策略強調了一種被動的，等待的方法，以利用市場傾向於一夜之間上升，而不是從事日常交易。
</details>

<details>
<summary>043. I Tested This Trading Strategy &amp; It Made...  | #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=Ouc9vmq2H38&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這種交易策略涉及在一個月的最後一個交易日結束時進入間諜（跟蹤標準普爾500標準普爾500的ETF），並在下個月的第一個交易日結束時退出該職位。 該策略基於這樣的觀察，即新月的第一個交易日往往比隨機日期更好，平均每次交易的平均收益為0.25％。 此外，首次嘗試時，貿易很有可能是有利可圖的，這使得它是希望利用每月市場模式的交易者的潛在可靠和簡單的方法。
</details>

<details>
<summary>044. Bullish Reversal Trading Strategy (With Trading Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=PX3jRwa_Dxk&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略旨在利用重大市場轉移後的逆轉模式，例如在關鍵水平上方或低於關鍵水平以下。 這是該戰略的簡明摘要：

1. **進入標準** ：
   - The current day's low is lower than the previous day's low.
   - The current day's close is higher than the previous day's close.
   - The 5-day RSI must be below 35, indicating potential oversold conditions.

2. **退出策略** ：
   - Green arrows on the chart signal buy entries.
   - Red arrows indicate exit points after a specified holding period.

3. **進行回測結果** ：
   - The strategy shows higher average gains as the holding period increases.
   - Exiting trades after 24 trading days yields an average gain of 2.02% per trade, with lower volatility compared to shorter holding periods.

4. **關鍵觀察** ：
   - Short-term exits (e.g., 1 day) result in a random walk-like equity curve, suggesting minimal edge.
   - Longer holding periods (up to 24 days) offer better returns and reduced volatility, indicating the strategy may be more effective with patient holding.

這種方法將技術指標和逆轉模式結合在一起，進行回測的表明，在較長的持有期間的性能提高了。
</details>

<details>
<summary>045. 59 Second Short-Term Reversal Strategy (That Works) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=ReWvN6BEMK0&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

有關的交易策略稱為 "Lower Lows and Lower Highs" 它是為各種股票ETF設計的平均回歸策略，包括QQQ，債券和國際股票。 這是一個簡明的摘要：

1. **策略概述** ：該策略通過在連續三天內觀察到較低的低點和較低的高點來確定趨勢，這表明了潛在的逆轉。

2. **進入信號** ：當一天的高和低點低於前兩天時，在始終如一的弱點的第三天觸發了買信號。

3. **退出信號** ：當收盤價超過前一天的高點時，交易已關閉，表明勢頭逆轉。

4. **表現** ：
   - **股權增長** ：從100,000美元開始，該策略在幾年內將近600,000美元的化合物佔了近600,000美元，每年的回報率近8％。
   - **平均增益** ：每個交易的收益約為1％。
   - **下降** ：在2000  -  2003年熊市期間發生了31％的大幅下降，但此後的性能一直很強。

5. **多功能性** ：該策略在包括債券和國際股票在內的各種ETF中有效。

該策略利用了回歸原則來利用ETF中的短期價格逆轉，儘管有很大的下降風險，但仍具有均衡的歷史成功方法。
</details>

<details>
<summary>046. Crude Oil Trading Strategy (Backtest + Setup)</summary>

[[Youtube]](https://www.youtube.com/watch?v=RjjoheELXKg&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

原油的交易策略涉及計算每日高低價格的25天平均水平，以確保在星期二或周四執行交易。 憑藉341筆交易，它的平均每次交易平均增長率為0.25％，獲勝率58％，最大降價為-7.5％。 這種系統的方法利用市場的波動和時間來實現一致的結果，儘管它需要紀律和適應能夠使市場狀況不斷發展。
</details>

<details>
<summary>047. Is THIS Larry Connors BETTER Than What 99% of Traders Are Trading? #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=SV-6yI5PNI8&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

拉裡·康納斯（Larry Connors）的策略涉及在關閉距離超過200天移動平均線時購買，低於5天移動平均線，並且過去五天中至少有四個。 銷售發生在昨天的高位超過昨天的高位時。 標準普爾500股票曲線表現出向上的增長，平均每貿易平均增長率為0.55％，年收益率為4％。 該策略僅使用200天的移動平均線，以確保看漲環境。 它的最大縮水量為13％，低於典型的趨勢範圍策略，使其適用於日間交易和搖擺交易。
</details>

<details>
<summary>048. Chat GPT Trading Strategy #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=TuhIGFNSwmU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略涉及使用chatgpt生成基本交易思想。 提到的具體策略使用了20個周期和兩個偏差因子的布林帶。 儘管股票曲線似乎是合理的，但重要的是要注意，不要期望chatgpt提供完美的策略。 相反，它是制定自己的模型和策略的起點。 這種方法強調了AI工具（例如Trading Bots）如何有助於為交易者生成新想法。
</details>

<details>
<summary>049. Momentum Trading Strategy (Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=Tz6V33LEFtY&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略涉及根據他們在過去三個月中的表現，對標準普爾500指數（股票：SPY）或黃金（股票：GLD）進行投資。 每個月，都選擇具有較高百分比回報率的資產進行投資。 從2005年開始，該投資組合通過利用這種基於勢頭的方法來增長到920,000美元。 該策略表明了強大的歷史回報，表明其有效性。
</details>

<details>
<summary>050. Pullback Trading Strategy (Trading Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=UU3CWUFdf1o&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

有關的交易策略是應用於標準普爾500指數的回調方法。 關鍵功能包括：

- **趨勢過濾器** ：以200天的移動平均線（MA）為趨勢指標。
- **算法交易** ：在特定條件下運行的自動化系統。
- **活躍時期** ：僅當標準普爾500指數高於其200天MA時，交易才表明上升趨勢。
- **表現** ：顯示出顯著增長，從五年來從100,000美元增加到100萬美元，獲得了10倍的回報。

該策略有效地利用趨勢關注原則來利用市場運動，同時遵守定義的趨勢過濾器。
</details>

<details>
<summary>051. Triple RSI Quantified Strategy (90% Win rate)</summary>

[[Youtube]](https://www.youtube.com/watch?v=VGWdcPdGD50&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

三重RSI交易策略以其對相對強度指數（RSI）的依賴而得名，旨在利用股票市場長期上升趨勢的回調。 這是該戰略的簡明摘要：

1. **進入條件** ：
   - The 5-day RSI must be below 30.
   - The RSI must have declined for three consecutive days.
   - The RSI reading three days prior was below 60.

2. **表現** ：
   - Since its implementation from 1993 to the present, it has generated only 83 trades.
   - It boasts an impressive win rate of 90%, with the average gain per trade being nearly 1.4%.

該策略旨在利用上升趨勢中的市場回調，利用RSI指標在原本不斷上升的趨勢中確定潛在的購買機會。
</details>

<details>
<summary>052. A CRUDE OIL Trading Strategy  (With Rules and Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=V_mmLWa6Q58&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

提出的交易策略涉及石油期貨，特別是使用25天平均或每日高的低範圍。 它要求在星期二或周四執行交易。 距離必須低於昨天的關閉範圍，並且位置在關閉之前保持24小時。 儘管建議進一步驗證，但2013年進行了回測的潛在有效性。

 **概括：** 

- **資產：** 石油期貨（CL）。
- **狀況：** 僅在星期二或周四進行交易。
- **進入信號：** 當前關閉<前一天的關閉 - 範圍（25天平均或高低範圍）。
- **位置持有：** 24小時。
- **回測結果：** 在2013年表現出了希望。

 **筆記：** 使用前始終驗證策略。
</details>

<details>
<summary>053. Dual Momentum Investing With Gary Antonacci  (Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=W5HtTSJMb0E&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**加裡·安東納奇（Gary Antonacci）雙重動量策略的摘要：** 

加裡·安東納奇（Gary Antonacci）的雙重動量策略，在他的書中詳細介紹 "Dual Momentum Investing," 涉及在選定的ETF之間採用動態分配方法，以利用市場勢頭。 該策略旨在根據每種資產對現金的相對績效每月轉移分配，旨在最大程度地提高收益，同時最大程度地減少衰退期間的風險。

 **關鍵組件：** 
1. **資產涉及：** 該策略通常包括間諜（標準普爾500指數），EFA（國際股票）和AG（可能是其他ETF或替代資產）。
2. **重新平衡頻率：** 每月，確保根據當前動量趨勢對投資組合進行調整。
3. **分配方法：** 資產與其相對績效成正比分配。 勢頭最強的資產獲得最大的分配，而其他資產則可能會收到較小的分配，或者如果表現不足，則沒有收到較小的分配。

 **表現：** 
- 到2019年，2004年的100,000美元投資增長到約328,000美元，表明年增長率（CAGR）約為7％，這與有效的動量策略績效一致。

 **注意事項：** 
- 儘管歷史表現很強，但未來的結果可能會有所不同。
- 該策略包括在沒有資產表現出積極勢頭的情況下持有現金，旨在在不利的市場條件下保留資本。

這種方法通過利用各種資產的動量動態來提供平衡的風險獎勵，提供了一種系統性而靈活的投資方法。
</details>

<details>
<summary>054. JIM SIMONS Trading System REVEALED (how he backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=WN2wds5QiXA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略涉及確定預測未來價格變動的指標。 使用歷史數據對這些指標進行嚴格的測試以確定其有效性。 如果指標有效，則將其納入系統的交易方法中； 如果沒有，它將被丟棄。 此方法可確保在交易系統中僅使用可靠和預測的元素。
</details>

<details>
<summary>055. Weekend Reversal Strategy - Step By Step (Results) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=WQcDDqLSZ0M&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略稱為 "Turnaround Tuesday" 戰略，幾十年來一直在股市有效。 這是該策略的摘要：

1. **進入信號** ：
   - On a Monday, if the closing price of the S&P 500 ETF (SPY) is lower than its price on the previous Friday, it triggers the entry signal.
   - This assumes that Friday was the last trading day before Monday.

2. **購買點** ：
   - Investors buy SPY at the close of trading on such a Monday.

3. **退出信號** ：
   - The exit occurs either on Tuesday if SPY closes higher than its previous day's (Monday's) high, or after five trading days, whichever comes first.
   -這意味著持有期是一天（星期二退出）或最多五天。

4. **理由** ：
   - The strategy aims to capitalize on short-term price movements following a downclose on Monday, with the expectation that SPY will rally by Tuesday or within five days.
   - It suggests that this approach has historically been profitable, as demonstrated by the example where $100,000 invested in SPY using this strategy grew to nearly $2.2 million over time.

該策略似乎是一種短期交易方法，可能利用市場動力和均值逆轉原則。 但是，重要的是要注意，過去的績效並不能指示未來的結果，並且應在個人風險承受能力和市場狀況方面仔細考慮任何投資策略。
</details>

<details>
<summary>056. Golden Cross Trading Strategy #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=WsuUqgp82yo&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

黃金交叉交易策略依賴於兩個不同時期的指數移動平均值（EMA） - 較短的50天和更長的200天。 它使用一個交叉系統，當較短的EMA交叉在較長的ema上方時，就會生成要購買的信號，這表明上升趨勢，並且當較短的EMA下降到較長的ema時，會觸發賣出信號，這表明潛在的下降趨勢。

在五年的時間裡，該策略表現出6.6％的複合年增長率（CAGR）為6.6％，略低於同期買賣策略的收益6.9％。 雖然性能差異並不顯著，但黃金交叉方法在波動市場期間的趨勢和鞭子或虛假信號的風險之間提供了平衡。
</details>

<details>
<summary>057. Death Cross Trading Strategies (Backtested+Rules) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=X9Dx8JMtlLo&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

當50天移動平均線突破200天移動平均線時，死亡十字架是一個技術交易指標，這表明潛在的趨勢逆轉。 儘管它臭名昭著地灌輸了對交易者的恐懼，但歷史表現表明，自1960年代以來，這種策略幾乎產生了平坦的回報，表明隨著時間的流逝，盈利能力最低。
</details>

<details>
<summary>058. If I Had To Learn Momentum Trading From ZERO! #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=XD-4aEAIrVU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略是一種基於勢頭的方法，該方法在兩個資產類別之間切換：標準普爾500（股票）和長期財政債券。 這是該策略的結構化摘要：

1. **分配的資產** ：投資組合由兩個ETF組成，這些ETF跟蹤標準普爾500指數和長期債券。

2. **執行頻率** ：在每個月結束時，該策略評估了過去三個月中哪些資產的性能更好，並將投資分配給下個月的ETF。

3. **性能示例** ：2003年的100,000美元投資增長到目前的920,000美元，表明十年來的顯著增長。 該策略每年比市場的表現高出約1％。

4. **考慮因素** ：
   - **簡單** ：策略很簡單，依靠兩個資產和每月重新平衡，從而減少了複雜性和管理需求。
   - **波動性管理** ：通過在股票和債券之間切換，該戰略旨在與僅持有股票相比，降低波動率。
   - **費用和稅收** ：頻繁的交易可能會產生交易成本和稅收影響，這可能會影響收益。
   - **市場周期** ：該策略似乎在不同的市場條件下有效，在不確定時期牛市和債券期間向股票轉移。

5. **潛在的缺點** ：
   - Reliance on recent performance (three months) might not always predict future outcomes.
   - Risk of overfitting historical data, which could affect live trading performance.

6. **結論** ：該策略提供了一種簡單而有效的方法，可以利用兩個資產類別之間的勢頭，並具有強大的歷史回報。 但是，潛在的投資者應根據其風險承受能力和投資目標考慮交易成本，稅收影響以及該策略的適用性。
</details>

<details>
<summary>059. Candlesticks Patterns Trading Strategies</summary>

[[Youtube]](https://www.youtube.com/watch?v=ZY6swQwQgLw&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

有關的交易策略通過定量分析和測試來系統地評估燭臺模式，以確定其有效性。 這是關鍵點的結構化摘要：

1. **客觀的** ：該策略旨在驗證燭臺模式是否可以可靠地產生利潤，超越軼事證據。

2. **方法論** ：
   - **定量分析** ：使用歷史數據對燭臺模式進行測試，包括成功和失敗的交易，以提供現實的績效評估。
   - **進行回測** ：在標準普爾500指數上進行，該標準普爾500指數顯示了20個淘汰的回報，比購買和持有的策略略有優勢（好1％）。

3. **性能指標** ：
   - The strategy outperformed a passive approach by a small margin, suggesting potential effectiveness.
   - Key metrics may include win rates, average returns, and risk-adjusted performance.

4. **考慮因素** ：
   - **過度擬合** ：該策略可能使用樣本外測試之類的方法來確保超出歷史數據的魯棒性。
   - **主觀性** ：燭臺模式在視覺上是基於視覺的，這可能導致不同的解釋。

5. **局限性和風險** ：
   - Performance may vary with market conditions; future results could differ.
   - Capital requirements and drawdown risks should be considered.

總之，該策略提供了一種數據驅動的方法來評估燭臺模式，從而在被動投資上提供了適度的優勢。 但是，有關方法和風險管理的更多詳細信息對於全面理解至關重要。
</details>

<details>
<summary>060. Russell 2000 Rebalancing Trading Strategy (Results) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=ZwOF8kOEQRM&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

russell重新平衡策略是一種年度交易方法，它利用了Russell 2000指數調整的時間。 貿易商在6月23日之後的第一個交易日購買指數，並在接下來的7月1日（如果7月1日不是市場日）出售該指數。 該策略利用了由指數重新平衡引起的價格變動，通常在過去二十年中每筆交易的收益率達到1.3％。 該戰略的有效性歸因於其年度執行和與羅素指數調整的一致性，從而確保每年一致性和盈利能力。
</details>

<details>
<summary>061. Options Expiration Week Trading Strategy #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=a2hGq4HKDqA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這種交易策略的重點是 "Options Expiration Week" （OPEX周），美國選項將在每個月的第三個星期五到期。 該方法涉及在OPEX Week的周一開放期間購買期權，並在OPEX Day結束時出售。 目的是利用坡度的向上傾斜趨勢，旨在隨著期權的價值朝著到期的發展而獲利。
</details>

<details>
<summary>062. Supertrend Indicator Strategy | Formula, Backtest, Settings | #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=aK9f8Ig6-ho&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

超級趨勢指標是一種趨勢跟隨工具，旨在根據價格動態頻段根據價格行動來識別潛在的買賣信號。 這是交易策略的簡明摘要：

1. **指標構建** ：超級趨勢指標是通過在指定期間的中位價格添加和減去平均真實範圍（ATR）來計算的。 這會在價格周圍產生上下邊界。

2. **條目規則** ：
   - **購買信號** ：當價格突破超過超級趨勢指標的上限時，輸入一個長位置。
   
3. **退出規則** ：
   - **賣出信號** ：當價格關閉超過超級趨勢指標的下部頻段時，退出貿易（關閉了長位置）。

4. **風險管理** ：適當的風險管理策略，例如設定止損訂單，對於在不利的市場轉移過程中保護資本至關重要。

5. **性能示例** ：假設使用該策略管理的1960年代的100,000美元的投資可能會增長到今天約400萬美元，從而展示了其潛在的有效性。

該策略旨在通過利用超級趨勢指標的動態性質來利用趨勢市場。
</details>

<details>
<summary>063. QQQ - TLT Strategy (With backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=auPTusg4zTo&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略是結合兩個資產類別以實現平衡增長和風險管理的一種結合結合的方法。 這是一個簡明的摘要：

1. **資產** ：側重於納斯達克100（QQQ）和長期國庫債券（TLT）。 這些資產的相關性較低，可以多樣化。

2. **策略類型** ：主要的職位很長，建議採用購買和趨勢的方法，可能使用技術指標來管理交易。

3. **利率** ：決策的關鍵因素，因為增長庫存（QQQ）對費率變化敏感。 該策略可以根據預期利率變動來調整暴露量。

4. **表現** ：在20年內帶來了令人印象深刻的12倍回報，跌幅超過20％。 這表明有效的風險管理和選擇性投資時間。

5. **投資時間範圍** ：僅投資58％的時間表明了一種保守的方法，可以在市場下跌期間的現金頭寸避免巨大的損失。

6. **風險管理** ：結合縮減控制和多元化。 提到購買和持有的QQQ最大值最高55％，突顯了其策略在減輕此類風險方面的重要性。

7. **考慮因素** ：潛在的風險包括意外的利率行為或資產類別的績效延長。 從長遠來看，經濟周期和通貨膨脹也可能影響回報。

總之，該策略通過多元化和選擇性投資有效地平衡了增長潛力與風險管理，這表明了強大的歷史表現。
</details>

<details>
<summary>064. VIX Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=bjkew9vMTAc&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

the總結的交易策略使用VIX索引，稱為 "fear index," 這意味著標準普爾500指數的期權的波動性。該策略涉及：

1. 與20天移動平均線相比，使用VIX。
2. 當VIX高於該平均水平（表明恐懼高）時，標準普爾500指數的平均每日回報率下降到0.3％。
3. 當VIX低於此平均值（低恐懼）時，回報率增加到0.5％。

這表明基於恐懼水平的交易，有可能避免或減少恐懼較高時的暴露。
</details>

<details>
<summary>065. Trading The ISM Manufacturing Index PMI (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=bxJaM1wZKJI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

the交易策略涉及使用ISM製造指數（PMI）作為在標準普爾500標準普爾500中進行交易的關鍵指標。這是一個簡明的摘要：

1. **指標** ：ISM製造PMI，反映了美國製造業的健康狀況。
2. **行動** ：
   - **購買信號** ：當PMI閱讀在本月初以上50。
   - **賣出信號** ：在下個月的開放式上出售。
3. **持有期** ：職位通常保留一個月。
4. **表現** ：
   - The strategy is active **72％的時間**，表明它在所有幾個月內都不保持職位。
   -它取得了成就 **年度回報率為7.3％**.
5. **關鍵好處** ：
   - Generates most gains when PMI readings are above 50.
   - Reduces drawdowns compared to a buy-and-hold approach.

該策略旨在利用強大的製造業健康（PMI以上50歲以上）與積極的市場運動之間的相關性，同時減輕下行風險。
</details>

<details>
<summary>066. 📊 Does January Predict the Stock Market’s Yearly Performance?</summary>

[[Youtube]](https://www.youtube.com/watch?v=cV-4aCIbI5M&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這種交易策略是基於這樣的想法：股市在一月份的績效可以預測其餘下的時間的績效，稱為 "January Barometer." 這是該策略的摘要：

1. **進入信號** ：如果一月份的標準普爾500指數的收盤價高於12月的收盤價，請在全年剩餘的時間內購買並持有標準普爾500指數。
   - Historical average gain: ~10.5% (excluding dividends).
   - This approach outperforms the returns of most random 11-month periods.

2. **退出信號** ：如果一月份的收盤價低於12月的收盤價，請清算該職位並避免在今年餘下的時間裡進行投資。
   - Historical average loss during these years: ~8%.

3. **性能洞察力** ：獲勝的年份（當一月份結束時）往往會產生近15％的平均收益，而損失年份的平均下降約為8％。 這種不對稱的回報使該策略有利。

從本質上講，該策略利用了一月份表現強勁的歷史趨勢，可以指示標準普爾500指數的積極一年。
</details>

<details>
<summary>067. Overbought trading strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=caWuJm7h5t0&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略是基於平均恢復原則，並著重於使用2天的RSI（相對強度指數）來識別過分買賣條件。 這是一個簡明的摘要：

1. **進入信號** ：當2天的RSI超過95時，在關閉時購買標準普爾500指數，表明狀況過高。
2. **退出信號** ：當2天的RSI降至70以下時，銷售銷售，這表明由於平均歸還而導致潛在的價格逆轉。

該策略利用較短的RSI計算來利用直接市場波動。 重要的是要注意，儘管這種方法使用技術指標，但有效的風險管理對於交易至關重要。
</details>

<details>
<summary>068. The Advance Block CANDLESTICK Pattern (Backtest and RULES)</summary>

[[Youtube]](https://www.youtube.com/watch?v=dwBstuKuJk4&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

討論的交易策略涉及分析 "Advanced Block" 燭臺圖案，通常是看跌，出現在看漲趨勢的末尾。 該模式由三個看漲蠟燭組成。 為了驗證其有效性，該策略的創建者使用S＆P 500數據對75種燭臺模式進行了回測。 結果表明，包括此模式在內的許多模式都表現良好。 有關更多詳細信息，請參閱提供的研究連結。
</details>

<details>
<summary>069. How To Find Great Trading Edges</summary>

[[Youtube]](https://www.youtube.com/watch?v=dzGTsLBJw9Y&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**交易策略的摘要：強調回測和增長** 

1. **進行回測的基礎** ：該戰略強調了對交易者的基本技能的重要性，強調了其在發展市場直覺中的作用並確定可利用的模式。

2. **現實世界的經驗** ：雖然紙質交易很有價值，但真正的貨幣交易是針對其獨特的情感見解強調的，這對於了解市場動態至關重要。

3. **文檔** ：建議保留所有策略的詳細記錄，無論結果如何。 這種做法使貿易商可以重新審視過去的努力，可能揭示隱藏的機會並從過去的經驗中學習。

4. **社區參與** ：鼓勵向成功的交易者學習並參與在線社區。 協作和反饋被認為對改進和支持至關重要。

5. **適應性和持續學習** ：該戰略強調了保持不斷變化的市場格局的重要性，主張在維持盈利能力的交易方法中持續學習和演變。

這種方法將技術技能發展與情感理解和社區支持融為一體，從而促進了成功交易至關重要的整體增長心態。
</details>

<details>
<summary>070. Strategy With Multiple Time Frames (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=eD-uHX60LY4&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略是一種多時間框架方法，旨在以優惠的價格進入趨勢。 這是一個結構化的摘要：

1. **客觀的** ：要與長期趨勢進行貿易，在短期回調中進行盤中交易。

2. **成分** ：
   - **長期趨勢濾波器（250天）** ：確保資產在上升趨勢中，確認當前關閉在250天前的關閉之上。
   - **中間趨勢過濾器（22天）** ：通過檢查近距離是否高於22天前，可以確認中期上升趨勢。
   - **條目規則** ：在盤中圖表上尋找短期回調以進入交易。

3. **理由** ：
   - Reduces risk by aligning with long-term trends.
   - Filters out false signals using multiple time frames.
   - Allows entry at better prices during temporary dips.

4. **考慮因素** ：
   - Risk Management: Tools like stop-loss orders are likely necessary but weren't specified.
   - Monitoring: Requires active intraday monitoring, potentially stressful for some traders.
   - Applicability: Suitable for stable assets; example used an ETF (XLP), adaptable to other assets.

5. **測試和評估** ：
   - Historical performance analysis needed to assess profitability and risk-reward ratios.
   - Consider transaction costs and slippage impacts on intraday trading.

6. **市場狀況** ：
   - Effective in trending markets; may underperform in flat or reversing markets.

該策略對於符合多個時間範圍分析和主動管理的紀律貿易商有效，提供了一種結構化的方法來利用趨勢。
</details>

<details>
<summary>071. Heiken Ashi Trading Strategy (Backtested)  #short</summary>

[[Youtube]](https://www.youtube.com/watch?v=eSHrfXSWd1s&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略基於Heikin-Ashi圖表技術，該技術起源於日本，並於1980年代後期被引入西方。 這是該策略的摘要：

### 要點：
1. **Heikin-Ashi圖表** ：
   - These charts display open, high, low, and close prices but are not based on real-time price data. They smooth out price movements, making trends more visible.
   - Heikin-Ashi is considered a lagging indicator, meaning it reflects past price actions and may delay signals.

2. **進入和退出規則** ：
   - **購買信號** ：當Heikin-Ashi蠟燭在其敞開之上交叉時，執行買入交易。
   - **賣出信號** ：當Heikin-Ashi蠟燭在其敞開以下越過時，執行賣出貿易。

3. **趨勢追隨性質** ：
   - The strategy is designed to follow trends, particularly on longer timeframes (e.g., daily or weekly charts).
   - It works best in trending markets and aims to capitalize on the continuation of price movements.

4. **性能指標** ：
   - **年回報** ：4.77％
   - **最大減收** ：23.1％
   - **夏普比率** ：0.52

5. **逆轉謹慎** ：
   - The strategy notes that reversals often occur when prices reach previous highs or lows, forming new trends.
   - Traders should exercise caution and be prepared for potential trend changes in such scenarios.

### 結論：
這種基於Heikin-Ashi的策略是一種趨勢跟蹤的方法，它利用價格變動的視覺平滑來識別潛在的進入和出口點。 儘管它提供了適中的年收益，並具有適度的風險回報比（如夏普比率所示），但交易者應意識到其滯後性質以及與趨勢逆轉相關的風險。
</details>

<details>
<summary>072. 87% Win rate! Percent B Strategy By Larry Connors #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=emLOxYW_FaI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

概述的交易策略利用了 "percent B" 指標，來自布林樂隊，具有特定參數和規則，以識別潛在的買賣信號。 這是該策略的結構化摘要：

### 關鍵組件：
1. **指標** ：百分比衡量收盤價相對於上和下布林帶的情況。 它通常範圍從0到1，值低於0.2，指示超售條件，高於0.8表示過多。

2. **布林樂隊參數** ：
   - Lookback Period: 5 days
   -標準偏差：2

3. **規則** ：
   - **購買信號** ：連續三天B級低於0.2時觸發，並且距離高於200天移動平均線。 該三重確認旨在濾除虛假信號並與長期上升趨勢保持一致。
   - **賣出信號** ：當閉幕超過昨天的高位時發生，這表明有上行的逆轉或獲利機會。

### 性能指標：
- **交易數量** ：大約55筆交易。
- **獲勝率** ：87％，表明55個交易中有48個是贏家。
- **風險獎勵比率** ：普通贏家和輸家的規模相似，表明風險獎勵平衡。

### 考慮和含義：
- **市場狀況** ：該策略在各種市場趨勢和條件上的表現可能不同。 建議在不同的時期和資產類別上進行測試。
- **信號頻率** ：該策略產生相對較少的信號，可能導致保守的交易方法，每個信號的獲利能力高。
- **位置尺寸** ：鑑於較高的獲勝率，除非考慮其他風險因素，否則位置規模可能不需要大量調整。
- **大體時間** ：尚未指定時間表，但為期5天的回顧建議是盤中或短期應用程式。 澄清這對於準確進行回測至關重要。

### 結論：
該策略似乎有效，重點是趨勢確認和波動性分析。 雖然它顯示出有希望的性能指標，但建議在各種市場和條件上進行徹底的回測，以評估其穩健性和適應性。
</details>

<details>
<summary>073. A Volatility Trading Strategy (Trading Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=gp3aBAq7uU0&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

the有關交易策略是一種定量方法，它利用了波動率的均值性質，特別有效地在標準普爾500中有效。這是一個結構化的摘要：

1. **策略概述** ：
   - **類型** ：定量，依靠數學模型和算法。
   - **重點** ：波動率平均逆轉，預計高波動性將重返歷史規範。

2. **目標資產** ：
   - Primarily suited for stocks, especially the S&P 500, known for its steady performance since 1993.

3. **概念基礎** ：
   - Belief that financial assets' prices and volatility revert to historical averages over time.
   - Opportunities arise when volatility deviates from these norms.

4. **實施注意事項** ：
   - Use of options strategies (e.g., straddles, iron condors) or technical indicators like Bollinger Bands or ATR.
   - Potential use of statistical models for identifying mean reversion signals.

5. **風險管理** ：
   - Crucial focus on risk mitigation techniques such as stop-loss orders and adjusting position sizes.

6. **市場周期** ：
   - Effective in high-volatility environments, such as bear markets, where spikes in volatility present trading opportunities.

7. **複製潛力** ：
   - While exact rules aren't provided, replication could involve studying volatility indicators, using options strategies, and developing quantitative models.

8. **結論** ：
   - A consistent, long-term strategy leveraging the predictable nature of volatility in stable assets like the S&P 500, requiring careful analysis and risk management.

該策略強調了了解市場動態並採用強大的分析工具來利用資產價格效率低下的重要性。
</details>

<details>
<summary>074. End Of Month Trading Strategy  (Trading Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=hAkoewf_QKI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

您指的交易策略是基於季節性效應 "Turn of the Month" 戰略。 這是一個簡明的摘要：

- **購買信號** ：在一個月的第五個交易日中輸入一個長位置。
- **賣出信號** ：退出交易，並在新月後的第三個交易日平坦（或佔用很短的位置），該交易通常與本月後期相對應。

人們已經注意到，自1960年以來，該策略捕獲了標準普爾500指數中的所有收益，這表明它在這些特定時間範圍內利用了重要的市場模式。
</details>

<details>
<summary>075. 88% Winrate!  R3 Trading Strategy By Larry Connors</summary>

[[Youtube]](https://www.youtube.com/watch?v=igM25-w1S8I&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

R3交易策略利用相對強度指數（RSI）在看漲市場中識別潛在的賣點。 這是一個簡明的摘要：

1. **進入條件** ：收盤價必須高於200天移動平均線，以確認看漲的趨勢。
2. **賣出信號** ：
   - The two-day RSI must have decreased for three consecutive days.
   - Today's two-day RSI must be below 20.
3. **退出信號** ：賣出兩天的RSI上升到70以上。

 **性能指標** ：
- **交易** ：94
- **獲勝率** ：88％
- **平均每次交易** ：1.16％
- **市場敞口** ：4.57％（花費95.43％的現金時間）

該策略是為保守方法而設計的，可以使市場敞口最少，同時利用具有高利潤率和損失量較低的強賣信號。
</details>

<details>
<summary>076. Seasonality Short Strategy With Backtest</summary>

[[Youtube]](https://www.youtube.com/watch?v=it3Hvl75K_s&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

季節性短期策略涉及將歷史上最糟糕的一周作為股票市場的目標，該股市發生在9月下半年。 該方法很簡單：在9月的第三個星期五，Short The S＆P 500，並保持了一周的職位。 自1960年以來，該策略的平均增長率為0.9％。 這種方法特別有吸引力，因為它利用了市場上定義明確的季節性異常，為短期交易策略提供了難得的機會，由於長期股票欣賞趨勢，這通常是具有挑戰性的。
</details>

<details>
<summary>077. Limit Order Book Trading Strategy (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=iw9VZ3Usapc&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略側重於分析限制訂單簿，該書詳細介紹了所有特定工具的買賣訂單。 雖然它提供了有關競標（買）和詢問（賣出）訂單的結構的見解，但由於其複雜性和進行回測的困難，尤其是零售交易者，該戰略建議不要僅依靠這種方法。

相反，建議是通過 **量化策略** 經過徹底的測試。 這些策略旨在通過利用數據驅動模型來增強決策。 對於有興趣探索此類策略的人 [jenterifiedstrategies.com](https://quantifiedstrategies.com) 在過去的十年中，提供大量免費資源。
</details>

<details>
<summary>078. The Market Timer Every Investor Should Know #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=jZT_EU0ylzA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

理察·法比安（Richard Fabian）在1960年代開發的Fabian定時模型是一種定量的長期趨勢跟蹤策略。 它涉及監視包括標準普爾500在內的三個主要指數，以確定它們是否高於各自的39周移動平均值。 當這三個指數符合此情況時，該模型建議對它們進行投資。 自2000年以來，這種方法的表現優於標準普爾500號，其餘量很大，強調了其作為一種基於系統的，基於趨勢的策略的有效性。
</details>

<details>
<summary>079. Martingale Trading Strategy - Gambling (Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=jhyDa7DdRC8&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

martingale交易策略是一種基於賭博的方法，每次損失後，交易者的投注大小加倍。 儘管它旨在恢復以前的損失，但該策略變得越來越風險和不切實際，尤其是在交易方案中。 該策略通常會導致財務損失，因為其賭注量的指數增加可能會迅速超過可管理的風險水平。 正如強調的那樣，通常認為這種方法不適合交易者。

 **回答：** martingale策略在每次損失後都會加倍賭注，但固有的風險和不切實際的交易是不切實際的。
</details>

<details>
<summary>080. IBS Strategy - The Best Kept Secret In Trading</summary>

[[Youtube]](https://www.youtube.com/watch?v=kc4jxkrYG4Q&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略稱為內部欄強度（IBS）指標。 這是一個簡明的摘要：

- **IBS指示器** ：用於股票市場交易的工具，每天計算，值範圍從0到1。
- **交易規則** ：
  - **購買信號** ：當IBS低於0.1時輸入交易。
  - **賣出信號** ：IBS高於0.9時退出交易。
- **進行回測結果** ：使用ThinkTrader（Amibroker）在ETF QQQ上測試。 從2000年開始，該策略在2023年增長到約150萬美元，在23年內獲得了14倍的回報。

該策略根據歷史表現有效，但可能無法保證未來的結果。
</details>

<details>
<summary>081. MACD Mean Reversion Strategy (Step-By-Step &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=klDDF9Of5zI&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略基於MACD（移動平均收斂差異）直方圖。 這是該策略的摘要：

### 策略概述：
- **MACD直方圖** ：直方圖是通過從更快的MACD線中減去信號線來計算的。
- **平均歸還方法** ：該戰略利用意味著恢復，並期望價格在偏差後恢復其歷史平均水平。

### 交易規則：
- **進入信號** ：當MACD直方圖從四天前低於零的水平連續四天下降四天時，將開始長位置。 這表明條件過多和潛在的價格逆轉。
- **退出** ：該策略沒有指定退出規則，但這暗示著在條件逆轉或預定義的利潤目標之前一直保持職位。

### 表現：
- **股權增長** ：儘管年收益率為5％，但沒有超過標準普爾500指數的購買和持有效果，但由於其市場敞口較低（只有5％），該策略被認為是不錯的。
- **獲勝率** ：該策略的高勝率為89％，表明大多數交易都是有利可圖的。
- **下降** ：在16％的情況下，經歷的最大降低相對較低，這表明最小的峰值損失。

### 策略優勢：
- **投資時間較低** ：在市場上花費的有限時間使交易者可以專注於其他互補策略，從而提高了整體投資組合效率。
- **陽性率和降低** ：高獲勝率和可管理的降低的結合使其對規避風險的投資者有吸引力。

### 策略缺點：
- **每個交易的少量利潤** ：每個交易都會產生少量的利潤，但是隨著時間的流逝，這些利潤會很好地複雜化。 但是，每種利潤的小規模可能不會吸引那些在較短時期尋求更高回報的人。

總而言之，這一基於MACD的戰略是一種保守的方法，它利用最小的市場敞口來利用均值回歸，提供高的獲勝率和可管理的降低，儘管它可能無法提供大量的短期利潤。
</details>

<details>
<summary>082. Night Trading Strategies (Facts, Statistics and Backtests)</summary>

[[Youtube]](https://www.youtube.com/watch?v=l4_oSEBjlX4&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所討論的交易策略涉及使用Spy，這是跟蹤標準普爾500標準普爾500的ETF，重點是從市場靠近下一個開放或關閉的市場交易。 這是該戰略的簡明摘要：

1. **進入信號** ：該策略連續三個下關閉價格連續三個時觸發了買入信號。 這意味著每天的關閉時間比前一天要連續三天低。

2. **執行** ：在第三下關閉時，交易者在市場上購買間諜，並保持該職位，直到下一個交易日開放或關閉。

3. **表現** ：自1993年以來，該策略已執行643筆交易，平均每次交易0.13％。 它只經歷了25次輸掉交易，表明較高的獲勝率。

4. **風險和考慮因素** ：
   - **市場波動** ：隔夜職位使交易者面臨新聞事件或地緣政治問題等市場風險。
   - **交易成本** ：頻繁的交易可能會產生大量的佣金費用和出價差價，這可能會影響盈利能力。
   - **流動性和槓桿作用** ：間諜的流動性是有利的，但是槓桿使用可以擴大損益。

5. **執行** ：該策略可以自動化，從而可以在不進行日常監控的情況下進行系統的執行。

6. **市場狀況** ：性能在不同的市場環境中可能有所不同（公牛與熊），在下降趨勢方面有更多的機會，但在上升趨勢方面的增長有可能。

7. **心理因素** ：隔夜持有需要紀律才能遵守該戰略，儘管市場波動性，強調與短期波動的情緒脫離。

8. **可伸縮性和魯棒性** ：如果越來越多的交易者採用策略的有效性，可能會影響市場行為。

總而言之，該策略利用較高的勝利率在許多交易中利用少量的收益，但其成功取決於仔細考慮交易成本，市場狀況和心理方面。
</details>

<details>
<summary>083. Closed-End Fund Investment Strategy (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=lMyPmQRHWiQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

交易策略涉及利用封閉式基金的價格與其淨資產價值（NAV）之間的差額。 這是一個簡潔的崩潰：

1. **使用的指示器** ：該策略跟蹤兩天內價格與NAV比率的相對強度指數（RSI）。

2. **進入信號** ：當RSI越過10以下時，將採取長期位置，表明價格與NAV的比率超出了。

3. **性能指標** ：
   - **交易數量** ：212
   - **平均每次交易** ：48％
   - **最大減收** ：67％

該策略利用勢頭指標來利用潛在的低估，提供高回報，但由於大量縮減而有很大的風險。
</details>

<details>
<summary>084. How Jim Simons MADE BILLIONS Trading</summary>

[[Youtube]](https://www.youtube.com/watch?v=mpeOC8tq3YU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略是一種系統的方法，依賴於技術分析和自動化。 這是一個簡明的摘要：

1. **確定預測指標** ：該策略首先確定諸如技術指標（例如移動平均）或被認為可以預測未來價格變動的模式。

2. **進行回測** ：這些潛在的預測元素將通過對歷史數據進行回測測試。 此步驟可確保該策略在不同的市場條件和時間段內的有效性。

3. **算法開發** ：基於確定的指標開發交易算法。 如果該算法在測試過程中被證明有效，則將實施； 否則，它將被丟棄。

4. **自動化** ：經過驗證後，按照算法的規則自動執行交易。 這種自動化旨在消除手動交易可能發生的情感決策。

5. **示例策略** ：提供的一個示例是使用100天的移動平均值來購買，當價格超過其以上並在下降時出售。 自動化確保沒有人類情感的一致執行。

這種方法強調紀律，一致性以及通過技術驅動的執行來消除情緒偏見。
</details>

<details>
<summary>085. iNVERTED YIELD CURVE Investment Strategy (Rules and backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=nDL_k9FI5qM&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

討論的交易策略涉及兩種基於倒置曲線的方法，這種現象是短期利率高於長期利率的現象，通常表明即將來臨的經濟衰退。 這是該戰略的簡明摘要：

1. **購買和保持方法** ：
   - When the yield curve inverts, buy the S&P 500 index.
   - Hold the investment for either 250 or 500 days.
   - Since 1976, this approach has yielded an average gain of 7.35% over 250 days and 18.3% over 500 days, which is comparable to a long-term buy-and-hold strategy.

2. **基於RSI的方法** ：
   - Use the Relative Strength Index (RSI) on the yield curve.
   - Buy when the RSI reaches oversold levels (below 20) and sell when it reaches overbought levels (above 80).
   - Since 1976, this strategy has resulted in 102 trades with an average gain of 2.5% per trade.

兩種策略都旨在利用倒置曲線指示的市場狀況。 有關更多詳細信息或其他策略，請訪問 [jenterifiedstrategies.com](https://quantifiedstrategies.com).
</details>

<details>
<summary>086. High-Frequency Trading Strategy (Backtest And Rules) - HFT</summary>

[[Youtube]](https://www.youtube.com/watch?v=nTwvkXCx8Bc&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

高頻交易（HFT）是一種交易策略，它使用強大的電腦程式來執行一秒鐘的大量交易，利用算法策略，速度和高離職率來利用小型，短暫的市場機會。 這種方法是高度資本密集型，技術上複雜的，需要基礎架構，例如位於交流附近的VPS服務，以最大程度地減少延遲。 結果，對於大多數零售商人來說，這是不可行的。

作者提出了一種稱為的替代策略 "slow-frequency trading," 他們認為，對於個人交易者來說，這更容易及其實用。 他們在其網站量化strategies.com上為此方法發表了許多策略。
</details>

<details>
<summary>087. Inverted Yield Curve Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=p_i51TbAReQ&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**使用產量曲線的交易策略摘要** 

基於收益曲線的交易策略涉及理解兩個關鍵概念：正常和倒置的屈服曲線。 一個 **正常產量曲線** 當更長的到期債券提供的收益率高於較短的收益率時，就會存在，這反映了與較長時期內投資相關的風險增加。 相反，一個 **倒的產量曲線** 當短期債券的收益率高於長期的債券時，就會發生這種情況，這可以表明潛在的經濟變化。

該策略採用兩種方法：

1. **反轉觸發的策略** ：這涉及在收益曲線倒轉並在250天後出售時購買資產。 自1976年以來，這種方法的平均回報率為7.3％，最大降低為18％，在同一時期表現優於標準普爾500的4.3％回報。

2. **基於坡度的策略** ：該策略使用收益曲線的斜率指導投資。 正斜率（正常曲線）提示很長，而負斜率（倒曲線）會導致較短的位置。 這種方法的平均回報率為8.3％，最大降低為20％。

兩種策略都優於標準普爾500標準普爾500，但並非沒有風險，因為它們的大量下降證明了這一點。 結論強調，雖然倒的產量曲線可能是有用的指標，但由於與其他指標的潛在衝突以及不可預測的市場中的不可預測性，它們應該成為更廣泛的投資策略的一部分。 因此，對此類指標的依賴應與其他因素保持平衡，以實現更可靠的預測。
</details>

<details>
<summary>088. End Of The Month Trading Strategy #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=qYkWXA_aqjU&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略涉及針對標準普爾500指數的短期方法。 這是一個簡明的摘要：

### 策略概述：
- **入口點：** 在每個月的第五交易日結束時購買。
- **出口點：** 在下個月的第三交易日結束時出售。
- **理由：** 該策略旨在在此特定窗口中利用市場價格的季節性集會。
- **年度回報：** 大約7.1％，表明一致但適中的盈利能力。

### 主要注意事項：
- **定時邏輯：** 基於歷史數據，指示從一個月的第五天到下一個的第三天的價格變動，可能受經濟報告或機構交易模式等因素的影響。
- **風險和成本：** 潛在的風險包括市場不可預測性和交易成本。 頻繁的交易可能會產生費用和滑倒，從而減少回報。
- **自動化：** 該策略可以自動化以提高效率和減少人為錯誤。

### 結論：
儘管該策略的歷史回報率為7.1％，但考慮市場變異性，經濟狀況和相關交易成本至關重要。 在這些時期內價格流動的根本原因的進一步研究可以增強理解和風險管理。
</details>

<details>
<summary>089. 2 Important Tips In Trading</summary>

[[Youtube]](https://www.youtube.com/watch?v=rxgWWEWkx0o&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

概述的交易策略強調了成功的兩個關鍵組成部分：

1. **積極的統計預期** ：這涉及通過對歷史數據進行反測試製定策略。 儘管過去的表現並不保證未來的結果，但它被認為是一個可靠的起點。 積極的期望表明，隨著時間的流逝，該策略可能會產生利潤。

2. **紀律和遵守計劃** ：即使市場挑戰您的立場，也必須堅持該戰略。 情感決策，例如儘早退出交易或承擔過度風險，可能會破壞長期成功。

總而言之，該策略著重於具有經過驗證的優勢的經過良好測試的方法，並在執行它時保持嚴格的紀律。
</details>

<details>
<summary>090. Silver Future Trading Strategy (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=ry3MZFLItUA&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這是描述的交易策略的摘要：

 **策略名稱：** 白銀未來貿易策略
 **關鍵功能：** 
- **樂器：** 白銀期貨（白銀期貨）
- **類型：** 一日交易（擔任幾個小時的職位）
- **進入標準：** 基於兩個季節性變量。
- **退出標準：** 簡單的時間退出（幾個小時後）。

 **績效指標（2005年至今）：** 
- 總交易：超過700
- 平均每個交易增益（無槓桿）：〜0.2％
- 獲勝率：64％
- 利潤因子：2.3
- 最糟糕的一年（2009年）：仍然是積極的，年收益為1.5％。

 **結論：** 儘管大宗商品交易具有挑戰性，但該策略表明了一致的盈利能力的潛力，尤其是在白銀期貨中。 有關更多詳細信息或其他策略，請訪問 [jenterifiedstrategies.com](https://quantifiedstrategies.com).
</details>

<details>
<summary>091. Swing Trader Strategy (Backtest &amp; Trading Rules) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=tnw8GHYXj-Q&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

**搖擺交易策略摘要** 

the概述的策略是一種搖擺交易方法，重點是標準普爾500指數的潛在短職位。這是一個簡明的細分：

1. **進入條件：** 
   - The S&P 500 index closes at a new low for the past five days.
   - The IBS (indicator behavior unknown, but assumed to be related to momentum or volume) is below .25.

2. **退出條件：** 
   - Sell and close the short position when the closing price exceeds yesterday's high.

該策略旨在利用技術指標來過濾和退出點後利用潛在的短期校正。 該策略表明，在特定的看跌條件下進行短貿易，並在與前一天的高價相對於價格轉移時退出。
</details>

<details>
<summary>092. The Money Flow Index (MFI) Trading Strategy #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=udVDs7FDTfM&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

這是交易策略的簡明摘要：

這 **貨幣流量指數（MFI）** 是將資金流入或從擔保中衡量的勢頭指標。 該策略涉及以下步驟：

1. **進入信號** ：
   - Buy at the close when the two-day MFI is below 10. This indicates low buying pressure and potential undervaluation.

2. **退出信號** ：
   - Sell at the close if the current day's high exceeds yesterday's high, signaling upward momentum and a potential price reversal.

3. **表現** ：
   -進行回測的結果表明，通過這種策略，1993年的100,000美元到1997年可能會增長到超過200萬美元，到2000年將超過450萬美元。

這種方法旨在利用低購買壓力，然後是強勁的向上移動。
</details>

<details>
<summary>093. Bullish Harami Pattern: Rules, Strategy, and Backtested Results</summary>

[[Youtube]](https://www.youtube.com/watch?v=xF5Ow4o218w&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

看漲的哈拉米交易策略是一種兩種狂歡的模式，在下降趨勢期間形成，標誌著潛在的逆轉。 這是一個結構化的摘要：

### 關鍵組件：
1. **模式識別** ：
   - **第一支蠟燭** ：一隻大的看跌蠟燭，有著長紅色的身體，表明銷售壓力很大。
   - **第二蠟燭** ：一個小的看漲蠟燭（通常稱為 "doe" 或綠色蠟燭）完全被第一支蠟燭的身體所吞噬。 這意味著市場猶豫不決。

2. **市場環境** ：
   - The pattern occurs during a downtrend, suggesting bearish momentum before showing signs of potential reversal.

3. **交易規則** ：
   - Hold the trade for approximately 10 days.
   - Entry signal is when the bullish harami pattern is identified.

### 性能指標：
- **獲勝率** ：在55％至70％之間，取決於持有期。
- **風險與獎勵比率** ：平均每個交易的利潤約為風險的2.5倍，與潛在損失相比有利。

### 考慮和問題：
1. **圖案細節** ：
   - Clarify if specific conditions (like wick length or color) are required beyond candle size and engulfment.
   
2. **持有期** ：
   - Holding for 10 days suggests it's a swing trading strategy, leveraging potential trend reversal rather than intraday movements.

3. **風險管理** ：
   - Understand how risk is measured (e.g., stop-loss placement) and its impact on overall strategy performance.

4. **市場狀況** ：
   - Consider how the strategy might perform in varying market environments, such as strong uptrends or periods of high volatility.

5. **歷史表現** ：
   - Examine the equity curve for volatility and drawdowns, recognizing that while returns are attractive, losses can occur.

6. **戰略邏輯** ：
   - The strategy likely hinges on a reversal after a downtrend, capitalizing on market indecision before potential upward momentum.

7. **變化和信譽** ：
   - Explore variations of the pattern and seek insights from other traders to gauge reliability across different market conditions.

### 結論：
看漲的哈拉米是一種有前途的策略，其歷史表現表明盈利能力。 但是，在識別模式時進行徹底的分析和實踐至關重要。 了解其機制，潛在的陷阱和對市場變化的適應性將是成功實施的關鍵。
</details>

<details>
<summary>094. Meb Faber Ivy ETF Portfolio (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=xSIQcXin12w&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

概述的交易策略 "Ivy Portfolio" meb Faber和Eric W Richardson旨在通過使用ETF的多元化方法來複製常春藤聯盟大學捐贈的表現。 投資組合由五個同等加權的ETF（每個分配的20％）組成，旨在反映機構投資中看到的多元化，包括對商品，房地產和其他替代資產的敞口。

該策略的年收益率為4.6％，由於商品績效差而低於歷史平均值。 這種方法適合尋求類似於機構投資組合的可訪問多元化的長期投資者，但必須指出的是，其回報與商品價格緊密相關，這可能是波動的，可能會影響整體績效。
</details>

<details>
<summary>095. NR7 Strategy From Toby Crabel in 1990 (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zF0UXJJHmHc&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

託尼·克拉貝爾（Tony Krabelle）於1990年制定的NR7交易策略是一種基于波動率的方法，旨在利用低波動性時期，然後是趨勢運動。 這是該策略的結構化摘要：

### 策略概述：
- **客觀的** ：在強烈的向上運動發生時，要在低波動和退出期間進入市場。

### 關鍵組件：
1. **波動率測量** ：
   - Volatility is defined as the difference between the daily High and Low prices.
   - The strategy identifies entry points when today's range (High-Low) is the smallest among the previous six trading days.

2. **進入信號** ：
   - Enter a long position at the close of the day if today's range is the lowest in the last six days.

3. **退出信號** ：
   - Exit the trade when the current day's closing price exceeds the previous day's high, then close the position at the end of that day.

### 進行回測結果：
- 從1993年開始測試，展示了100,000美元的起始資本。
- 以8％的年化增長率達到了向上的股票曲線。

### 考慮和含義：
- **市場狀況** ：在高波動期或各種資產類別（股票，外匯，商品）中，該策略的性能可能不同。
- **風險管理** ：潛在的風險包括交易成本，打滑以及過去的績效不能保證未來的結果。
- **心理方面** ：儘管市場波動，但仍需要紀律遵守進入/退出規則。
- **自動化** ：該策略可以自動化以有效執行。

### 結論：
NR7是一種利用低波動性周期的簡單而有效的趨勢遵循策略。 雖然對測試結果顯示出令人鼓舞的結果，但交易者應考慮在不同的市場和條件上進行其他測試，並注意相關的風險和成本。
</details>

<details>
<summary>096. A Penny Doubled Every Day For A Month</summary>

[[Youtube]](https://www.youtube.com/watch?v=zhaE_JgbUSM&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq)

所描述的交易策略的重點是複雜興趣的概念，強調了小規模的初始投資如何導致隨著時間的推移顯著增長。 這是一個簡明的摘要：

1. **初始投資** ：從最少的數量開始，例如一分錢。
2. **每日增長** ：投資每天在指定期間（例如30天）增加一倍。
3. **指數增長** ：通過複合興趣的力量，最初的小儲蓄呈指數增長。 例如，在30天內，投資可以增長到5,368,709.12美元。
4. **長期利益** ：這種策略強調，讓您的資金通過複雜的利益增長可能會帶來豐富的財務獎勵。
5. **打電話給行動** ：該信息鼓勵提早開始，並允許複雜的興趣為一個更美好的財務未來而努力。

這種方法強調了複合的重要性和從少量節省開始的好處。
</details>

