### TRADING STRATEGIES 2024 (Backtested With Rules And Logic) (中文)

---

<details>
<summary>001. Overnight Trading Strategy (+Backtest) | NIGHT TRADING</summary>

[[Youtube]](https://www.youtube.com/watch?v=-ML4YWkC6to&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 小節整理：隔夜交易策略在SPY (S&P 500 ETF) 中的應用

#### 主題
- 隔夜交易策略在SPY（跟蹤標普500指數的ETF）中的應用。
- 如何通過隔夜交易實現盈利。

#### 交易商品
- SPY：跟蹤標普500指數的ETF，作為主要交易標的。

#### 策略細則
1. **交易信號**：
   - 當出現連續第三個較低收盤價時（即連續三天收跌），在收盤時買入。
   - 持有至次日開盤，隨後賣出。

2. **操作流程**：
   - 從收盤到次日開盤或收盤期間保持最大持倉。
   - 離場時機：次日開盤時平倉。

#### 回測績效
1. **原始策略**（出場於次日開盤）：
   - 總交易次數：643次。
   - 平均每筆交易收益：0.13。
   - 勝率：65%。
   - 最大回撤：8%。

2. **改進策略**（出場於次日收盤）：
   - 平均每筆交易收益提升至0.24。
   - 勝率下降至60%。
   - 最大回撤增加至17%。

#### 策略優化
- 可通過調整出場時機優化績效，但需權衡勝率與最大回撤。

#### 結論
- 隔夜交易策略在SPY中具有可操作性。
- 改進策略雖收益提升，但風險增加。
- 作者採用類似策略，實現平均每筆交易0.35的收益，但交易次數減少。
- 建議有興趣者訪問網站獲取更多細節與代碼。

#### 其他
- 強調SPY價格（400美元）足以覆蓋滑點與佣金成本。
- 鼓勵觀眾點讚、訂閱，並期待更多相關視頻。
</details>

<details>
<summary>002. 3 SIMPLE Trend Following Trading Strategies (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=0kJ_fWP5fKU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 本文要點整理

#### 主題：趨勢跟隨（Trend Following）策略在投資中的應用

1. **定義與核心思想**
   - 趨勢跟隨策略旨在捕捉金融市場中延伸的漲跌行情，無論上漲或下跌。
   - 不基於未來預測，避免判斷市場頂底，通過跟隨現有趨勢來獲利。

2. **交易商品**  
   - 本案例研究主要圍繞美國標普500指數（S&P 500）展開。

3. **使用指標**
   - **跨月策略**：基於月線圖，使用12個月簡單移動平均線。
   - ** golden cross 策略**：基於日線圖，利用50天和200天移動平均線的交叉來判定買賣信號。
   - **Super Trend 指標**：基於週線圖，通過計算中位價並附加bands（通道）來判斷趨勢變化。

4. **策略細則**
   - **跨月策略**：
     - 規則一：當月度收盤價突破12個月簡單移動平均線，做多。
     - 規則二：當月度收盤價跌破12個月簡單移動平均線，賣出並持現金直至買入信號出現。

   - **Golden Cross 策略**：
     - 規則一：50天移動平均線突破200天移動平均線，發出買い信號。
     - 規則二：50天移動平均線跌破200天移動平均線，賣出並平倉。

   - **Super Trend 策略**：
     - 規則一：當收盤價突破Super Trend指標的前一期值，發出買い信號。
     - 規則二：當收盤價跌破Super Trend指標的前一期值，發出賣出信號。

5. **回測績效**
   - **跨月策略**：
     - 年化報酬率：接近6%。
     - 投資持股天數：約62%時間持有股票。
     - 調整後報酬（基於投資時間比例）：約9.5%。

   - **Golden Cross 策略**：
     - 年化報酬率：接近6%。
     - 投資持股天數：約62%時間持有股票。
     - 調整後報酬：約9.5%。

   - **Super Trend 策略**：
     - 年化報酬率：接近6%。
     - 投資持股天數：約62%時間持有股票。
     - 風險調整後報酬：約9.5%。

6. **結論**
   - 趨勢跟隨策略具有簡單易行、管理成本低等優點，適合長線投資者。
   - 策略缺點包括高頻率的虧損交易和趨勢突然反轉的風險，需心理承受能力強並避免過早.EXIT短กำไร。
   - 推薦配合其他策略（如波段交易）以優化整體_Portfolio表現。
</details>

<details>
<summary>003. Death Cross Trading Strategies (Backtested+Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=12al7KQInww&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章精要整理

#### 主題  
- **死亡交叉交易策略**：介紹_death cross_ 指標的工作原理、歷史意義及其在股票市場中的應用。

#### 交易商品  
- 股票（包括個股和指數）
- 其他資產類別（如ETFs、加密貨幣、CFD、外匯及期貨），但需針對每種.asset進行驗證。

#### 使用指標  
- **死亡交叉**：由短期移動平均線（通常為50日）跌破長期移動平均線（通常為200日）形成。
- 作為一個lagsging指標，反應價格走勢後事件。

#### 策略細則  
1. **死亡交叉的形成條件**：
   - 短期MA（紅色線）跌破長期MA（藍色線）。
2. **交易信號**：
   - 發出賣出信號，表徵股市可能進入熊市或回報率下降期。
3. **時間框架**：
   - 常用每日K線圖進行分析。

#### 回測績效  
1. **歷史表現**：
   - 自1960年以來，Equity曲線顯示幾乎未賺錢，即使持股時長達30%。
2. **死亡交叉次數**：
   - 1960年至2023年間共發生32次死亡交叉，每次均帶來股災。
3. **成功率**：
   - 成功率高達75%，但更重要的是平均每筆交易的收益。

#### 結論  
- 死亡交叉是一種有效的熊市信號，但需謹慎使用，因其可能導致長期空倉，錯失股市上漲紅利。
- 建議結合其他指標或策略以提高勝率。
- 黃金交叉（Golden Cross）為其對應的牛市信號，值得進一步研究。

#### 其他  
- **黃金交叉**：短期MA重回長期MA上方，表徵可能的牛市來臨，將在下一視頻深入探討。
</details>

<details>
<summary>004. Friday 13th Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=22GwTbRFrzE&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章總述
本文探討了「黑色星期五」（Friday the 13th）在金融市場中的 superstition及其實證表現。研究分析了自1960年以來標準普爾500指數（S&P 500）在該日的歷史數據，旨在驗證此日是否具備不祥之兆。

---

### 主題
- 探討黑色星期五在股票市場中的 luckiness。
- 分析S&P 500在黑色星期五的表現。

---

### 交易商品
- 標準普爾500指數（S&P 500）。

---

### 使用指標
- 紐約證券交易所（NYSE）平均漲跌幅。
- S&P 500 historical performance.

---

### 策略細則
1. **交易日選擇**：集中於黑色星期五（即每月的第十三個且為星期五的日子）。
2. **數據範圍**：分析自1960年以來的歷史數據。
3. **績效評估**：比較黑色星期五與一般交易日的平均漲跌幅。

---

### 回測績效
- 黑色星期五的平均漲幅為0.12%。
- 一般交易日的平均漲幅為0.3%。
- 結論：黑色星期五的表現略優於一般交易日，但整體差異不大。

---

### 結論
- 根據歷史數據，黑色星期五並非股市中的不祥之日。
- 證據表明，此日的表現並不劣於一般的交易日。
- 因此，可否定將黑色星期五視為「不幸」的 superstition。

--- 

此文總結了研究結果，並提出了一種基於歷史數據的交易策略，為投資者提供了客觀的參考依據。
</details>

<details>
<summary>005. MULTIPLE Time Frame Trading Strategy (+Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=2fASgIgUPrw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 多重時間框架交易策略解析

## 一、主題與目的  
多重時間框架交易策略旨在通過結合不同時間尺度的市場信息來捕捉交易機會，同時降低風險。本研究提出了一種具體的策略鱤式，並提供了回測結果以驗證其有效性。

---

## 二、交易商品  
本次交易策略應用於以下金融商品：  
1. **標的指數**：XLP（Consumer Staples ETF）  
2. **時間框架**：  
   - 長期趨勢：周線圖（250天）  
   - 中期趨勢：日線圖（22天）  
   - 短期回撤：小時圖（3天）

---

## 三、策略細則  
本策略基於以下規則設計：  

1. **長期趨勢指標**：  
   - 現價需高於250天前的收盤價，表明存在上行趨勢。  

2. **中期趨勢指標**：  
   - 現價需高於22天前的收盤價，確保短期市場情緒積極。  

3. **短期回撤條件**：  
   - 今天收盤價必須是過去3天的最低收盤價，表明價格可能在短期內觸底反彈。  

4. **入市規則**：  
   - 若上述條件均滿足，於今日收盤時建倉做多。  

5. **出市規則**：  
   - 獲利平倉：當日收盤價高於昨日收盤價時平倉肭。  
   - 阻止損失：未提及具體止損條件，但策略中默示了風險控制的重要性。  

---

## 四、回測績效  
本次交易策略在XLP指數上的回測結果如下：  

1. **交易筆數**：316次  
2. **平均每筆交易收益**：0.28%  
3. **勝率**：73%  
4. **最大虧損回撤**：-10%  
5. **盈災比（Profit Factor）**：2  

---

## 五、結論與改進建議  
本次交易策略在Consumer Staples指數上表現出一定的盈利能力，勝率和盈災比均令人滿意。然而，平均每筆交易收益略低，可能需要進一步優化入市條件或增加FILTERING機制以提高收益水準。  

---

## 參考資料  
1. 策略代碼與詳細信息可於研究團隊的YouTube頻道、官網或聯絡方式中獲得。  
2. 視頻連結已嵌入描述欄位，歡迎觀看並訂閱以獲取更多內容。
</details>

<details>
<summary>006. The #1 Reason Traders Fail!</summary>

[[Youtube]](https://www.youtube.com/watch?v=3aN9r9vAcq4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：交易策略的重要性與回測必要性

#### 主題
- 本文強調了在金融交易中建立一套具備正向統計期望值（statistical expectancy）且可持續執行的策略的重要性。
- 強調了回測（backtesting）在驗證交易策略有效性和可靠性的必要性。

#### 交易商品
- 文章未指定特定的交易商品，但適用於任何金融市場，包括但不限於股票、外匯、期貨等。

#### 使用指標
- 文章未提及具體的技術指標或分析方法，但強調了將策略量化為明確的規則的重要性。
- 可能涉及統計分析和數據驗證，以確保策略的有效性。

#### 策略細則
1. **交易規則**：
   - 需要制定明確且可執行的交易規則。
   - 每次交易應該基於清晰的_criteria_（例如市場條件、指標信號等）。
2. **紀律性**：
   - 強調了堅持策略的重要性，無論市場環境如何變化。

#### 回測績效
1. **回測目的**：
   - 驗證策略在歷史數據上的表現。
   - 確定策略是否具備正向統計期望值（即長期來看能否盈利）。
2. **回測結果**：
   - 只有通過回測驗證的策略才有可能帶來穩定的盈利能力。

#### 結論
1. **缺乏回測的風險**：
   - 如果不能進行有效的回測，很可能是因為策略本身缺乏明確的規則或盈利的能力。
2. **行動建議**：
   - 投資者應該花時間量化和驗證自己的交易策略。
   - 確保精力投入到具備實際盈利能力的策略中。
3. **總結**：
   - 建立一套可持續執行且經過回測驗證的交易策略是確保盈利的關鍵。
</details>

<details>
<summary>007. No Way These Returns Are True!  | Trading A Few Days a Month</summary>

[[Youtube]](https://www.youtube.com/watch?v=4iAHRyUuW5g&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 重點整理

#### 主題  
本文介紹了一種基於季節性模式的交易策略，該策略專注於每月特定的交易日進行投資，並在過去60年中表現優於「.buy and hold」strateGy。

---

#### 交易商品  
- 標普500指數（S&P 500）

---

#### 策略細則  
1. **買入條件**：每月的第五個交易日進行買入。  
2. **賣出條件**：新月的第三個交易日進行賣出。  
3. **投資時長**：每月僅需7個交易天（買入至賣出期間）。  
4. **市場參與度**：全年約33%時間持有倉位，其餘時間保持現金。  

---

#### 使用指標  
- 本文未提及使用特定技術指標，而是基於季節性模式和交易日規則制定策略。

---

#### 回測績效  
1. **年化回報率**：7%（優於.buy and hold的6.9%）。  
2. **最大虧損**：27%（顯著低於.buy and hold的56%）。  
3. ** equity curve**：整體表現平穩，無明顯波動。  

---

#### 策略改進  
- 通過優化交易規則，將市場參與度降低至23%，年化回報率仍維持在6.7%。  
- 改進版本僅限於付費訂閱會員。  

---

#### 其他亮點  
- 提供多種免費策略，包括五個swing strategies，適用於不同交易時間框架。  
- 網站資源豐富，涵蓋各類最佳交易策略。  

---

#### 結論  
本文展示了一種高效低風險的交易策略，通過短時間市場參與實現了穩定的回報率和較小的虧損幅度。改進版本進一步降低了市場暴露程度，但仍保持不錯的收益水平。作者鼓勵觀眾訂閱頻道以獲取更多免費資源和策略。
</details>

<details>
<summary>008. 2 Inverted Yield Curve Strategies (Rules and backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=573OfvS1foc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 逆收益率曲線交易策略分析

## 主題
本文探討了**逆收益率曲線（Inverted Yield Curve）**作為股票市場指標的有效性，並提出了一種基於逆收益率曲線的交易策略。

## 交易商品
- **債券收益率曲線**：重點關注2年期和10年期國債收益率。
- **股票市場**：分析逆收益率曲線對股市的影響。

## 使用指標
- **收益率曲線（Yield Curve）**：通過比較不同期限債券的收益率，判斷其是否為正常或逆形態。
- **相對強度指數（RSI）**：用於第二個交易策略中的均值回歸分析。

## 策略細則
### 第一策略
1. **買入條件**：當2年期國債收益率高於10年期國債收益率，即收益率曲線 inverted 時買入。
2. **賣出條件**：持有期限為250個交易日後賣出。

### 第二策略
1. **買入條件**：基於收益率曲線的均值回歸特性，結合RSI指標進行判斷。
2. **賣出條件**：未明確提及具體賣出條件，但強調交易次數較少且平均持有時間為3個月。

## 回測績效
### 第一策略
- 1976年至今的回測結果顯示：
  - 平均報酬率為 **7.3%**。
  - 報酬率與典型年度報酬率持平。

### 第二策略
- 1976年至今共產生了102筆交易：
  - 平均報酬率為 **2.5%**。
  - 平均持有時間約為3個月。

## 結論
本文研究結果表明，基於逆收益率曲線的交易策略在歷史回測中表現並不明顯。第一策略的報酬率雖穩定，但與市場平均報酬率相當；第二策略的報酬率略高，但交易次數少且持有時間長。整體來看，逆收益率曲線作為交易指標的效果有限，需進一步研究或結合其他因子以提高策略的有效性。

# 總結
本文分析了逆收益率曲線在股票市場中的應用，提出了兩種基於逆收益率曲線的交易策略，並通過歷史數據進行了回測。結果顯示，雖然這些策略在某些方面具有一定的盈利能力，但整體來看其效果並不顯著。未來的研究可以進一步探討其他影響市場走勢的因素，或將逆收益率曲線與其他指標結合使用，以提升交易策略的有效性。
</details>

<details>
<summary>009. Trading the SANTA CLAUS Christmas Rally (Seasonal Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=60CKmOTmb70&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章整理：聖誕老人行情在黃金市場的表現與策略

## 主題
文章探討了聖誕老人行情（Santa Claus Rally）在股票和黃金市場中的表現，並指出過去20年中黃金價格在此期間的表現遠強於股票。

## 交易商品
- 股票
- 黃金

## 使用指標
- 遊民行情：聖誕老人行情，通常是指歲末年初市場價格上漲現象。
- 期權到期日（Options Expiration Day）

## 策略細則
1. **買入時機**：在12月的期權到期日收盤時買入黃金。
2. **賣出時機**：在新年第一個交易日收盤時.sell 黃金。
3. **持有期間**：從12月底至元旦當天，通常為1-2個交易日。

## 回測績效
- 平均回報率：超過2%每筆交易（自2000年起）。
- 策略穩定性： historical backtesting表明此策略在過去20年中表現一致且 profitable。

## 結論
聖誕老人行情在黃金市場中的表現比股票市場更為顯著，值得投資者關注並作為交易策略之一。文中建議 подписаться на недорогуюWeekly Newsletter для получения дополнительной информации и analysis.

---

此整理結構清晰地展示了文章的核心內容和主要發現，適合用於進一步的分析或報告參考。
</details>

<details>
<summary>010. SECTOR ROTATION strategy  (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=6GfsFt5Wxzw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章要點整理

## 主題  
- 業 sector rotation 管理策略：一種資產類別或多隻 ETF 之間的切換策略。

---

## 交易商品  
- 四隻 ETF：SPY（標普 500）、TLT（20 年期美國公債）、EFA（MSCI 外國大型股指數）、EEM（新興市場ETF）。  

---

## 使用指標  
- 近一個月的績效表現作為排名依據。

---

## 策略細則  
1. 每月月底對四隻 ETF 的過去一個月績效進行排序。  
2. 本月持有表現最佳的 ETF。  
3. 持股一個月後，再根據最新績效重新評估並切換至表現最佳的 ETF。  
4. 重複上述步驟。

---

## 回測績效  
- **整體回測結果**：策略在 2022 年之前表現出色，年度報酬率為 10.1%。  
- **平均收益/交易**：每次交易的平均報酬率為 1.3%。  

---

## 結論  
- 儘管 2022 年市場環境惡劣，此策略仍能實現正報酬並保持穩定績效。  
- 更詳細的內容可參閱 [quantifiedstrategies.com](https://quantifiedstrategies.com) 或點擊文章中的鏈接閱讀更多相關研究。
</details>

<details>
<summary>011. 3 Momentum Trading Strategies (Backtests &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=6NWcKpupjJo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：動量交易策略分析

#### 主題
- 動量交易策略（Momentum Trading Strategies）  
- 分析不同市場條件下動量策略的有效性及應用。

---

### 交易商品
1. 標普500指數（S&P 500）
2. 比特幣（Bitcoin）
3. 四種資產：
   - SPY（標普500ETF）
   - TLT（長期美國公債ETF）
   - EFA（發達市場股票ETF）
   - EEM（新興市場股票ETF）

---

### 使用指標
1. **第一策略**：
   - 100天最高收盤價（100-day high of close）
   - 100天最低收盤價（lowest close in the last hundred days）

2. **第二策略**：
   - 25天最高收盤價（25-day high of close）

3. **第三策略**：
   - 每月價格表現（monthly bars）  
   - 前三個月的動量表現

---

### 策略細則
1. **第一策略**：
   - 買入條件：收盤價突破過去100天最高收盤價。
   - 出場條件：收盤價跌破過去100天最低收盤價。

2. **第二策略**：
   - 買入條件：比特幣創下新高（25-day high of close）。
   - 出場條件：收盤價低於最近高位。

3. **第三策略**：
   - 每月月底評估四種資產過去三個月的表現。
   - 投資表現最佳的.asset，下一月持有該.asset。

---

### 回測績效
1. **第一策略**：
   - 標普500：  
     - 60年回測期，本金10萬美元增長至550萬美元。  
     - 年化報酬率：6.5%（未含股息），約8.5%（含股息）。  
     - 確定率：69%，避開重大下跌。  
     - 最大虧損幅度（Max Drawdown）：<buy and hold策略的50%>。

2. **第二策略**：
   - 比特幣：  
     - 本金10萬美元增長至360萬美元。  
     - 投資時間：<14%>，表現接近Buy and Hold。  
     - drawdown。

3. **第三策略**：
   - 四種資產組合：  
     - 本金10萬美元增長至140萬美元。  
     - 年化報酬率：13.1%。  
     - 最大虧損幅度：<2022年除外，drawdown為34%>。  
     - 獨立於股市的表現。

---

### 結論
1. 動量策略特性：
   - 跟隨市場強勢（Buy Strength）。
   - 適用多種時間框架（每日、週線、月線等）。  
   - 有效避開重大下跌。

2. 應用建議：
   - 策略需具備可持續性，建議在_demo_account_中測試。
   - 可結合其他指標或策略（如 daily pullbacks）以提升效果。  
   - 適用於不同市場條件，但需根據特定資產調整時間框架。

3. 總結：
   - 動量交易是一種有效的投資策略，關鍵在於選擇合適的指標和時間框架，並進行充分的回測。
</details>

<details>
<summary>012. Limit Order Trading Strategy (Rules +Backtest )</summary>

[[Youtube]](https://www.youtube.com/watch?v=7b9dU8tDYtQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章重點整理

## 主題
本文主要探討不同交易訂單類型（市價單與限價單）在交易策略中的效果差異，並展示如何將市價單轉換為限價單的交易策略。文章通過回測實驗，分析兩種訂單類型在具體策略下的表現。

## 交易商品
- **NASDAQ 100**：文中提到的回測是以NASDAQ 100指數為交易對象。

## 使用指標
- **均值回歸（Mean Reversion）**：文中提出並實驗了一種基於均值回歸的基本策略，該策略在市場價格遠離長期平均值時進行買賣操作。

## 策略細則
### 市場價交易策略
1. **入市條件**：當今日收盤價低於昨日收盤價時買進。
2. **退市條件**：未提及明確的	exit condition，但假設為均值回歸信號觸發。

### 限價單交易策略
1. **入市條件**：調整為今日開盤價低於昨日收盤價時買進。
2. **限價價格**：設定買入限價為昨日收盤價，僅在市場PRICE達到或低於此限價時成交。
3. **入市延遲**：買單設定為隔日開盤前生效。

## 回測績效
### 市場價交易策略
- **平均收益/筆**：89%
- **年化收益率**：10.4%
- **投資槓桿**：18%，資金閒置時間較長。
- **交易筆數**：未提及具體數量，但從績效來看交易頻率較高。

### 限價單交易策略
- **平均收益/筆**：1.12%
- **年化收益率**：7.6%
- **交易筆數**：明顯下降，相比市場價交易策略減少超過一半。
- **資金閒置時間**：未提及，但可推測因限價單失敗率較高，資金閒置情況可能有所變化。

## 結論
1. **訂單類型的影響**：
   - 限價單交易策略在平均收益/筆上有所提升，但整體年化收益率下降。
   - 使用市場價訂單能提高交易筆數和整體收益，但可能會增加市場風險。

2. **交易槓桿與資金閒置的考量**：
   - 市場價策略因高槓桿操作帶來較高的回報，但也伴隨著更高的市場參與度。
   - 限價單策略雖然降低了市場參與度，但限制了盈利能力。

3. **未來改進方向**：
   - 文章提出可以進一步優化策略或調整指標，以平衡交易筆數與平均收益。具體建議包括但不限於調整限價 threshold、改變入市條件或結合其他技術指標等。

4. **交易.trade-offs**：
   - 限價單交易策略在提高平均收益/筆的同時，犧牲了整體交易機會，導致年化收益率下降。
   - 市場價交易策略則相反，雖然降低了每筆交易的平均收益，但通過高交易頻率實現整體較高的回報。

## 參考資料
- 文章中未提及具體數據來源或模型細節，僅提供基本的績效數據與策略描述。
</details>

<details>
<summary>013. Williams %R Strategy: (Rules Revealed + Backtest))</summary>

[[Youtube]](https://www.youtube.com/watch?v=7hrpH-b_2es&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
- 探討威廉指標（Williams Percentage R）作為有效的交易策略在股票市場中的應用。  

### 2. 交易商品  
- 標普500指數（S&P 500）。  

### 3. 使用指標  
- **威廉百分比R指標**：  
  - 衡量當前收盤價與最近期內最高價的相對位置，範圍在0到-100之間。  
  - 讀數為0表示價格處於回溯期間的最高點，而讀數為-100則表示處於最低點。  

### 4. 策略細則  
- **交易規則**：  
  - 使用2天的回溯期進行交易。  
  - **進場信號**：當指標低於-90時，建立多頭倉位（long position）。  
  - **出場信號**：  
    1. 當指標高於-30時平倉。  
    2. 或者當收盤價高於前一天的高點時平倉。  

### 5. 回測績效  
- **時間範圍**：1993年至今，共計580筆交易。  
- **年度回報率**：11.5%。  
- **勝率**：僅需22%的時間持倉，其餘時間保持觀望。  
- **最大回撤（Max Drawdown）**：17.7%。  
- **特殊情況表現**：  
  - 2008年金融危機期間，回報率為98.9%。  
  - 2020年新冠疫情時期，回報率為43.3%。  
  - 2022年市場下跌時，仍實現15.7%的回報率。  

### 6. 結論  
- 威廉百分比R策略被證明是一種簡單而有效的交易方法，尤其在應對市場危機時表現突出。  
- 儘管存在一定的回撤風險，但其長期回報率優於「買入並持有」策略。  
- **建議**：投資者應根據具體市場環境和自身風險承受能力，通過充分的回測來確定最佳的參數設置（如回溯期長度、買賣閾值）。
</details>

<details>
<summary>014. 3 ETF Trading Strategies (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=8EmDCJUgnrw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：三種ETF交易策略分析

#### 主題：
本文介紹了三種不同的ETF（交易所交易基金）交易策略，涵蓋了從簡單到較為複雜的方法，並提供每種策略的詳細規則、績效數據及適用性評估。

#### 交易商品：
1. **Turnaround Tuesday**：使用Spy（追蹤標普500指數的ETF）。
2. **Lower Lows and Lower Highs**：主要針對QQQ（納斯達克100指數ETF），但也適用於其他股票和債券ETF。
3. **Momentum Rotation Strategy**：涉及三種ETF：
   - Spy (標普500)
   - GLD (黃金ETF)
   - TLT (美國長期公債ETF)

#### 使用指標：
1. **Turnaround Tuesday**：
   - 基於價格走勢，無具體技術指標。
2. **Lower Lows and Lower Highs**：
   - 連續三日的低點和高點均下降（反映市場弱勢）。
3. **Momentum Rotation Strategy**：
   - 使用3個月和1年期移動平均線來判斷動量方向。

#### 策略細則：
1. **Turnaround Tuesday**：
   - 策略規則：當Spy在某一日收盤價較前一天低，且次の交易日再次下跌時，建議賣出；反之，若Spy在某一日收盤價較前一天高，且次の交易日上漲，則建議買入。
2. **Lower Lows and Lower Highs**：
   - 策略規則：連續三日的低點和高點均下降，表示市場處於下行趨勢，賣出；反之，若連續三日的低點和高點均上升，表示上行趨勢，買入。
3. **Momentum Rotation Strategy**：
   - 策略規則： comparative momentum signals based on 3-month and 1-year moving averages to rotate between the three ETFs.

#### 回測績效：
1. **Turnaround Tuesday**：
   - 長期回測數據未提供，但文章強調其簡單性和可執行性。
2. **Lower Lows and Lower Highs**：
   - 長期回測數據未提供，但文章指出其適用於多種ETF和市場環境。
3. **Momentum Rotation Strategy**：
   - 回測數據未提供，但強調其分散風險和長線持有的優勢。

#### 結論：
1. **主題結論**：本文強調多樣化策略的重要性，建議投資者根據自身Risk tolerance和 торговые.preferences選擇適合的策略。
2. **適用性**：三種策略分別適用於不同市場條件和交易時間框架，Turnaround Tuesday適用於短期交易，Lower Lows and Lower Highs適用於中短期，Momentum Rotation Strategy則適合長線投資。
3. **風險提示**：作者強調所有策略需經過充分的模擬測試，且不應該作為直接的投資建議。

#### 常見問題解答：
1. **最佳ETF交易策略**：不存在「最佳」策略，多樣化是關鍵。
2. **能否進行Swing Trade ETFs**：可以，本文提供具體示例。
3. **ETF交易的優缺點**：
   - 優點：分散風險、降低個股大幅波動的影響。
   - 缺點：相對收益有限，除非長期持有。
4. **是否適合初學者**：適合，但建議先在模擬帳戶中測試至少一年。
5. **最佳交易時間框架**：推薦使用每日、週ly或月度時間框架。

本文最後呼籲觀眾蔊看更多內容，並鼓勵留言交流。
</details>

<details>
<summary>015. Fabian Timing Model Strategy (Trading Rules &amp; Backtest) #shorts</summary>

[[Youtube]](https://www.youtube.com/watch?v=8gH33k5W334&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 小節歸納

#### 1. 主題
- **Fabian Timing Model Strategy**:  
   本文介紹了一種名為Fabian Timing Model的量化趨勢跟隨策略，由Richard Fabian於20世紀60年代中期開發。該策略基於數學規則，用於幫助投資者在市場中捕捉長期趨勢。

#### 2. 交易商品
- **主要指標**：  
   - 標普500（S&P 500）  
   - 道瓊工業平均指數（Dow Jones Industrial Average）  
   - 公用事業板塊  
- **交易工具**：  
   - 使用SPY ETF來跟蹤標普500的表現。

#### 3. 使用指標
- **主要指標**：  
   - 各指數的39周移動平均線（39-week moving average）。  
   - 用於判斷市場趨勢的方向。

#### 4. 策略細則
- **買入條件**：  
   - 標普500、道瓊工業平均指數和公用事業板塊均位於其各自的39周移動平均線之上。  
   - 發出買入信號，建議投資者購買標普500。
- **賣出條件**：  
   - 若上述三個市場中有兩個或更多位於其各自的39周移動平均線之下。  
   - 發出賣出信號，建議投資者出售標普500。

#### 5. 回測績效
- **回測時間段**：  
   - 從2000年開始進行回測。
- **績效指標**：  
   - 年化報酬率：7%（相對於持有策略的5%）。  
   - 投資參與度：僅56%。  
   - 備註：此為長期.Strategy，不適合短期交易。

#### 6. 結論
- **主要結論**：  
   - Fabian Timing Model被證實在長期內具有盈利能力。  
   - 該策略能夠幫助投資者提升報酬率。  
   - 需要時間和耐心才能看到收益，不適合追求短期利益的投資者。

---

### 具體的投資建議

1. **適合的人群**：  
   - 長期投資者：Fabian Timing Model是一種長線策略，適合能夠耐得住寂寞、持股待漲的投資者。  
   - 偏好量化分析的投資者：該策略基於數學規則和移動平均線指標，適合喜歡客觀化交易信號的投資者。

2. **操作建議**：  
   - **跟蹤市場趨勢**：定期查看標普500、道瓊工業平均指數和公用事業板塊的39周移動平均線，以判斷買賣時機。  
   - **分散投資**：雖然策略主要關注標普500，但可以考慮將其他指數或板塊納入觀察範圍，以進一步多元化風險。

3. **注意事項**：  
   - **成本考量**：使用ETF（如SPY）跟蹤標普500時，需注意交易成本和稅務影響。  
   - **市場劇烈波動**：在市場大幅震盪期間，移動平均線可能會發出錯誤信號，需謹慎對待。

4. **進一步研究**：  
   - 研究該策略在不同市場周期下的表現，特別是在股災或牛市中的適用性。  
   - 考慮將策略與其他量化模型結合，以提高交易勝率。

5. **心理準備**：  
   - 長期策略需要耐心和紀律，避免因短期市場波動而輕易改變投資計劃。
</details>

<details>
<summary>016. Value Investing vs Growth Investing Rotating Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=9UlOnc-3Uck&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 本文重點整理

#### 主題
本篇文章探討了價值投資（Value Investing）與成長股投資（Growth Investing）兩種常見的投資策略，介紹了一種基於這兩種資產類別之間波動的旋轉交易策略，並指出此策略在歷史回測中表現優於傳統的「買進並持有」策略。

#### 交易商品
- **價值股票 ETF**：USV（Value Stock ETF）
- **成長股 ETF**：IUSG（Growth Stock ETF）

#### 使用指標
- **動量指標**：基於 USV 和 IUSG 的價格走勢，計算二者的比率。
- **移動平均線**：使用 10 日和 40 日移動平均線來判斷短期動態。

#### 策略細則
1. **策略核心**：
   - 根據價值股與成長股之間的相對表現，進行資產配置的調整。
   - 計算 USG 和 USV 的比率（IUSG/USV），並觀察其 10 日和 40 日移動平均線的交叉情況。
   
2. **交易規則**：
   - 當價值股表現超越成長股時，賣出成長股 ETF（IUSG），買進價值股 ETF（USV）。
   - 當成長股表現超越價值股時，賣出價值股 ETF（USV），買進成長股 ETF（IUSG）。

3. **執行機制**：
   - 基於短期動量（10 日移動平均線）與中期趨勢（40 日移動平均線）的交叉點來實施交易。
   - 策略強調市場 timing，根據相對表現動態調整投資組合。

#### 回測績效
- **年化回報率**：
  - 旋轉策略：9%
  - 最佳個股表現（價值股 ETF）：7.4%
  
- **風險指標**：
  - 成功降低價格波動性，即「風險」。
  - 策略在控制風險的前提下，實現了優於傳統.buy and hold 的回報。

#### 結論
1. **策略有效性**：
   - 旋轉策略在歷史數據中表現 superior，尤其是年化回報率和風險控制方面。
   
2. **批評與反辯**：
   - 部分投資者質疑市場 timing 的難度，認為「買進並持有」或多元化投資組合更為 practical。
   - 策略支持者則強調其在特定市場環境下的優越性。

3. **未來展望**：
   - 文章最後提及即將探討的三種指數策略，暗示旋轉交易策略可進一步優化或與其他策略結合使用。
</details>

<details>
<summary>017. Currency Trading Strategies - &quot;From Carry Trades to Curve Trades&quot;</summary>

[[Youtube]](https://www.youtube.com/watch?v=9ZuBES1XZ4k&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 研究報告名稱：《From Carry Trades to Curvy Trades》  
- 作者：Ferdinand Dre, Johan Grob 和 Thomas Kasa  
- 主旨：介紹一種名為「Curvy Trades」的新興貨幣交易策略，與傳統的「Carry Trades」策略相比，Curvy Trades 利用收益率曲線信息（特別是 Nelson-Siegel 因子）來提升風險-adjusted returns。

#### 交易商品  
- 貪婪交易：依賴短期利率差異。  
- Curvy Trades：基於相對曲率因子（Relative Curvature Factor），該因子來自Nelson-Siegel模型，用以總結收益率曲線的特徵。  

#### 使用指標  
- **Curvature Factor**: 由Nelson-Siegel模型衍生出來，用於衡量收益率曲線的曲率。  
- **Nelson-Siegel Factors**: 包含水平（Level）、斜率（Slope）和曲率（Curvature），用於總結不同期限的利率信息。  

#### 策略細則  
1. Curvy Trades策略基於相對曲率因子，而非傳統的短期利差。  
2. 交易.currency選擇不再依賴典型的carry貨幣（如日圓和瑞士法郎）。  
3. 曲線因子用於預測未來短期利率走勢，進而影響匯率。  

#### 回測績效  
1. Curvy Trades具有更高的夏普比率（Sharpe Ratio），表示風險調整後的報酬更為優異。  
2. 預期收益的偏態（Skewness）較低，意味著結果更一致且波動性較小。  
3. 相對於傳統Carry Trades，Curvy Trades受市場逆轉的影響較小，降低崩盤風險。  

#### 結論  
1. Curvy Trades策略在回測中表現優於傳統Carry Trades。  
2. 曲率因子提供了一種新的資產定價框架，能夠更好地解釋貨幣匯率的變動。  
3. 這些發現為量化金融和貨幣交易開啟了新可能性，特別是在風險管理和報酬 optimization 方面。  

---

### 英文原文段落引用

#### 主題  
- *"The research paper titled 'From Carry Trades to Curvy Trades' authored by Ferdinand Dre, Johan Grob and Thomas Kasa introduces a novel approach to currency trading strategies called curvy trades."*  

#### 交易商品  
- *"Unlike traditional carry trade strategies that rely solely on differences in short-term interest rates, curvy trades incorporate additional information from yield curves, specifically the Nelson-Siegel factors."*  

#### 使用指標  
- *"The study's findings are interesting: curvy trades yield higher Sharpe ratios, meaning better risk-adjusted returns and exhibit a smaller return skewness compared to traditional carry trade strategies."*  

#### 策略細則  
- *"Curvy trades build less upon typical carry currencies like the Japanese Yen and the Swiss Franc, making them less susceptible to crash risk."*  

#### 回測績效  
- *"Moreover, curvy trades build less upon typical carry currencies like the Japanese Yen and the Swiss Franc, making them less susceptible to crash risk. This is a significant advantage as traditional carry trades can be vulnerable to sudden market reversals."*  

#### 結論  
- *"In conclusion, the research paper 'From Carry Trades to Curvy Trades' introduces a paradigm shift in currency trading strategies by leveraging yield curve information. Curvy trades offer higher risk-adjusted returns, reduced return skewness, and lower susceptibility to crash risk. As investors seek innovative approaches to navigate the ever-changing financial markets, this research could pave the way for a new era in currency trading."*
</details>

<details>
<summary>018. 3 MACD Trading Strategies 2024 (Backtested With Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=9h46J1xanfk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理與結構化總結報告

---

#### **主題**
本文主要探討三個基於MACD指標的交易策略，涵蓋了策略細則、回測績效及其適用性分析。最終目的是幫助交易者了解如何有效利用MACD指標進行交易。

---

#### **交易商品**
- 標普500指數（S&P 500）
- 標普500 ETF（ ticker code: S）

---

#### **使用指標**
- MACD（移動平均收斂散度指標）
- Bollinger Bands（布林帶）
- RSI（相對強弱指數）

---

#### **策略細則**
##### 1. 基於MACD Histogram的均值回歸策略
- **進場條件**：當MACD直方圖連續四天向下移動，且四天前水準低於零。
- **離場條件**：未提及，但強調其為均值回歸策略。
- **特性**：
  - 投資時間較短（5%）。
  - 截斷率高（勝率89%）。
  - 最大虧損幅度16%。

##### 2. 基於MACD Histogram與Bollinger Bands的策略
- **進場條件**：當MACD直方圖跌破布林帶下限。
- **離場條件**：當MACD直方圖突破布林帶上限。
- **特性**：
  - 投資時間較長（64%）。
  - 年報酬率8.4%。
  - 最大虧損幅度44%。

##### 3. 維 secrecy 營銷策略
- **進場與離場條件**：未公開，但涉及RSI指標。
- **特性**：
  - 投資時間短（21%）。
  - 年報酬率高（接近Buy and Hold表現）。
  - 最大虧損幅度15%。
  - 風險調整後回報率43%。

---

#### **回測績效**
##### 1. 基於MACD Histogram的策略
- 投資金額：$100,000。
- 終值：未提及。
- 年報酬率：未提及，但強調勝率高（89%）。
- 最大虧損幅度：16%。

##### 2. 基於MACD Histogram與Bollinger Bands的策略
- 投資金額：$100,000。
- 終值：$1,150,000。
- 年報酬率：8.4%。
- 最大虧損幅度：44%。

##### 3. 維 secrecy 營銷策略
- 投資金額：$100,000。
- 終值：$1,500,000。
- 年報酬率：接近Buy and Hold表現。
- 最大虧損幅度：15%。
- 交易次數：未提及。

---

#### **結論**
##### 1. MACD指標的有效性
- MACD指標在均值回歸策略中表現良好，勝率高且虧損幅度可控。
- 結合Bollinger Bands可以提高收益，但最大虧損幅度較大。
- RSI指標的加入進一步提升了策略績效。

##### 2. 時間框架與交易類型
- MACD在日線或周線時間框架下表現最佳。
- 適宜於波動性交易（Swing Trading），而非日內交易。

##### 3. 策略改進空間
- 加入其他指標（如RSI）可提升績效，但需避免過度擬合。
- 適當的超參數設定（如短時間框架）能提高策略效果。

##### 4. 局限性
- 沒有 guarantees 策略未來表現將持續優異。
- 投資者需根據自身風險承受能力選擇合適的策略。

---

#### **結構化總結報告**

**1. 主題**
本文探討了三個基於MACD指標的交易策略，分析其細則、回測績效及適用性。

**2. 交易商品**
- 標普500指數（S&P 500）。
- 標普500 ETF（ticker code: S）。

**3. 使用指標**
- MACD。
- Bollinger Bands。
- RSI。

**4. 策略細則**
- **策略1**：基於MACD Histogram的均值回歸策略，連續四天向下移動且低於零進場。
- **策略2**：基於MACD_histogram與Bollinger Bands，跌破下限進場，突破上限離場。
- **策略3**：未公開，但涉及RSI指標。

**5. 回測績效**
- 策略1：勝率89%，虧損幅度16%。
- 策略2：年報酬率8.4%，虧損幅度44%。
- 策略3：終值$1,500,000，年報酬率接近Buy and Hold，虧損幅度15%。

**6. 結論**
- MACD在均值回歸策略中表現優異。
- 結合其他指標（如RSI）可提升績效。
- 適宜於波動性交易，需避免過度擬合。
</details>

<details>
<summary>019. Multiple Days Up (MDU) And Multiple Days Down (MDD). - Larry Connors</summary>

[[Youtube]](https://www.youtube.com/watch?v=9j20XPfOcgQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
此篇文章介紹了Laurence Connor著作《High Probability Trading》第六章中的一種交易策略，名為「Multiple Days Up and Multiple Days Down」。文章詳細解讀了該策略的操作方式、規則以及回測結果。

---

#### 交易商品  
- 操作對象：股票市場ETF（Exchange-Traded Funds），文中提到下載了20隻不同股票市場ETF的報價進行回測。
- 策略後期改為專注於spy和QQQ這兩隻ETF，並分配50%的資金至每筆交易。

---

#### 使用指標  
- 指標名稱：未明確提及具體指標名稱，但文中描述了一個.swinging indicator（震盪指標），用來判斷買賣時機。
- 指標特性：
  - 指標從低到高波動。
  - 高數值表示近期多為下跌日，此時為買進信號。

---

#### 策略細則  
1. **買進條件**：  
   - ETF在最近的5個交易日內至少有4個交易日下跌（即「四跌一漲」）。  
2. **賣出條件**：  
   - ETF價格收盤突破五天移動平均線。  
3. **其他規則**：  
   - 未設置止損（No Stop Loss）。  
   - 買入時點：當上述條件之一成立時，於收盤價進場。  

---

#### 回測績效  
1. **初步回測**：  
   - 對20隻ETF從2000年至今進行回測，結果顯示收益變化很大，表現不一。  
2. **組合策略回測**：  
   - 建立投資組合，將資金平均分配至每筆交易（每筆佔20%，最多同時持有5隻ETF）。  
   - 結果：年化收益率低，且市場參與度（holding time）較低。  
3. **策略優化後回測**：  
   - 專注於spy和QQQ兩隻ETF，並分配50%資金至每筆交易。  
   - 仍舊未見顯著的收益提升，績效不穩定， equity curve波動大。

---

#### 結論  
- 文章認為此策略整體表現不佳，回測結果並不可觀。  
- 提醒讀者作者另有數百種免費策略可供參考，鼓勵網友前往網站查看更多內容。  

---

### 英文原文  
[已提供於文章開始部分]
</details>

<details>
<summary>020. Money Flow Index Strategy | MFI Trading Indicator (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=9qmYEqzA7HI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：Money Flow Index (MFI) 交易策略

#### 主題
- **錢流指數（MFI）**：介紹了一種基於資金流動的簡單交易策略，並探討其在金融市場中的應用。

#### 交易商品
- **標普500指數（S&P 500）** 和其他股票市場指標。
- 適用於任何金融資產，但需根據具體資產特性調整設定。

#### 使用指標
- **錢流指數（MFI）**：衡量資金流入和流出的動量指標，結合價格和成交量數據，範圍在0到100之間。
- 提供超買超賣條件 signals 和潛在價格反轉的預測。

#### 策略細則
1. **信號條件**：
   - 若2日MFI低於10，買入（close position）。
   - 若價格收高於昨日最高價，賣出（close position）。
   
2. **時間限制**：
   - 交易持有期為最多10個交易日。

3. **最佳設定**：
   - 經回測驗證，短時間窗口（如2日）效果最佳。

#### 回測績效
- **起始資金**：1993年開始，10萬美元。
- **最終資產**：超過200萬美金，年複利報酬率為10.5%。
- **買持比率**：僅35%的時間處於投資狀態。

#### 結論
- MFI策略簡單有效，適合新手交易者。
- 相較於持有策略（年報酬率9.7%），MFI策略表現更佳。
- MFI雖有局限性（如假信號、敏感性），但通過適當的資金管理和風險控制可提高成功率。

---

### 英文原文段落截取與翻譯

#### 定義MFI
- **"The money flow index (mfi) is a momentum indicator that measures the flow of money into and out of a security by combining price and volume data."**
  - 翻譯：錢流指數（MFI）是一種動量指標，通過結合價格和成交量數據來衡量資金流入和流出的情況。

#### 策略細則
- **"If the two-day mfi is below 10 we buy at the close we sell at the close when the close ends higher than yesterday's high."**
  - 翻譯：如果2日MFI低於10，我們在當收盤時買入；若收盤價高於昨日最高價，則在當收盤時賣出。

#### 回測績效
- **"Starting with $100,000 in 1993 and ending up with over $200,000, that's a compounded annual return of 10.5%."**
  - 翻譯：從1993年的10萬美元開始，最終資產超過200萬美元，年複利報酬率為10.5%。

---

### 英文總結
The article introduces the Money Flow Index (MFI) as a simple yet effective trading strategy for financial markets. By combining price and volume data, MFI measures資金流入和流出, providing signals for overbought or oversold conditions. A two-day MFI below 10 triggers a buy signal, while a close higher than the previous day's high triggers a sell signal. Backtesting shows strong performance with a compounded annual return of 10.5% and a holding period of only 35%. Despite limitations like false signals, the strategy is deemed suitable for novice traders due to its simplicity and objective nature.

---

This structured summary captures the essence of the article, highlighting key themes, strategies, and conclusions related to the MFI trading approach.
</details>

<details>
<summary>021. Trade the High - Short Interest Indicator (Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=A6WIwn58sd4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### Summary of Key Points from the Article  

#### **Theme**  
The article examines the relationship between short interest and stock performance, particularly focusing on whether high short interest is beneficial or detrimental to investors. It also explores which type of stocks—those with high or low short interest—tend to perform better over time.

---

#### **Trading Instrument**  
- Stocks (equities)  
- Short selling strategies  

---

#### **Key Indicators**  
1. **Short Interest**:  
   - Defined as the percentage of a company's outstanding shares that have been sold short.  
   - Example: If a company has 1 billion shares outstanding and 50 million are shorted, the short interest is 5%.  
2. **Short Interest Ratio (SIR)**:  
   - Measures the average number of days it takes for short sellers to close their positions.  
   - Calculated as the total shorted shares divided by the daily trading volume of the stock.  

---

#### **Strategy Details**  
1. High Short Interest:  
   - Stocks with high short interest (e.g., 20%) are often considered "over短" and may indicate strong conviction among short sellers.  
2. Low Short Interest:  
   - Stocks with low short interest (e.g., less than 2% in the lowest deciles) suggest limited short selling activity, which could be a sign of weaker conviction among bears.  

---

#### **Backtesting Performance**  
1. High Short Interest Stocks:  
   - Historically, stocks with high short interest have shown weak returns over one year.  
   - The highest short interest deciles (top 20%) have demonstrated the weakest performance.  
2. Low Short Interest Stocks:  
   - Companies with low short interest outperform the average stock in terms of returns.  

---

#### **Conclusion**  
1. **High Short Interest**:  
   - Generally associated with weak future returns, suggesting it is not a reliable indicator for identifying "multi-baggers" (stocks that increase significantly in value).  
   - The GameStop short squeeze in 2021 was an outlier and not representative of typical market behavior.  

2. **Low Short Interest**:  
   - Tend to outperform stocks with high short interest, making them a more promising target for investors seeking strong returns.  

3. **Cautionary Note**:  
   - Investors should avoid relying on anecdotal data or isolated events (e.g., short squeezes) when assessing the potential of a stock.  
   - High short interest does not guarantee future profitability and is unlikely to be a reliable indicator for identifying the next big winner.  

---

#### **Final Thoughts**  
The article emphasizes the importance of using long-term, systematic analysis rather than relying on short-term trends or isolated events. It suggests that investors should focus on stocks with low short interest when seeking opportunities for strong returns.
</details>

<details>
<summary>022. Gold Overnight Trading Strategy – Make Money While Sleeping</summary>

[[Youtube]](https://www.youtube.com/watch?v=AofDVmSjQjY&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 重點整理

#### 主題  
- 描述一種利用黃金及其礦業股在隔夜市場（從收盤到次日開盤）進行交易的策略。
- 強調該策略具有穩定的正收益潛力。

#### 交易商品  
- GDX：跟蹤黃金礦商的ETF。
- GLD：跟蹤黃金價格的ETF。

#### 策略細節  
1. **時間框架**  
   - 交易時段為從收盤到次日開盤（overnight trading）。  
   - 相反，日內交易（買入當日開盤價，賣出當日收盤價）通常會導致虧損。  

2. **策略優化**  
   - 單獨的隔夜趨勢收益不足以構成可交易策略。  
   - 通過添加一到兩個其他變量（具體未明確說明），可以顯著提升策略的有效性。  
   - 示例：針對GLD開發的一種黃金隔夜交易策略，回測結果顯示其在過去近二十年內表現出持續穩定的上升趨勢。  

#### 回測績效  
- **GDX的表現**：  
  - 隔夜收益穩定且呈上升趨勢。  
  - 相比之下，日間交易（從開盤到收盤）通常導致虧損。  

- **GLD的表現**：  
  - 隔夜收益略高於持有成本（Buy and Hold）。  
  - 日間交易的回報率略微為負，因此需要結合其他變量來提高策略的有效性。  

#### 結論  
- 單獨的隔夜交易策略可能不足以盈利，但通過引入額外的指標或變量，可以開發出長期穩定的盈利能力策略。  
- 提供訂閱服務（課程、網站資源等），有興趣者可進一步了解和使用這些策略。
</details>

<details>
<summary>023. Testing A Random Entry Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=CDw5HhC9Lc8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 小節一：主題  
- 文章介紹了一種基於隨機選取交易機會的工作交易策略（Random Work Strategy）。  

### 小節二：交易商品  
- 未提及特定交易商品，但不限定於任何市場或金融工具。  

### 小節三：使用指標  
- 策略基於完全隨機選擇的交易機會，未涉及具體技術指標或分析方法。  

### 小節四：策略細則  
1. 每年進行12次交易。
2. 交易機會完全隨機選取。
3. 每筆交易設置4個交易日的退出時間限制。

### 小節五：回測績效  
1. **權益曲線（Equity Curve）**：展示了策略的整體表現。
2. **最大回撤（Max Drawdown）**：約為12%，表現尚可。
3. **平均交易收益（Average Gain per Trade）**：約為0.37。
4. **盈利能力質因子（Profit Factor）**：約為1.7。

### 小節六：結論  
- 結果表明，即使基於完全隨機的策略，也可以獲得不錯的交易績效。
</details>

<details>
<summary>024. What Happens To Stocks When Bonds Go Down?</summary>

[[Youtube]](https://www.youtube.com/watch?v=Dw1pit-dC8Y&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：股票與債券市場的互動關係及交易策略

#### 1. 主題：
本文探討了債券市場走弱對股市的影響，提出了一種基於股債之間相互作用的回測交易策略。

#### 2. 財務理論與股債互動：
- 利率是決定股票價值的核心因素。
- 高利率抑制風險性資產（如股票）的需求，除非提供足夠的報酬。
- 低利率環境下，持有風險性資產（股票、黃金、比特幣等）更具吸引力。

#### 3. 債券特性與市場價格：
- 債券票息固定，但市場價格受利率波動影響。
- 利率下降時，債券價格被推高；反之亦然。
- 債券的信用風險低於股票，債權持有人在破產情況下優先受償。

#### 4. 策略假說：
- 假設債市下跌（即利率上升）對股市不利。
- 策略：當債券ETF（TLT）跌破其移動平均線時買進股票ETF（SPY），反之賣出。

#### 5. 使用指標與交易商品：
- 移動平均線（MA）用於研判市場趨勢。
- SPY（追蹤S&P500指數的ETF）為主要交易工具。
- TLT（美國20年期公債ETF）作為指標。

#### 6. 策略細則：
- 使用15日移動平均線作為買賣信號。
- 規則：
  - TLT跌破15日MA：買進SPY並持有至收盤。
  - TLT上穿15日MA：賣出SPY，離場直至下次信號。

#### 7. 回測與績效分析：
- 回測涵蓋2003年至影片發布期間的數據。
- 策略績效：
  - 平均年化報酬率：<1%，遠低於SPY的9.8%。
  - 交易次數：355次，平均每筆交易收益0.86%。
  - 最大虧損：50%。

#### 8. 結論：
- 策略在債市下跌期間難以賺錢。
- 反向信號（即債市上漲時）的績效更佳，將於下一集影片中探討。
</details>

<details>
<summary>025. Sell The Rip Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=EHj846zWHLY&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：.sell The Rip 設定交易策略之研究

#### 主題  
本文探討了**Mean Reversion**交易策略的改進，特別是針對**Sell The Rip**信號的優化，旨在提升交易績效並降低最大回撤（Drawdown）。文章通過實證分析，展示了優化後的策略在股票市場中的表現，並討論其在不同資產類別中的適用性。

#### 交易商品  
- **主要研究對象**：標準普爾500指數（S&P 500）  
- **不適用的市場**：大宗商品與外匯市場  

#### 使用指標  
1. **原始策略**：3日相對強度指數（RSI）  
   - 當3日RSI低於30時，建立多頭倉位；當RSI達到70時賣出。  
2. **優化後的信號**：改進的Sell The Rip信號  
   - 賣出條件：收盤價高於昨日最高價，表明價格已超漲至可能被高估的水平。

#### 策略細則  
1. **原始策略細節**：
   - 入場信號：3日RSI < 30。
   - 出場信號：3日RSI > 70。  

2. **優化後策略細節**：
   - 新增賣出條件：收盤價 > 昨日最高價。
   - 目標：更精準地捕捉超漲時機，減少持有時間並提高收益。

#### 回測績效  
1. **原始策略績效（1993年至今）**：
   - 總交易次數：391次。
   - 平均每筆交易回報率：61%。
   - 最大回撤：35%，發生兩次。  

2. **優化後策略績效**：
   - 回撤改善顯著，最大回撤不超過20%，僅出現兩次超過20%的情況。
   - 年化回報接近「買入並持有」策略的水平，但持倉時間大幅減少（僅27%的時間）。

#### 結論  
1. **主要發現**：
   - 優化後的Sell The Rip信號顯著提升了交易策略的表現，特別是在降低回撤方面。  
   - 該策略在股票市場中表現優異，但在趨勢性較強的市場（如大宗商品和外匯）中可能效果不佳。  

2. **建議**：
   - 對於不同市場，需通過回測確定最佳的交易策略與信號。  
   - 投資者應根據自身風險承受能力和市場特性選擇適合的策略。

3. **局限性**：  
   - 該策略在趨勢性較強的市場中可能表現不佳，存在賣早的風險。
</details>

<details>
<summary>026. CANDLESTICKS Patterns Trading Strategies - Which One Is Best?</summary>

[[Youtube]](https://www.youtube.com/watch?v=G6kvcga6zPQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 主題  
- 探討 Candlestick（蠟燭圖）在金融市場中的有效性及其盈利能力。  

---

### 交易商品  
- 研究對象為標準普爾500指數（S&P 500）。  

---

### 使用指標  
- **Candlestick 模式**：通過分析過去30年內的至少50筆交易，對75種Candlestick模式進行了系統性研究。  

---

### 策略細則  
1. **定量方法**：  
   - 將所有Candlestick模式量化，並進行回測以評估其績效。  
2. **篩選標準**：  
   - 僅選擇在過去30年中有至少50筆交易的模式，並根據「利潤因子」（Profit Factor）對其進行排名。  
3. **代碼實現**：  
   - 提供易於測試的AmiBroker和Tradestation代碼，方便用戶實時交易Candlestick模式。  

---

### 回測績效  
1. **總體表現**：  
   - 使用10種最佳的Candlestick模式對S&P 500進行回測，結果顯示其收益率為20倍（即20 bagger），優於「買入並持有」策略約1個百分點。  
2. **時間效率**：  
   - 實現上述收益僅需投入28%的時間。  
3. **風險控制**：  
   - 最大回撤小於15%，而同期S&P 500的最大回撤為55%。  

---

### 結論  
- **有效性驗證**：Candlestick模式在長期回測中表現優異，尤其是在熊市或下跌市場中提供無相關性的收益（如2008年股市暴跌期間，Candlestick模式仍實現23.7%的收益率）。  
- **策略優勢**：與傳統的「買入並持有」策略相比，Candlestick模式具有更高的風險調整後收益和較低的最大回撤。  

---

### 建議與提供  
- 提供一份有償研究報告，包含所有75種Candlestick模式的詳細邏輯、交易結果及代碼支持。  

---

此研究為金融市場提供了基於實證的Candlestick模式分析，具有較高的參考價值。
</details>

<details>
<summary>027. Last Day Of The Month Trading Strategy - Ultimo Effect (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=H7asjNMQ0OU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題
- 本文介紹了一種古老且高效的交易策略，稱為「月轉策略」（Turn of the Month Strategy），並解釋了如何利用月末效應（End-of-the-Month Effect）來提高交易績效。

### 2. 交易商品
- 操作標的：S&P 500指數。
- 適用市場：股票市場。

### 3. 使用指標
- 主要基於季節性模式（Seasonal Pattern），特別是月末效應，即每月月底股票價格往往會出現上漲現象。

### 4. 策略細則
1. **進場時間**：
   - 購入時機：每月第5個交易日的收盤價。
2. **出場時間**：
   - 出脫時機：次月第3個交易日的收盤價。
3. **操作方式**：
   - 每月操作時間約7天（從每月第5個交易日至次月第3個交易日）。
4. **策略優勢**：
   - 相對於「買進並持有」策略，操作時間更短，但年化報酬率更高（7.1% vs. 6.9%）。
   - 降幅度較小（-27% vs. -56%）。

### 5. 回測績效
1. **報酬率**：
   - 年化報酬率：7.1%。
   - 對比「買進並持有」策略，年化報酬率為6.9%。
2. **最大_DrawDow**：
   - 月轉策略：-27%。
   - 「.buy and Hold」策略：-56%。

### 6. 結論
1. **策略有效性**：
   - 月轉策略在歷史回測中表現優於「買進並持有」策略，尤其是在報酬率和風險控制方面。
2. **實用性**：
   - 操作時間短，僅需7天/月，可讓交易者有更多時間從事其他活動。
3. **改進空間**：
   - 作者建議交易者根據自身經驗進一步優化策略，以追求更好的回報。

### 7. 其他
1. **月末效應的來源**：
   - 與工資支付、會計記錄彌平、企業資金流入儲蓄等季節性現象有關。
2. **適用性**：
   - 雖然此策略在S&P 500上表現良好，但需進一步研究其在其他市場或指標上的效果。
</details>

<details>
<summary>028. Turnaround Tuesday Trading Strategy (Trading Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=HClGJJgzv4U&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章要點整理

## 主題  
本文探討了「轉折點星期二交易策略」（Turnaround Tuesday Strategy），並通過回測分析其績效，與「買進後持有」策略進行比較。

---

## 交易商品  
- 指標：SPY（追蹤標普500指數的ETF）

---

## 策略細則  
1. **交易規則**：  
   - 如果今天是星期一且收盤價低於上周五，則在當日收盤時買入。  
   - 退出信號為：  
     - 收盤價高於昨日最高價（Qs.sell）。  
     - 或者，持有最多5個交易日後賣出。

2. **操作時間**：  
   - 與「買進後持有」策略相比，此策略投資時間更短，僅約24%的時間蔊市，其餘時間可投入現金於其他策略。

---

## 回測績效  
1. **年化回報率**：  
   - 轉折點星期二策略：9.8%。  
   - 買進後持有策略：10.6%。  

2. **最大虧損**：  
   - 転折點星期二策略：短期最大虧損24%，但恢復迅速，其他虧損幅度通常為個位數。  
   - 買進後持有策略：歷史最大虧損55%（1993年買入至當前）。  

3. **風險調整後績效**：  
   - 轉折點星期二策略的虧損期間較短，且回測結果顯示其績效相對穩定。  

---

## 結論  
- 轉折點星期二策略在歷史數據中表現出色，尤其在短期收益和風險控制方面優於「買進後持有」策略。  
- 改進版本（供付費訂閱者使用）進一步提升了績效和 metrics。  
- 本文強調交易者應根據個人財務目標進行獨立研究，並建議探索更多策略以分散投資組合。  

---

## 其他注意事項  
- 文章提醒觀眾此內容不構成投資建議，需自行評估風險與可行性。
</details>

<details>
<summary>029. Bullish Reversal Trading Strategy – (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=IF7-Ne2BV5k&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 本文重點整理

#### 主題  
本文主要探討金融市場中「反轉日（Reversal Day）」策略的有效性，包括牛市和熊市兩種情境下的策略細則及回測績效。

---

#### 交易商品  
- **黃金ETF（Gold GLD）**：用於示範和回測反轉日策略。

---

#### 使用指標  
1. **相對強弱指數（RSI）**  
   - **牛市反轉日**：五天RSI低於35，表示超賣。
   - **熊市反轉日**：五天RSI高於65，表示超買。

2. **價格走勢**  
   - **牛市反轉日**：今日最低價低於昨日最低價，今日收盤價高於昨日收盤價。
   - **熊市反轉日**：今日最高價高於昨日最高價，今日收盤價低於昨日收盤價。

---

#### 策略細則  
1. **牛市反轉日策略**  
   - 信號條件：  
     - 今日最低價 < 昨日最低價。  
     - 今日收盤價 > 昨日收盤價。  
     - RSI(5) < 35。  
   - 進場點位：價格突破昨日高點。  
   - 出場條件：持有五天後退出，或使用平臺Optimizer函數設定.Exit。

2. **熊市反轉日策略**  
   - 信號條件：  
     - 今日最高價 > 昨日最高價。  
     - 今日收盤價 < 昨日收盤價。  
     - RSI(5) > 65。  
   - 進場點位：價格跌破昨日低點。  
   - 出場條件：持有五天後退出，或使用平臺Optimizer函數設定.Exit。

---

#### 回測績效  
1. **牛市反轉日**  
   - 平均最大回撤（Max Drawdown）：-0.94%。  
   - 最佳出場天數：24天，平均收益為2.02%。  
   - 利益因數（Profit Factor）：整體表現良好，交易次數較少。

2. **熊市反轉日**  
   - 平均最大回撤（Max Drawdown）：-1.32%。  
   - 獲利能力較牛市反轉日顯著降低。  
   - 利益因數（Profit Factor）：整體表現尚可，但交易次數有限。

---

#### 結論  
1. ** bullish reversal day**策略在黃金市場中表現較為穩定且具備盈利能力。  
2. **bearish reversal day**策略在黃金市場中的效果不如牛市反轉日，可能與黃金的長期上漲趨勢有關。  
3. 本文最後提及訂閱者可獲得更多策略和資源，包括課程和網站內容。

---

以上整理為正式的學術用語，並以小節方式分類，旨在清晰地展示文章的核心內容和結論。
</details>

<details>
<summary>030. VOLATILITY Trading Strategy - ATR Bands (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=LXVwz2KE6O8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理與分析

#### 主題  
本文介紹了一種已運行近10年的波動性策略（Volatility Strategy），並展示了其在不同金融指數上的表現。策略的核心是在寬泛的ETF和期貨合約上操作，特別是NASDAQ 100指數。

---

#### 交易商品  
- **主要交易商品**：NASDAQ 100指數（ Nasdaq-100 ETF 或 futures）  
- **其他適用商品**：S&P 500 ETF、Consumer Staples ETF (XLP) 等。  

---

#### 使用指標與策略細則  
1. **波動性規則**：作為主要交易規則之一，用於決定入市時機。  
2. **價格行為規則**：基於市場價格走勢的動作規則。  
3. **趨勢過濾器規則**：用於篩選合適的交易環境，避免在不利趨勢中交易。  
4. **退出規則**：有一個簡單的.sell rule（未具體公開）。  

---

#### 策略細則  
1. **入市條件**：基於波動性、價格行為和趨勢過濾器的多重指標。  
2. **平均交易次數**：每年約8次交易，每次交易平均持倉不到5天，市場參與度低（約11%）。  
3. **風險調整後回報**：表現優異，年化回報率高達120%，考慮到低風險和短時間市場暴露，風險調整後回報顯著更高。  

---

#### 回測績效  
- **NASDAQ 100**：  
  - 平均年回報率：13%  
  - 最大回撤：18%（發生於2008年金融危機）  
  - 所有年度均有正回報，僅在2005年略有虧損。  

- **S&P 500**：  
  - 平均回報率：1%/次交易  
  - 總體表現良好，但不及NASDAQ 100。  

- **Consumer Staples ETF (XLP)**：  
  - 經益曲線穩定上升，僅有小幅短暫回撤。  

---

#### 結論  
1. **策略的有效性**：在多種市場環境下均表現良好，包括牛市和熊市（如2000-2002年、2008年、2022年）。  
2. **風險管理**：低交易頻率和短持倉時間有效降低了最大回撤，避免了恐慌性SELL。  
3. **市場適應性**：除NASDAQ 100外，該策略在其他指數上也有不錯的表現，但性能略有差異。  

---

#### 其他注意事項  
- 滴僕與手續費未包含在回測中，但影響微小（低交易頻率）。  
- 策略䗪售需支付 moderate fee，作者建議此策略值得投資。  
- 提供大量免費策略，但本策略需付費使用。
</details>

<details>
<summary>031. Magical RSI Trading Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=LsLv-m1AAK4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：RSI 策略分析與實證研究

#### 主題
- **策略名稱**：Relative Strength Index (RSI) 策略  
- **核心概念**：利用均值回歸（Mean Reversion）效應，在股票市場中尋找短期超賣或超買機會，進行低買高賣操作。  

---

#### 交易商品
- **市場指標**：SPX（S&P 500 指數）  
- **ETF 範例**：SPY、XLP（Consumer Staples ETF）、XLV（Healthcare ETF）。  
- **適用性**：策略可拓展至其他類似市場或ETF。  

---

#### 使用指標
- **RSI 指標**：Relative Strength Index，用於衡量資產價格的超買或超賣程度。  
  - **計算方式**：RSI = (100 × (平均上漲數 / 平均波動數))。  

---

#### 策略細則
- **進入條件**：
  - RSI 跌至 20 以下，視為超賣信號，立即買入。
  
- **退出條件**：
  - 情況一：RSI 上升至 60 以上，視為超買信號，立即賣出。  
  - 情況二：今日收盤價高於昨日最高價，鎖定利潤，賣出。  

- **操作特性**：
  - 短期交易：平均持股天數為 5 天，年均投資時間約 16%。  
  - 適用時機：主要針對市場短期過度反應（如恐慌性下跌）進行反向操作。  

---

#### 回測績效
- **回測期間**：
  - 自 1993 年開始，初始資金 10 萬美元，最終資產規模成長至 140 萬美元（年均複合報酬率為 56%）。  

- **具體數據**：
  - 總交易次數：351 次。  
  - 平均每筆交易報酬率：0.8%。  
  - 年化報酬率：9.2%（vs 存股策略的 9.7%）。  
  - 成功率：78% 的交易為盈利。  

- **風險管理**：
  - 最大回撤（Max Drawdown）：23%。  

---

#### 結論
- **優點**：
  - 策略簡單有效，具備良好的風險調整後報酬率。  
  - 年均報酬率與存股策略相近，但投資時間大幅降低。  

- **缺點**：
  - 需要在短期內多次交易，操作成本可能增加。  
  - 市場恐慌或劇烈波動時，可能存在執行難度。  

- **總結**：
  - RSI 策略作為一種均值回歸策略，在短時間內實現了不錯的報酬率，特別是在市場短期超賣時提供良好的投資機會。
</details>

<details>
<summary>032. Ranging Trading Strategies (NR7) Since 1990</summary>

[[Youtube]](https://www.youtube.com/watch?v=MHbAliaJo-c&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
- **名稱**: NR7 Volatility Strategy  
- **提出者**: Tony Crabill  
- **年份**: 開發於1990年  

### 2. 交易商品  
- **標的**: S&P 500指數（使用ETF代號SPY進行回測）  

### 3. 使用指標  
- **主要指標**: 日成交量範圍（Daily Range）  
  - 定義為每日最高價與最低價之差。  
- **額外濾鏡**: 可選用200天移動平均趨勢filer來降低最大回撤。  

### 4. 策略細則  
1. **進場條件**:  
   - 當當前交易日的日成交量範圍為過去六個交易日中最小值時，於收盤價進場做多。  
2. **離場條件**:  
   - 於次日收盤價超過昨日最高價時平倉。  
3. **額外優化**:  
   - 結合200天移動平均線作為趨勢濾鏡，進一步降低風險。  

### 5. 回測績效  
- **初始資金**: $1,100,000 USD  
- **最終資金**: 經驗曲線上顯示向上趨勢。  
- **平均收益 per trade**: 26%  
- **最大回撤**: 25%（未使用濾鏡時）  
- **年化報酬率**: 7.6%  
- **風險調整後報酬率**: 20%  

### 6. 結論  
- **優點**:  
  - 風險調整後報酬率高，適合趨勢交易者。  
  - 最大回撤可通過結合濾鏡進一步降低。  
- **缺點**:  
  - 年化報酬率略低於.buy and hold策略（9.7%）。  
  - 操作時間短，僅37%的時間持有頭寸。  

### 7. 改進建議  
- 結合200天移動平均線濾鏡可將最大回撤從25%降低至15%，同時保持平均收益不變。
</details>

<details>
<summary>033. Why You Should Love A Bear Market! (Trading Strategy)</summary>

[[Youtube]](https://www.youtube.com/watch?v=MbT5H87uxio&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
本文探討裸空市場（Bear Market）中的交易策略，特別是在股票市場表現不佳的情況下，如何利用簡單的均值回歸策略進行交易。文章強調，在裸空市場中，長期持有股票策略的表現未必最佳，而是介紹了一種針對裸空市場的有效交易方法。

### 2. 交易商品  
- 主要交易標的：NASDAQ 100 指數（使用 ETF QQQ）。  

### 3. 使用指標  
- **裸空市場定義**：股票價格低於其 200 日移動平均線（DMA）。  
- **交易策略指標**：  
  - 2日相對強度指數（RSI）低於10。  
  - 短期價格突破：當收盤價高於前一天的最高價時賣出。

### 4. 策略細則  
- **買進條件**：  
  - RSI(2) 小於10，表示超賣狀況。  
  - 價格在觸及超賣後反彈，並突破前一天高點。  
- **賣出條件**：  
  - 短期價格突破，即收盤價高於前一天的最高價時賣出。  
- **濾鏡**：只在裸空市場（QQQ 股價低於200日DMA）執行交易。

### 5. 回測績效  
- **裸空市場策略**：平均每次交易獲利1.3%，明顯優於牛市市場表現。  
- **歷史表現**：在以下裸空市場期間均錄得正收益：  
  - 2000年網際網路泡沫破裂。  
  - 2008年金融危機。  
  - 2022年全球性熊市。  

### 6. 結論  
- 裸空市場中，短期均值回歸策略表現優異。  
- 費城證券交易所（NASDAQ）在裸空市場期間的波動性較高，為交易者提供 inefficiency 機會。  
- 短賣策略在裸空市場中效果顯著，但僅限於此階段。  

---

### 中文摘要  
本文介紹了一種針對裸空市場的有效交易策略，主要基於NASDAQ 100指數（QQQ）的表現。策略核心是利用2日RSI低於10時買進，並在短期價格突破時賣出，且濾鏡設為只在裸空市場執行交易。回測結果顯示，在裸空市場中，平均每次交易獲利1.3%，顯著優於牛市市場表現。此外，短賣策略在裸空市場中效果尤為明顯。本文強調，裸空市場的高波動性提供了 inefficiency 機會，使交易者能在不確定性中尋找收益。
</details>

<details>
<summary>034. 4 Bond Trading Strategies (Rules and Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=N7PnyY132fk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 探討債券交易策略及其在投資組合中的作用，強調債券作為低風險、高收益資產的優勢。

#### 交易商品  
- **債券類型**：美國長期國債（以ETF TLT為例）。
- **其他債券種類**：政府債券、企業債券、垃圾債券等。

#### 債券特性  
- 債券與股票的區別：
  - 債券持有人在破產時優先於股東獲得償付，風險較低。
  - 股票價格波動更大，債券價格波動較小。
- **影響債券價格的因素**：信用風險、利率風險和通脹風險。

#### 策略細則  
1. **策略一：季節性交易策略**  
   - 在每月倒數第七個交易日買入TLT ETF，於月末賣出。  
   - 年回報率5.45%，投資時間佔28%。

2. **策略二：反轉策略**  
   - 於月末做空TLT ETF，於下月倒數第七個交易日回補倉位。  
   - 年回報率4.41%，儘管TLT價格上漲。

3. **策略三：結合策略一與策略二**  
   - 在每月倒數第七個交易日買入TLT ETF，月末做空，次月倒數第七個交易日平倉。  
   - 投資時間佔61%，年回報率10.25%。

4. **策略四：基於價格動量和季節性因素的長期持有策略**  
   - 具體規則未公開（會員專屬）。  
   - 年度平均收益4.8%，最大回撤較低。

#### 回測績效  
- 策略一：年回報5.45%。  
- 策略二：年回報4.41%。  
- 綜合策略三：年回報10.25%，優於Buy and Hold（7%）。  
- 策略四：平均收益0.44%，年回報4.8%。

#### 結論  
- 債券交易具有較高的風險調整後收益，適合用作投資組合的分散工具。  
- 結合股票和債券策略可提升整體收益率並降低回撤。  
- 未來表現依賴歷史數據，需謹慎評估。
</details>

<details>
<summary>035. Averaging Down Trading Strategy (Backtest+Performance)</summary>

[[Youtube]](https://www.youtube.com/watch?v=NBOGY39woyA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 重點整理：平均成本向下交易策略

#### 主題  
本文介紹了一種名為「平均成本向下交易策略」（Averaging Down Trading Strategy）的方法，該策略用於在股價下跌時買入更多股票，以降低平均成本並潛在獲利。文章還比較了傳統交易策略與平均成本向下策略的績效。

---

#### 交易商品  
- 指定的股.stock or stock index (文中提到使用S&P 500作為回測對象)。

---

#### 使用指標  
1. **相對強度指數（RSI）**：  
   - 第一種策略使用5日RSI指標，當其跌破35時買入。  
   - 第二種策略在RSI進一步下跌至少五點且仍低於50時追加投資。

---

#### 策略細則  
1. **傳統交易策略**：  
   - 買進條件：5日RSI < 35。  
   - 銀行條件：股價回升至昨日最高價以上。  

2. **平均成本向下策略**：  
   - 初始投資：使用50%的資金，買入股票當5日RSI低於50。  
   - 第二次投資：追加剩餘的50%資金，條件為每日RSI下跌至少五點且仍低於50，並遵循相同的退出規則（股價回升至昨日最高價以上）。  

---

#### 回測績效  
1. **傳統策略**：  
   - 在S&P 500指數上回溯測試表現良好（1993年至今）。  
   - 總體利潤和勝率均為「一般」（文中未具體量化）。  

2. **平均成本向下策略**：  
   - 最大虧損較低。  
   - Win/Loss比例提升，Profit Factor改善至55%（傳統策略為39%）。  
   - 總體利潤略低於傳統策略，但風險調整後報酬率更佳。  

---

#### 結論  
平均成本向下交易策略在降低最大虧損和提高勝率方面表現優異，尤其是風險調整後的報酬率更高（55% vs. 39%）。然而，其總體利潤略低於傳統策略。因此，是否選擇此策略取決於個人風險偏好與投資目標。作者建議讀者可前往Quantified Strategies網站探索更多交易策略。
</details>

<details>
<summary>036. Backtest Trading Strategies Using CHATGPT &amp; AI</summary>

[[Youtube]](https://www.youtube.com/watch?v=NOOKxAMHpGU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章要點整理

#### 主題：ChatGPT在交易策略後測中的應用  
ChatGPT作為由OpenAI開發的人工智慧語言模型，在金融交易領域展示出潛力，特別是在策略後測方面。

#### 交易商品：S&P 500指數  
本研究使用S&P 500指數作為交易標的，進行策略後測。

#### 使用指標：布林帶（Bollinger Bands）  
ChatGPT被用於生成並後測基於布林帶的均值回歸交易策略。布林帶參數設定為期間（period）20，標準差偏移量（deviation factor）2。

#### 策略細則：  
1. **.buy條件**：當價格收盤低於布林帶_LOWER_BAND時買進。  
2. **賣出條件**：當價格收盤高於布林帶_UPPER_BAND時賣出。  

#### 回測績效：  
- **年化回報率**：3.2%  
- **交易次數**：326次  
- **持倉時間比例**：45.63%  

#### 結論：  
1. ChatGPT可作為交易策略後測的輔助工具，提供策略構建的起點。  
2. 儘管ChatGPT無法取代專業金融分析，但其在Brainstorming交易想法和生成後測代碼方面具有價值。  
3. 未來AI工具有望成為量化模型的核心部分，ChatGPT將對金融市場產生革命性影響。  

#### 注意事項：  
- ChatGPT並非Trading Platform，也不提供金融建議或作出投資決定。  
- 使用者需根據需要對生成的策略進行進一步調整和優化。
</details>

<details>
<summary>037. 9/30 Trading Strategy |  (Backtest And Example)</summary>

[[Youtube]](https://www.youtube.com/watch?v=NRUyND6zzF4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 本文介紹了一種名為「9 30 Training Strategy」的趨勢-following交易策略，基於兩個移動平均指標：九天的指數移動平均（EMA）和三十天的加權移動平均（WMA）。  

#### 交易商品  
- 案例中使用標普500指數（S&P 500）作為交易標的。  

#### 使用指標  
1. **九天指數移動平均（EMA）**：用於反映短期趨勢。  
2. **三十天加權移動平均（WMA）**：用於反映較長時間周期的趨勢。  

#### 策略細則  
1. **買入條件**：  
   - 短期九天EMA上穿長期三十天WMA，並在當日收盤時買入。  
2. **賣出條件**：  
   - 短期九天EMA下穿長期三十天WMA，並在當日收盤時賣出。  

#### 第一輪回測績效  
1. **平均收益**：每筆交易平均收益率為0.85%。  
2. **相對買股持有策略（Buy and Hold）**：  
   - 本策略年化收益為4.6%，低於Buy and Hold的9.2%。  

#### 第二輪回測績效  
1. **牛市趨勢定義**：  
   - 短期九天EMA位於長期三十天WMA之上，且後者呈上昇趨勢。  
2. **買入與持有策略**：  
   - 符合條件時於當日收盤買入，並持倉至下一交易日收盤。  
3. **績效**：年化收益為4.5%，仍低於Buy and Hold的9.2%。  
4. **市場參與度**：策略僅佔用市場60%的時間。  

#### 風險調整後回報評估  
- 儘管絕對回報較低，但策略的風險調整後回報尚可，主要基於其低市場參與度。  

#### 結論  
1. 9 30 Training Strategy作為一種簡單的趨勢-following指標組合，在某些市場條件下可能提供合理的風險調整後回報。  
2. 然而，其績效仍無法超越Buy and Hold策略的表現。  
3. 更多細節可參閱量化交易策略資源（如quantifiedstrategies.com）。
</details>

<details>
<summary>038. Bullish Harami Candlestick: Definition, Trading Backtest</summary>

[[Youtube]](https://www.youtube.com/watch?v=NWK8JPbD2P0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：牛市 Harami 區間模式分析與回測研究

#### 主題
- **技術分析**：探討牛市 Harami 燃燒模式在技術分析中的應用。
- **市場趨勢 reversal**：研究此模式如何預示下降趨勢中的反轉潛力。

#### 交易商品
- **標普 500 指數（S&P 500）**：用於回測的金融商品。

#### 使用指標
- **RSI 指標**：用於篩選交易信號，確保買入時市場處於超賣狀態（RSI 等級低於 40）。
- **牛市 Harami 燃燒模式**：核心分析工具，由兩個 Candlestick 組成。

#### 經略細則
1. **牛市 Harami 模式的定義**：
   - 第一 candle 是一個大的熊市燃燒（黑色 candle），表示強烈的賣壓。
   - 第二 candle 是一個小 bulls 燃燒，通常為 Doji，並且完全包含在第一 candle 的體內。

2. **模式結構**：
   - 出現在下降趨勢中。
   - 要求有明顯的價格下跌趨勢。
   - 第一 candle 為大體黑色，第二 candle 為小型燃燒（Doji）且被第一 candle 包含。

3. **交易策略**：
   - 確定牛市 Harami 形成後，買入並持有一定時間（例如 10 個交易日）。
   - 結合 RSI 指標，確保買入時市場處於超賣狀態（RSI < 40）。

#### 回測績效
- **平均收益**：
  - 若持有 10 個交易日，平均收益率為 0.95%。
  - 收益率約為隨機時期的兩倍。

- **勝率**：
  - 勝率在 55% 到 70% 之間，具體取決於持有時間。
  - 持有時間越長，勝率越高，主要原因是股市長期上漲趨勢。

#### 結論
- **有效性**：牛市 Harami 模式結合 RSI 指標可以作為有效的交易策略，在歷史數據中表現出不錯的回測績效。
- **局限性**：
  - 勝率並非百分之百，需結合其他技術指標或分析工具以降低失敗風險。
  - 存在 false signal 的可能性，市場未必總是遵循此模式。

#### 其他
- **未來研究方向**：可探討其他 Candlestick 模式（如看跌 Harami、吞佊線等）及其交易策略。
</details>

<details>
<summary>039. 7 Algo Trading Strategies (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=NojfYk31_xI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### Summary of Key Points from the Article

#### 1. **Introduction to Algorithmic Trading**
- **Definition**: Algorithmic trading involves using automated systems to execute trades based on predefined rules and quantitative analysis.
- **Advantages**:
  - Reduces human error and emotional decision-making.
  - Allows for high-frequency trading (HFT) at optimal times.
  - Enables the simultaneous management of multiple strategies.

#### 2. **Algorithmic Trading Strategies Discussed**
- The article presents seven distinct algorithmic trading strategies, each with its own rules, indicators, and performance metrics.

#### 3. **Strategies Overview**

##### **Strategy 1: Mean Reversion in S&P 500**
- **Description**: Uses mean reversion to exploit short-term price deviations from the norm.
- **Indicators**: Based on one variable for entry and exit signals.
- **Performance**:
  - Returns approximately 15% annually since 1993.
  - Invested only 35% of the time with lower drawdowns compared to buy-and-hold strategies.

##### **Strategy 2: Momentum-Based Trading**
- **Description**: Focuses on trends in asset prices using momentum indicators.
- **Indicators**: ETFs (SPY, TLT, GLD) are used based on their moving averages.
- **Performance**:
  - Performed well until 2015 but underperformed afterward.
  - Annual returns from 2005 to present are below historical averages.

##### **Strategy 3: Faber's Momentum Strategy**
- **Description**: Developed by Meb Faber, this strategy switches between stocks, bonds, and gold based on momentum signals.
- **Indicators**: Uses 3-month and 10-month moving averages.
- **Performance**:
  - Historically achieved an annual return of ~13.1% with lower drawdowns than equities.

##### **Strategy 4: Fabian Timing Model**
- **Description**: A market-timing strategy based on weekly index movements relative to a 39-week moving average.
- **Indicators**:
  - S&P 500, TLT, and DJIA are monitored against their respective moving averages.
  - Buy signal when all indices are above the moving average; sell when at least two are below.
- **Performance**:
  - Outperformed S&P 500 since 2000 with returns significantly higher than market returns.
  - Invested approximately half the time.

##### **Strategy 5: Trend Following with ETFs**
- **Description**: Focuses on trend following using momentum indicators in ETFs.
- **Indicators**: Uses moving averages to determine entry and exit points.
- **Performance**:
  - Historically strong performance but underperformed post-2015.

##### **Strategy 6: Simple Moving Average Crossover**
- **Description**: Utilizes a basic moving average crossover to generate signals.
- **Indicators**: Short-term MA crossing above long-term MA for buy signals; vice versa for sell signals.
- **Performance**:
  - Consistent returns with moderate drawdowns.

##### **Strategy 7: Custom Quantitative Strategy**
- **Description**: A proprietary strategy available to paying subscribers, details not fully disclosed.
- **Indicators**: Based on one variable for entry and exit.
- **Performance**:
  - Historically achieved ~15% annual returns since 1993.
  - Invested only 35% of the time with lower drawdowns than buy-and-hold strategies.

#### 4. **Key Concepts and Tools**
- **Backtesting**: Essential for validating strategy performance.
- **Coding**: Required for implementing and automating strategies.
- **Systematic Mindset**: Necessary for long-term profitability, emphasizing紀律和一致性。

#### 5. **Advantages of Algorithmic Trading**
- **Efficiency**: Automates decision-making, reducing human error.
- **Scalability**: Allows management of multiple strategies simultaneously.
- **Behavioral Discipline**: Minimizes emotional interference by maintaining a layer between strategy and execution.

#### 6. **Disadvantages of Algorithmic Trading**
- **Complexity**: Requires coding skills and experience.
- **Trial and Error**: Essential for refining and optimizing strategies.
- **Resource Intensive**: Needs computational power and data for backtesting and simulation.

#### 7. **Conclusion**
- Algorithmic trading is accessible to individual traders with the right skills and mindset.
- Simplicity in strategy design often leads to better long-term profitability.
- Emphasizes the importance of systematic approaches, discipline, and leveraging the law of large numbers.

### Final Thoughts
The article underscores that algorithmic trading does not require excessive complexity. Instead, it highlights the benefits of developing a few well-tested strategies that can be automated and executed consistently over time.
</details>

<details>
<summary>040. CARRY TRADE Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=PqE3eM2eJio&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 重點整理

#### 主題：  
- 轉入策略（Carry Trade Strategy）

#### 定義與基本概念：  
- 轉入策略涉及借入低利率貨幣並將其兌換為高利率貨幣，以利用利差賺取收益。  
- 這是一種常見於外匯市場（Forex）的交易策略。  

#### 使用指標：  
- **利差**：主要依賴於兩種貨幣之間的利差（Interest Rate Differential）。  
- **流動性**：高流動性貨幣通常更受歡迎，因其交易更容易且成本更低。  

#### 策略細則：  
1. 選擇貨幣對：  
   - 借入低利率貨幣（如日本円）並兌換為高利率貨幣（如美元）。  
2. 使用槓桿：  
   - 通常需要使用高槓桿以放大利潤，但也增加了風險。  
3. 持有期限：  
   - 短期至中期交易均可適用，但長期持有需注意貨幣政策變化。  

#### 市場風險：  
- 貨幣兌換率的波動性可能導致重大損失，尤其是當市場出現意外 shocks 時。  
- 尾部風險（Tail Risk）：如 Nassim Taleb 所描述，轉入策略易受罕見但高影響力事件的影響。  

#### 結論：  
- 轉入策略具有高風險和高回報特性，適合具備經驗的交易者。  
- 雖然利差可以帶來穩定收益，但貨幣兌換率的不確定性可能導致重大虧損。  

### 注意事項與疑問：  
- 文章中提到「很多小盈、大虧」的特性，這是否意味著該策略在實際操作中更傾向於短期波動而非長期穩健收益？  
- 如何具體量化利差對轉入策略的影響？是否存在最佳的利差範圍？
</details>

<details>
<summary>041. Supertrend Indicator Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=PvPsrjGW2tI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題
- 超級趨勢指標（Super Trend Indicator）是一種追蹤趨勢的技術指標。
- 探討其效能及盈利能力。

### 2. 使用指標
- **超級趨勢指數**：基於中位價加上/減去一定倍數的平均真實範圍（ATR），形成上下兩條バンド。
- 與傳統_BANDS指標不同，超級趨勢指數只有一個信號線，其值取決於上下バンド的交錯情況。

### 3. 策略細則
- **買進條件**：價格突破超級趨勢指數上緣。
- **賣出條件**：價格跌破超級趨勢指數下緣。
- **時間框架**：
  - 使用 weekly bars。
  - 回測使用10根K線的回顧期間和3倍的ATR乘數。
- **槓桿與靈活性**：可調整參數（如LOOKBACK PERIOD和 multiplier）以適用不同市場環境。

### 4. 回測績效
- **時間範圍**：
  - 回測數據涵蓋1960年至今。
- **資金曲線**：
  - 初始投資10萬美元，最終價值接近4百萬美元。
- **交易次數**：
  - 自1960年以來僅進行38次交易。
- **績效指標**：
  - 年化報酬率：約6%（未考慮復利股息）。
  - 最大回撤（Max Drawdown）：24%，較「.buy and hold」策略的56%顯著降低。
- **風險調整後報酬**：
  - 風險調整後報酬率：9.4%，遠優於「.buy and hold」的7%。

### 5. 結論
- 超級趨勢指標在長期走勢中表現出色，尤其在風險控制方面。
- 其低頻交易特性（平均每年僅少量交易）使其適合具備耐心和長線思維的投資者。
- 推薦進一步研究並根據個人需求調整參數。
</details>

<details>
<summary>042. 3 RSI Trading Strategies - Relative Strength Index (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=Qo62oiT0xdg&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 1. 主題  
- 探討三種基於RSI（相對強弱指數）的交易策略，並提供詳細的交易規則和回測結果。

#### 2. 交易商品  
- 標普500指數（ETF代碼：SPY）

#### 3. 使用指標  
- RSI指標

#### 4. 策略細則  

##### 策略一：Two-Day RSI Strategy  
- **買入條件**：RSI（2天）低於10。  
- **賣出條件**：RSI（2天）高於80。  
- **特點**：被稱為「Two Periods RSI Strategy」，回測期間（30年）初始資金10萬美元增長至120萬美元，年化收益率約8.5%，市場參與度約27%。

##### 策略二：Two-Day RSI with Qs Exit  
- **買入條件**：RSI（2天）低於10。  
- **賣出條件**：當日收盤價高於昨日最高價。  
- **特點**：結合「Qs退出」機制，初始資金10萬美元增長至95萬美元，回測期間最大虧損23%，但虧損罕見超過12%。市場參與度較策略一低10%，風險調整後收益更佳。

##### 策略三：RSI Momentum Strategy  
- **買入條件**：建立牛市 режим時做多，否則退出市場。  
- **賣出條件**：未明確提及，但策略基於RSI的動量效應。  
- **特點**：使用100天回顧期和14天RSI，回測期間僅產生12個交易信號，其中兩次虧損，戰勝率較低。

#### 5. 回測績效  

##### 策略一緩  
- 初始資金：100,000美元  
- 終值：1,200,000美元  
- 年化收益率：8.5%  
- 市場參與度：27%  

##### 策略二  
- 初始資金：100,000美元  
- 終值：950,000美元  
- 最大虧損：23%  
- 平均虧損：<12%  
- 市場參與度：未明確，但低於策略一。  

##### 策略三  
- 交易信號數量：12次  
-虧損交易數量：2次  
-戰勝率：未明確，但表現不如前兩種策略。

#### 6. 結論  
- **最佳RSI策略**：作為均值回歸策略（如前兩個策略），建議在股票和股票ETF上使用。  
- **適合的市場**：主要適用於股票市場，因其具有均值回歸特性。  
- **最佳RSI設置**：2天或3天的回顧期，使用每日時間框架。  
- **日交易vs波動交易**：RSI更適合波動交易，使用每日K線圖。  
- **指標組合**：增強性能建議加入其他指標。
</details>

<details>
<summary>043. PMI and the Stock Market - Strategy To Trade The ISM Index</summary>

[[Youtube]](https://www.youtube.com/watch?v=RU8Ic_YUClc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 主題
- 探討ISM製造業採購經理人指數（PMI）對美國股市的影響。
- 分析PMI高於和低於50時的交易策略。

### 交易商品
- S&P 500指數。

### 使用指標
- ISM Manufacturing Index (PMI)。

### 策略細則
1. **買入條件**：當ISM PMI讀數高於50時，於月度開盤買入S&P 500。
2. **賣出條件**：持有一個月後，在次月開盤賣出。
3. **投資時間段**：策略每月進行一次交易，持倉期為一個月。

### 回測績效
1. **整體表現**：
   - 策略的年化回報率為7.3%。
   - S&P 500的年化回報率為8.5%。
2. **持倉時間**：
   - 策略每月平均投資天數為72%。
3. **風險控制**：
   - PMI高於50時的表現顯著優於低於50時，有效降低_Drawdown_。

### 擴展分析
- **持倉期限影響**：將持倉期延長至12個月時，平均收益為10.99%，投資時間增加至86%。
- **比較與結論**：
  - PMI高於50時的市場表現顯著優於隨機選擇的12個月時期。
  - 經濟擴張期（PMI高於50）的股市表現更為出色。

### 結論
- ISM Manufacturing PMI是有效的經濟指標，可用於指導股市交易策略。
- 當PMI讀數高於50時，投資股票市場能獲得更好的回報並降低風險。
- 長期持倉（如12個月）可進一步提升策略績效。
</details>

<details>
<summary>044. 4 VIX Trading Strategies (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=SoqRHI5ldXs&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 主題  
- 解釋VIX指數及其在金融市場中的作用。  

### 交易商品  
- S&P 500指數。  

### 使用指標  
- VIX指數：衡量市場波動性和恐慌程度的工具。  

### 策略細則  
1. **策略一**：基於VIX和20天移動平均線的相對位置。
   - 規則：當VIX突破其20天移動平均線，進入上行；跌破移動平均線時退出。
   - 結果：日均回報率為0.05%（VIX上行時） vs 0.03%（VIX下行時）。  

2. **策略二**：結合VIX和布林格帶。  
   - 規則：當VIX突破10天布林格上 bands 時買入，退出條件為今日收盤價高於昨日最高價。  
   - 結果：日均回報率0.45%，年化回報率4.6%；最大回撤22%。  

3. **策略三**：VIX突破和相對強度指數（RSI）。  
   - 規則：當VIX創下20天新高且5天RSI超過65時買入，退出條件同上。  
   - 結果：日均回報率0.55%，年化回報率4.8%；最大回撤22%。  

4. **策略四**：隔夜交易策略。  
   - 規則：每日收盤時買入，次日開盤時賣出。  
   - 結果：年化回報率為平均0.28%，累計577筆交易；最大回撤未提及。  

### 回測績效  
- 各策略均表現優於持有S&P 500的年化回報率（7.6%），但投資比例較低，風險調整後回報良好。  

### 結論  
- VIX指數可用於捕捉市場恐慌時的交易機會。  
- 長期來看，逢低介入市場在恐慌時期是有利可圖的。
</details>

<details>
<summary>045. 10 Trading Strategies (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=T2J8x9xlZKc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：10個交易策略與回測分析

#### 1. 季節性現貨市場策略（Stock Market Seasonality）
- **主題**：季節性交易。
- **交易商品**：標準普爾500指數（S&P 500）。
- **使用指標**：無特定指標，基於歷史價格數據。
- **策略細則**：
  - 購買時點：每年12月14日之後的第一個交易日。
  - 出售時點：新年的第三個交易日。
- **回測績效**：
  - 平均收益：1.34%。
  - 投資時間佔比：4%。
  - 額外指標：風險調整後回報率超過30%。
- **結論**：此策略在節假日期間表現穩定且優異。

#### 2. 比特幣動量策略（Bitcoin Momentum Strategy）
- **主題**：加密貨幣交易。
- **交易商品**：比特幣（Bitcoin）。
- **使用指標**：
  - 突破 historical closing price over a lookback period (25 days).
- **策略細則**：
  - 購買條件：比特幣價格突破過去25天的收盤價。
  - 出售條件：比特幣價格跌破過去25天的收盤價。
- **回測績效**：
  - 年平均回報率：86%（vs. Buy and Hold的60%）。
  - 勝率：42%。
- **結論**：儘管勝率低，但年回報率遠高於Buy and Hold策略。

#### 3. 小盤股月底交易策略（Russell 2000 End-of-Month Strategy）
- **主題**：小盤股交易。
- **交易商品**：羅素2000指數（Russell 2000）。
- **使用指標**：
  - 無特定指標，基於月度價格數據。
- **策略細則**：
  - 購買時點：每月最後一個交易日的前五個交易日之一。
  - 持股至新月的第一天。
- **回測績效**：
  - 資本累積穩定增長，但2010年後表現較弱。
  - 無現金再投資情況下，表現仍優於Buy and Hold。
- **結論**：適合小盤股交易者。

#### 4. 季節性短賣策略（Seasonal Short Strategy）
- **主題**：短賣交易。
- **交易商品**：標準普爾500指數（S&P 500）。
- **使用指標**：
  - 無特定指標，基於歷史價格數據。
- **策略細則**：
  - 建立空頭部位的時點：九月第三個交易日。
  - 平倉時點：一周後。
- **回測績效**：
  - 年平均回報率：0.9%。
- **結論**：在九月 historically 經濟蕭條時期，短賣策略表現優異。

#### 5. 櫻花節랠리策略（Santa Claus Rally Strategy）
- **主題**：節日交易。
- **交易商品**：標準普爾500指數（S&P 500）。
- **使用指標**：
  - 無特定指標，基於歷史價格數據。
- **策略細則**：
  - 購買時點：12月14日之後的第一個交易日。
  - 出售時點：新年的第三個交易日。
- **回測績效**：
  - 平均收益：1.34%。
  - 投資時間佔比：4%。
  - 額外指標：風險調整後回報率超過30%。
- **結論**：此策略在節假日期間表現穩定且優異。

#### 6. 威廉士百分比R策略（Williams Percentage R Strategy）
- **主題**：均值回歸交易。
- **交易商品**：nasdaq100指數（NASDAQ-100）。
- **使用指標**：
  -威廉士百分比R指標（Williams %R）。
- **策略細則**：
  - 購買條件：Williamson %R顯示超賣。
  - 出售條件：Williamson %R顯示超買。
- **回測績效**：
  - 年平均回報率：未提及，但表現穩定。
- **結論**：適合短期交易者。

#### 7. 小盤股交易策略（Russell 2000 Strategy）
- **主題**：小盤股交易。
- **交易商品**：羅素2000指數（Russell 2000）。
- **使用指標**：
  - 無特定指標，基於月度價格數據。
- **策略細則**：
  - 購買時點：每月最後一個交易日的前五個交易日之一。
  - 持股至新月的第一天。
- **回測績效**：
  - 資本累積穩定增長，但2010年後表現較弱。
  - 無現金再投資情況下，表現仍優於Buy and Hold。
- **結論**：適合小盤股交易者。

#### 8. 比特幣動量策略（Bitcoin Momentum Strategy）
- **主題**：加密貨幣交易。
- **交易商品**：比特幣（Bitcoin）。
- **使用指標**：
  - 突破 historical closing price over a lookback period (25 days).
- **策略細則**：
  - 購買條件：比特幣價格突破過去25天的收盤價。
  - 出售條件：比特幣價格跌破past 25天的收盤價。
- **回測績效**：
  - 年平均回報率：86%（vs. Buy and Hold的60%）。
  - 勝率：42%。
- **結論**：儘管勝率低，但年回報率遠高於Buy and Hold策略。

#### 9. 季節性短賣策略（Seasonal Short Strategy）
- **主題**：短賣交易。
- **交易商品**：標準普爾500指數（S&P 500）。
- **使用指標**：
  - 無特定指標，基於歷史價格數據。
- **策略細則**：
  - 建立空頭部位的時點：九月第三個交易日。
  - 平倉時點：一周後。
- **回測績效**：
  - 年平均回報率：0.9%。
- **結論**：在九月 historically 經濟蕭條時期，短賣策略表現優異。

#### 10. 威廉士百分比R策略（Williams Percentage R Strategy）
- **主題**：均值回歸交易。
- **交易商品**：nasdaq100指數（NASDAQ-100）。
- **使用指標**：
  -威廉士百分比R指標（Williams %R）。
- **策略細則**：
  - 購買條件：Williamson %R顯示超賣。
  - 出售條件：Williamson %R顯示超買。
- **回測績效**：
  - 年平均回報率：未提及，但表現穩定。
- **結論**：適合短期交易者。

以上策略均基於 historical performance，具體效果可能因市場環境變化而有所不同。
</details>

<details>
<summary>046. IBS - Internal Bar Strength Trading STRATEGY (Statistic &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=URPUON-P3zY&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理重點

#### 主題
- 介紹「內部柱體強度指標」（Internal Bar Strength Indicator, IBS）及其在股票市場交易中的應用。
- 探討如何利用IBS指標進行短線交易，捕捉市場波動機會。

#### 使用指標
- **IBS指標**：計算公式為今日收盤價 - 今日最低價，再除以今日最高價 - 今日最低價。該指數每日更新，範圍在0到1之間。
- **RSI指標**：用於輔助交易決策，尤其是與IBS指標結合使用。

#### 策略細則
1. **第一策略**：
   - 買入條件：IBS值低於0.1。
   - 賣出條件：IBS值高於0.9。
   
2. **第二策略**：
   - 計算方法：取過去兩日的IBS指標平均值。
   - 費入條件：兩日平均IBS值低於0.25。
   - 賣出條件：兩日平均IBS值高於0.75。

3. **第三策略**：
   - 結合三日RSI指標與IBS指標。
   - 費入條件：
     - 三日RSI值低於30，且IBS值低於0.2。
   - 賣出條件：
     - 昨日最高價被突破，或IBS值高於0.9。

#### 回測績效
1. **第一策略**：
   - 在SPY（標普500期貨）上的回測結果顯示：
     - 年化報酬率約為9.6%。
     - 最大虧損幅度僅23%，遠低於同期SPY的55%。
     - 自1993年起，僅在2001年和2018年出現虧損。

2. **第二策略**：
   - 在XLP（公用事業板塊ETF）上的回測結果顯示：
     - 投資金額從10萬美元增長至41.3萬美元。
     - 年化報酬率約為6.3%，且僅需33%的時間持倉。

3. **第三策略**：
   - 在Spy（標普500ETF）上的回測結果顯示：
     - 投資金額從10萬美元增長至150萬美元。
     - 年化報酬率約為9.6%，且僅需18%的時間持倉。

#### 結論
- IBS指標在短線交易中表現出色，尤其適合用於避免市場重大回撤。
- 與其他指標（如RSI）結合使用時，可進一步提升交易策略的有效性。
- 建議投資者將IBS指標作為輔助工具，融入整體交易系統中，以期達到更好的風險報酬比。
</details>

<details>
<summary>047. 3 Index Trading Strategies (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=UURZzdzdxTQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章重點整理

## 主題  
本文主要探討三種指數交易策略，並提供具體的交易規則和設置，用以進行回測，以驗證其歷史表現。文章還回答了一些常見問題，包括最容易交易的指數、最佳交易方式等。

---

## 交易商品  
1. ** Commodities to Equity Ratio Trading Strategy**  
   - 使用的商品指數：Goldman Sachs 商品指數（GSCI）與標普500指數（S&P 500）。  
   - 目標：利用大宗商品和股票之間的表現差異進行交易。  

2. **Value and Growth Rotation Strategy**  
   - 使用的指數ETF：iUSV（價值型股票ETF）與iUSG（成長型股票ETF）。  
   - 戰略目標：根據價值和增長兩個因子的表現，輪動投資於相應ETF。  

3. **Mean Reversion Strategy**  
   - 使用的指數ETF：標普500指數 ETF（SPY）。  
   - 策略目標：利用均值回歸特性，在指數超買或超賣時進行交易。  

---

## 使用指標  
1. **Commodities to Equity Ratio**  
   - 指標定義：GSCI 與 S&P 500 的比率，用以衡量大宗商品與股票的表現差異。  

2. **Moving Average Crossover System**  
   - 指標定義：短期和長期移動平均線的交叉點，用於決定買賣時機。  

3. **Mean Reversion**  
   - 指標定義：利用價格相對於某段時間內均值的偏離程度，判斷超買或超賣情況。  

---

## 策略細則  
1. **Commodities to Equity Ratio Trading Strategy**  
   - 交易規則：當GSCI/S&P 500比率突破短期移動平均線時做多，跌破短期移動平均線時做空。  

2. **Value and Growth Rotation Strategy**  
   - 交易規則：根據價值和增長因子的表現，輪換投資於iUSV或iUSG ETF。  

3. **Mean Reversion Strategy**  
   - 交易規則：當指數價格遠高於或遠低於 historical average 時，進行反向交易。  

---

## 回測績效  
1. **Commodities to Equity Ratio Trading Strategy**  
   - 獲利能力：具備一定的回測收益，但具體數據未公開。  

2. **Value and Growth Rotation Strategy**  
   - 獲利能力：歷史表現表明，在因子切換時輪動投資可帶來超額收益。  

3. **Mean Reversion Strategy**  
   - 獾利能力：均值回歸特性在短期和長期均表現良好，特別是在市場波動性較高時。  

---

## 結論  
1. **交易策略建議**  
   - 分散投資於不同市場、時間框架和策略，以降低風險。  

2. **最容易交易的指數**  
   - 股票市場因其多樣性和流動性，被認為是最容易交易的市場。  

3. **最佳交易方式**  
   - 短期均值回歸與長期趨勢交易均可考慮，需根據市場環境進行	backtesting。  

4. **指數交易策略的優勢**  
   - 相對於外匯交易，指數交易策略具有較低的進入門檻和更高的流動性。  

---

## 常見問題解答（FAQ）  
1. **最容易交易的指數**  
   - 股票市場因其多樣性和流動性，被認為是最容易交易的市場。  

2. **最佳交易方式**  
   - 短期均值回歸與長期趨勢交易均可考慮，需根據市場環境進行 backtesting。  

3. **指數交易策略與股票交易的差異**  
   - 指數交易通常更為分散化，整體波動性較低；股票交易則更具針對性和高波動性。  

4. **指數交易策略是否優於外匯交易**  
   - 是，指數交易策略被認為比外匯交易更容易掌握和操作。
</details>

<details>
<summary>048. 3 MEAN REVERSION TRADING STRATEGIES</summary>

[[Youtube]](https://www.youtube.com/watch?v=UkoTdKV65yk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題：均值回歸交易策略

本文介紹三種均值回歸（Mean Reversion）交易策略，涵蓋定義、指標選擇、策略細則及歷史回測績效，並探討均值回歸在不同市場中的適用性。

---

### 小節分類與整理

#### 1. 均值回歸的定義
- **基本概念**：金融資產價格在大幅偏離其平均價格會重新回歸至均值。
- **市場特性**：多數全球股票市場過去 decades 表現良好，但其他資產類別效果不佳。

#### 2. 適用市場與限制
- **適用市場**：
  - 全球股票市場表現較為穩定。
  - 商品市場可能存在短期均值回歸機會。
- **限制**：
  - 短線交易策略在上漲趨勢市場中困難。

#### 3. 均值回歸指標
- **最佳指標**：
  - IBS（自訂相對強度指數）。
  - Williams %R。

#### 4. 策略細則與交易商品

##### （1）策略一：Consumer Staples ETF (XLP)
- **交易規則**：
  - 買入條件：市場下跌後。
  - 出售條件：強勢回升時。
- **績效**：
  - 年化回報率：6.7%。
  -  持股待回酬（Buy and Hold）：6.8%。
  - 投資時間佔比：28%。
- **風險調整後回報**：23.6%。

##### （2）策略二：中國市場ETF (FXI)
- **交易規則**：
  - 短線.sell on strength.
- **績效**：
  - 年化回報率：超越 Buy and Hold。
  - 投資時間佔比：未提及。
- **注意事項**：
  - 策略在2008年前效果不佳。
  - 短線交易困難度高於長線。

##### （3）策略三：S&P 500 ETF (SPY)
- **交易規則**：
  - 買入條件：五日低點。
  - 出售條件：昨日高點或持有五天後賣出。
- **績效**：
  - 年化回報率：8.8%。
  - 比較對象：Buy and Hold（9.5%）。
  - 投資時間佔比：19%。

---

#### 5. 適用時機與策略選擇
- **最佳適用環境**：
  - 熊市市場因高波動性，均值回歸效果較佳。
  - 長線策略表現優於短線。
- **策略限制**：
  - 均值回歸未必超越趨勢跟隨策略。

---

#### 6. 其他重要資訊
- **數據與建議**：
  - 所有策略均使用每日時間框架。
  - 策略績效需結合風險考量。
- **警告**：
  - 短線交易策略在上漲趨勢市場中困難度高。
  - 均值回歸效果因市場環境變化而不同。

---

### 總結
本文提出三種均值回歸交易策略，涵蓋不同市場（Consumer Staples, 中國市場, S&P 500）和指標（IBS, Williams %R），並提供歷史績效數據。研究表明，均值回歸在熊市中表現較佳，但需注意其局限性。
</details>

<details>
<summary>049. What Happens When Stock Markets Are Overbought?</summary>

[[Youtube]](https://www.youtube.com/watch?v=V8lL3DBl44E&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### Key Points from the Article

#### Theme: Understanding Overbought Conditions in the Stock Market
- The article emphasizes the importance of understanding overbought conditions as a key concept for stock market success.
- It highlights the principle of mean reversion, which suggests that strong deviations from a trend will eventually revert to the average.

#### Trading Asset: S&P 500 Index (SPX)
- The trading strategy is applied to the S&P 500 index (SPX).

#### Indicator Used: Relative Strength Index (RSI)
- The RSI indicator is utilized to identify overbought conditions.
- The RSI measures the velocity of market movements and indicates euphoric market conditions when values are high.

#### Trading Strategy Details
1. **Entry Rule**: 
   - Buy S&P 500 at the close when the two-day RSI is above 95.
2. **Exit Rules**:
   - Sell at the close after a specified number of days (e.g., exiting after one day, two days, etc.).

#### Backtesting Performance
- The backtest results are summarized in a table with the following key points:
  - Returns in the first five days after entry are significantly lower than the long-term average return of approximately 0.05% per day.
  - As time progresses, returns gravitate toward the long-term average.

#### Conclusion
- The article concludes that overbought conditions lead to lower short-term returns compared to the long-term average.
- It suggests that investors should be cautious and expect lower returns in the immediate term after an overbought condition is identified.
</details>

<details>
<summary>050. Martingale Trading Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=VlvO82W6QlA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 本文要點整理

#### 主題  
- 文章探討了**鞅（Martingale）交易策略**，強調其為一種高風險的賭博性策略。
- 儘管該策略在理論上看似有吸引力，但作者認為它並不適合實際的金融市場交易。

---

#### 交易商品  
- 文章以標普500指數（S&P 500）作為回測對象，展示了策略在這一金融商品上的表現。

---

#### 使用指標  
1. **4日相對強度指數（RSI）**：
   - 當4日RSI跌破30時，投入33%的資金。
   - 當4日RSI跌破20時，再追加66%的資金。

---

#### 策略細則  
1. **鞅策略的核心思想**：  
   - 在每次交易失利後，將賭注金額 doubling（加倍），以期在下一筆交易中彌補所有之前的損失。  
   - 例如，若初始投資額為100美元，連續兩次失利後，投資額將分別增加至200美元和400美元。

2. **策略的理論假設**：  
   - 理論上，只要勝率為50%，最終必有一筆交易能彌補所有損失並盈利。  

3. **實踐中的問題**：
   - 金融市場中勝率 rarely 達到50%。
   - 即使最終獲勝，盈利能力可能無法完全彌補之前的損失。

---

#### 回測績效  
1. **原始策略**：
   - 年化回報率為8.7%，且投資時間佔比較小。  

2. **修改後的策略（部分資金投入）**：
   - 總體收益降低，原因是未充分利用資金，導致在罕見的大虧損情況下損失加重。

---

#### 結論  
1. 電子-Martingale策略並不適合交易者，其高風險特性容易導致帳戶被清空。
2. 作者建議尋找其他更穩健的交易策略，Martingale更適合用於賭博而非金融市場。
</details>

<details>
<summary>051. 3 Simple LITECOIN Crypto Trading Strategies | Crypto</summary>

[[Youtube]](https://www.youtube.com/watch?v=X3J7x3AUEaw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 本文介紹了三種經過背測的Litecoin交易策略，旨在幫助讀者在加密貨幣市場中實現盈利。  

#### 交易商品  
- Litecoin（ LTC ），一種去中心化的 cryptocurrencies ，用於.peer-to-peer.transactions  
- Litecoin於2011年10月發行，受Bitcoin啟發，是最早期的altcoins之一。  

#### 使用指標  
1. **短期趨勢跟蹤策略**  
   - 20日簡單移動平均線（SMA）  
2. **長期趨勢跟蹤策略**  
   - 短周期移動平均線（100日SMA）  
   - 長周期移動平均線（250日SMA）  
3. **動量策略**  
   - 25日前的收盤價  

#### 策略細則  
1. **短期趨勢跟蹤策略**  
   - 若收盤價突破20日SMA，買入。  
   - 若收盤價跌破20日SMA，賣出。  

2. **長期趨勢跟蹤策略**  
   - 當短周期SMA（100日）上穿長周期SMA（250日），買入。  
   - 當短周期SMA下穿長周期SMA，賣出。  

3. **動量策略**  
   - 若收盤價高於25日前的收盤價，買入。  
   - 若收盤價低於25日前的收盤價，賣出。  

#### 回測績效  
1. **短期趨勢跟蹤策略**  
   - 156筆交易，平均每筆交易收益8.4%  
   - 年化回報率114%  
   - 比Buy and Hold策略（年化回報率40%）表現優越。  

2. **長期趨勢跟蹤策略**  
   - 7筆交易，年化回報率66%  
   - 比Buy and Hold策略（年化回報率40%）表現稍優。  

3. **動量策略**  
   - 129筆交易，平均每筆交易收益9.6%  
   - 年化回報率70%  
   - 比Buy and Hold策略（年化回報率40%）表現優越。  

#### 結論  
- 三種策略均在回測中表現優於傳統的Buy and Hold策略，顯示出良好的盈利能力。  
- 建議讀者蔊.Subscribe至頻道或訪問網站以獲取更多策略和資產類別的相關信息。  
- 最後祝願讀者交易順利。
</details>

<details>
<summary>052. END OF MONTH Trading Strategy (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=XJp8E3HmqG8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

- **theme**: The article discusses a trading strategy for the S&P 500 index, focusing on its performance compared to a buy-and-hold approach.

- **trading instrument**: The strategy is applied to the S&P 500 index.

- **indicators used**: No specific indicators are mentioned; the strategy relies on fixed calendar-based rules.

- **strategy details**:
  - Buy at the close of the last fifth trading day of the month.
  - Sell at the close of the third trading day of the new month.
  - The strategy is invested approximately 33% of the time.

- **backtesting performance**:
  - Generated similar returns to a buy-and-hold strategy since 1960 (around 7%).
  - Drawdowns are significantly smaller, with max drawdown being half that of buy-and-hold.
  - The equity curve has been consistent and stable since 1960.

- **conclusion**: The strategy offers a viable alternative to traditional buy-and-hold investing by balancing returns with reduced risk, as evidenced by its backtesting results.
</details>

<details>
<summary>053. 3 Bollinger Band Trading Strategies (+Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=ZErni3FA24w&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：Bollinger Bands 的實用交易策略與回測分析

#### 1. 主題
- Bollinger Bands 是一種廣受歡迎且多樣化的技術指標，可用於識別趨勢、衡量波動性和尋找市場突破。
- 該文章介紹了如何有效使用Bollinger Bands來提升交易績效。

#### 2. 使用指標
- **主要指標**：Bollinger Bands（布林格帶）
  - 包含三部分：
    - 中間バンド：10天簡單移動平均線（SMA）。
    - 上 banda 和下バンド：基於均值波動的標準差，通常設置為2個標準差。
- **其他指標**：文中提及了替代版本，如百分比布林格バンド、布林格寬度和雙布林格バンド。

#### 3. 策略細則
##### (a) 基本策略
1. 利用Bollinger Bands來識別市場趨勢和波動性。
2. 上 banda 和下バンド作為超買或超賣 signals。
3. 中間バンド用於判斷短期支撐或阻力位。

##### (b) 進階策略
1. **均值回歸策略**：
   - 使用5天移動平均線並調整bands至1.5個標準差。
   - 買點：S&P 500收盤價跌破下バンド。
   - 賣點：收盤價突破昨日高點。

2. **波動性交易策略**：
   - 短期波動性增加時，市場可能突破bands。
   - 在 bands被突破後反向操作以捕捉趨勢。

3. **混合使用其他指標**：
   - 可與其他技術指標（如MACD、RSI）結合使用。
   - 建議進行回測以驗證策略的有效性。

#### 4. 回測績效
##### (a) 策略一：均值回歸策略
- **時間範圍**：1993年至現在。
- **年化報酬率**：9%，略低於買後持有策略的10%。
- **投資天數**：僅25%的交易日。
- **交易次數**：約500筆交易。
- **平均收益/損失**：
  - 每筆交易平均收益：+0.5%。
  - 滿意的勝率：76%。
- **最大回撤**：相比買後持有策略，回撤較低。

##### (b) 策略二：簡單突破策略
- **時間範圍**：未明確提及。
- **績效**：
  - 年化報酬率：未提及。
  - 投資天數：56%的交易日。
  - 最大回撤：26%，與買後持有策略相近。

##### (c) 策略三：波動性交易
- **績效**：未明確提及，但強調了短期波動性捕抓的潛力。

#### 5. 常見錯誤及建議
##### (a) 常見錯誤
1. 盲目依賴bands進行交易，忽略市場趨勢。
2. 將相同策略套用至不同資產類別（如商品和股票）而未調整。
3. 遷於相信「一招致勝」的交易規則。

##### (b) 改進建議
1. 總體考量市場趨勢，避免單純依賴bands signal。
2. 根據不同資產類別調整策略參數。
3. 建議在實盤操作前進行充份的回測和驗證。

#### 6. 結論
- Bollinger Bands 是一個強大的工具，能夠幫助交易者識別趨勢、波動性和均值回歸機會。
- 成功使用該指標的關鍵在於：
  - 根據不同市場條件調整參數。
  - 與其他技術分析工具結合使用並進行充分的回測。
  - 避免盲目跟隨，保持靈活和理性。

#### 7. 參考資料
- 文章來源：YouTube頻道「TradingWithContext」或其他相關金融教育平臺。
</details>

<details>
<summary>054. 3 Stochastics Trading Strategies 2024 (Backtested)</summary>

[[Youtube]](https://www.youtube.com/watch?v=_PGzHyatvLI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
本文介紹了三種基於 stochastic 指標的交易策略，並提供了具體的交易規則和回測績效數據。

---

### 2. 使用指標  
- **Stochastic Oscillator**：用於衡量股票最近的強弱程度及其相對於前期 highs 和 lows 的表現。  
  - 計算公式基於一定時間內（n 天）的高點和低點， сравнивает текущую цену с этим диапазоном.  
  - 當價格遠低於前期高點和低點範圍時， stochastic 讀數較低，反之則較高，並在超買和超賣水平之間震盪。

---

### 3. 交易策略  

#### 策略一：Two-Day Fast Stochastic Strategy  
- **買入市 Rules**：當 fast stochastic 值跌至 25 或以下時買入。  
- **賣入市 Rules**：當收盤價高於昨日最高價且 stochastic 指標顯示超賣時賣出。  
- **交易商品**：NASDAQ 100 ETF (NDX)  
- **回測績效**：  
  - 平均每筆交易收益：76%。  
  - 投資時間比例：26%。  
  - 經驗曲線穩定，具有較大的安全邊 margins。  

#### 策略二：3-Day Lookback Fast Stochastic Strategy  
- **買入市 Rules**：當 fast stochastic 指標跌破 20 時買入。  
- **賣入市 Rules**：同上策略一（收盤價高於昨日最高價且 stochastic 超賣時賣出）。  
- **交易商品**：10 年期美國公債 ETF (TLT)  
- **回測績效**：  
  - 平均每筆交易收益低於股權ETF。  
  - 經驗曲線表現良好且線性，但收益相對較低。  

#### 策略三：15-Level Fast Stochastic Strategy  
- **買入市 Rules**：將買入門檻降低至 15，其他規則與策略二相同。  
- **交易商品**：消費者必需品 ETF (XLP)  
- **回測績效**：  
  - 平均每筆交易收益：76%。  
  - 最大虧損：12%。  
  - isk-adjusted return_：40%（僅投資 8% 的時間）。  

---

### 4. 結論  
本文展示了三種基於 stochastic 指標的交易策略，並提供客觀的回測數據以支持其有效性。每種策略針對不同的 ETF，具有不同的風險收益特點：  
- 策略一和三在NASDAQ 100 和消費者必需品 ETF 上表現出色，具有高平均每筆交易收益和低最大虧損。  
- 策略二在公債 ETF 上表現穩定但收益相對較低。  

作者希望本文能為讀者提供交易策略的啟發和參考。
</details>

<details>
<summary>055. 3 Dual Momentum Trading Strategies</summary>

[[Youtube]](https://www.youtube.com/watch?v=_QN7zq1-elU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：三種雙矩遠交易策略斠述

#### 1. 主題  
本文介紹了三種不同的雙矩遠交易策略，探討其交易商品、策略細則、回測績效及適用性。

---

#### 2. 第一種策略：.stock and bond rotation（股票與債券輪動）  
- **交易商品**：美國股市指數（如標普500）和美國國庫券。  
- **使用指標**：-relative momentum（相對矩遠）。  
- **策略細則**：  
  1. 每月末評估股票和債券的表現。  
  2. 細分為短期（3個月）和長期（1年）兩種版本。  
     - **短期版本**：若股市過去3個月跑贏債券，則增持股票；否則增持債券。  
     - **長期版本**：若股市過去1年跑贏債券，則增持股票；否則增持債券。  
- **回測績效**：  
  - 短期版本：年化報酬率3.6%，夏普比率1.78。  
  - 長期版本：年化報酬率5.2%，夏普比率1.94。  
  - 二者皆在不同市場環境下表現優於持有標普500指數。  

---

#### 3. 第二種策略：大盤股與小盤股輪動  
- **交易商品**：美國股市中的大型股和中小型股（如羅素1000和羅素2000指數）。  
- **使用指標**：-relative momentum。  
- **策略細則**：每月末比較大型股和中小型股的表現，若大型股過去3個月跑贏，則增持大型股；否則增持中小型股。  
- **回測績效**：  
  - 年化報酬率5.4%，夏普比率2.07。  
  - 在金融危機期間仍具備韌性，因中小型股表現相對較佳。  

---

#### 4. 第三種策略：跨市場矩遠（境外股票指數）  
- **交易商品**：全球主要股市指數（如美國標普500、英國富時100、日經225等）。  
- **使用指標**：-relative momentum。  
- **策略細則**：每月末評估各市場指數表現，若某市場過去3個月跑贏其他市場，則增持該市場；否則持有現有持股。  
- **回測績效**：  
  - 年化報酬率6.7%，夏普比率2.54。  
  - 表現優於美國股市指數，展現了全球markets的分散化效果。  

---

#### 5. 研究發現與結論  
- **共同點**：  
  1. 三種策略均基於-relative momentum概念，且每月再平衡一次。  
  2. 都展現出優於傳統持有指數的報酬率和夏普比率。  
  3. 在不同市場環境下（如牛市、熊市）均有不錯的表現。  
- **差異點**：  
  1. 投資標的範圍不同，涵蓋股債、國內國際markets。  
  2. 風險程度有所差異，跨市場策略具備更高的分散化效果。  

---

#### 6. 結論與建議  
- 雙矩遠交易策略是一種基於 anomalies（如矩遠效應）的主動式投資方法，具有一定的actical application potential。  
- 投資者可根據自身風險承受能力和市場環境選擇合適的策略版本。  
- 需注意.curve fitting問題，確保策略在不同時間框架下具備 robustness。  

---

#### 7. 研究限制與未來研究方向  
- **限制**：  
  1. 回測結果可能存在過去績效不代表將來表現的問題。  
  2. 操作成本（如交易手續費、滑價等）未納入考量。  
- **未來研究**：  
  1. 探討不同市場環境下策略的有效性。  
  2. 研究策略在不同地理區域或資產類別中的表現。  
  3. 考量操作成本對整體績效的影響。
</details>

<details>
<summary>056. 4 Overnight Trading Strategies (Night Trading)</summary>

[[Youtube]](https://www.youtube.com/watch?v=_XVib3RF9sU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 主題  
文章主要探討如何通過交易SPY（標普500期貨ETF）進行隔夜交易策略，並介紹了三種不同的交易策略及其績效表現。

---

### 交易商品  
- **SPY**：標普500指數基金（S&P 500 ETF），用於跟蹤標普500指數的表現。

---

### 隔夜交易策略定義  
- 隔夜交易策略是指從當日市場收盤到次日開市期間持有的投資戰術。
- 獲利來源主要來自於股票在overnight（隔夜）期間的漲幅，而非白天交易時間的波動。

---

### 策略細則  

#### 1. 第一策略：三連陰線買入法則  
- **規則**：如果今日收盤價連續三天創新低，則於當日收盤時買入，次日開市時賣出。  
- **績效**：自1993年開始回測，共661筆交易，平均報酬率為0.13%，換算年化報酬率為2.8%。  
- **優化**：若將持股時間延長至次日收盤而非開市，平均報酬率提升至0.24%，績效顯著改善。

#### 2. 第二策略：RSI指標買入法則  
- **規則**：當2天.Relative Strength Index（RSI）低於10時，於當日收盤買入，次日開市賣出。  
- **績效**：共741筆交易，平均報酬率為0.14%，勝率62%。  
- **優化**：若延長持股時間至次日收盤，可將本金複利增加超過一倍。

#### 3. 第三策略（未明確提及）  
- 文章提到存在第三種策略，但未詳細描述其規則與績效，僅提及性能提升的可能性。

---

### 回測績效總結  
- **第一策略**：年化報酬率2.8%，勝率不明，但平均每次交易報酬率為0.13%。  
- **第二策略**：平均報酬率0.14%，勝率62%。  
- 通過優化退出時點（延長持股至次日收盤），績效顯著提升。

---

### 結論  
- 隔夜交易策略具有一定的獲利潛力，尤其是利用SPY的overnight漲幅特性。  
- 使用簡單技術指標（如RSI）或基本趨勢判斷法則可有效捕捉市場機會。  
- 持股時間的延長（至次日收盤）能顯著提升績效，建議進一步研究與優化策略。
</details>

<details>
<summary>057. Valentine&#39;s Day Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=_c09_6BV6sw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：Valentine's Day Rally in the Stock Market

#### 主題
- 探討情人節（2月14日）前後股市是否存在顯著上漲現象，即所謂的「情人節 rally」。

#### 交易商品
- 標普500指數（S&P 500）
- 新興市場ETF（eem）

#### 使用指標
- 市場收益：通過回測標普500和新興市場ETF的歷史數據來評估收益率。

#### 策略細則
1. **入場時機**：
   - 在2月10日或之後的交易日買入。
   
2. **出場時機**：
   - 在2月14日收盤賣出，若2月14日為非交易日，則延至下一個交易日平倉。

3. **持有時間**：
   - 平均持倉時間為約3個交易日。

#### 回測績效
1. 標普500指數（1960年以來）：
   - 平均單次交易收益為0.35%。
   - 股權曲線呈上升趨勢，表明情人節 rally 存在顯著性。

2. 新興市場ETF（過去二十年）：
   - 平均單次交易收益高達1.4%，表現優於其他隨機時間段。

#### 結論
- 數據支持情人節 rally 的存在。
- 新興市場在此期間表現尤為突出。
- 投資者可通過遵循該策略捕獲季節性收益。
</details>

<details>
<summary>058. RAMADAN Trading Strategy (Muslim holiday Stock Market Effect)</summary>

[[Youtube]](https://www.youtube.com/watch?v=aUkSakgFVY0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章要點整理

#### 主題：宗教節日聖殿儀式交易策略——以齉月（Ramadan）為例  
- 探討在 İslam 聖殿儀式期間（齉月）進行股票交易的可能性及其績效。

---

#### 交易商品：股票市場指數與ETF  
- **S&P 500**：用於測試主要股市的表現。  
- **KSA、EGPT、2R**：分別代表沙烏地阿拉伯、埃及和土耳其的ETF，作為 muslim 國家的代表市場。

---

#### 策略細則：
1. **買入條件**：  
   - 齉月假期若在週末開始，則於下一個交易日（星期一）買入S&P 500或其他指定ETF。  
2. **賣出條件**：  
   - 齉月結束後賣出持有的頭寸。

---

#### 使用指標：
- 無具體技術或基本面指標提及，策略基於節日時間窗口的買賣操作。

---

#### 回測績效：
1. **S&P 500**：  
   - 年化報酬率為1.1%，略高於「持有至到期」（Buy and Hold）策略。  
   - 縁於投入時間較短，整體報酬相對有限。  
2. **Muslim國家ETF（KSA、EGPT、2R）**：  
   - 近15年績效平庸，未顯著優於指數或買入持有策略。

---

#### 結論：
- 齉月期間的交易策略並未能在主要市場或伊斯蘭國家中展現出色績效。  
- 作者建議投資者參閱更多策略，強調此為眾多策略之一，需進一步研究與實證。  

--- 

此文總結了齉月節日期間的股票交易策略，並指出其在不同市場中的表現不佳，提醒投資者需謹慎評估節日效應對交易策略的影響。
</details>

<details>
<summary>059. 3 Top Bitcoin Trading Strategies (Backtest Results)</summary>

[[Youtube]](https://www.youtube.com/watch?v=cSHNnwcMIO8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 小節歸納與分析

#### 主題
本文主要探討三種比特幣交易策略及其 historical performance。這些策略基於技術指標和季節性模式，旨在通過不同的入市和出市規則來捕捉比特幣市場的上漲潛力。

---

#### 交易商品
- **比特幣**（Bitcoin）：文章中所有策略均圍繞比特幣展開，比特幣被視為具有高度波動性和潛在高回報的數位資產。  
*個人看法：比特幣的高波動性使其成為技術分析的理想對象，但其市場行為可能受到外在因素（如政策變化）的影響，需謹慎評估風險。*

---

#### 使用指標
1. **MACD 指標**：基於移動平均 convergence divergence（MACD）指標，用於衡量動量。
2. **突破策略**：基於價格突破近期高點或低點的技術分析方法。
3. **季節性模式**：基於月度交易日數 patterns，與股票市場中常用的季節性策略類似。

---

#### 策略細則
1. **MACD 策略**：
   - 入市信號：MACD 直線（12 日 EMA 與 26 日 EMA 的差值）與 signal line（9 日 EMA of MACD）的差異，即 histogram 為正。
   - 出市信號：histogram 確轉為負。
   - 操作規則：買入並持有至.sell信號出現。

2. **突破策略**：
   - 入市信號：價格突破 25 天前的收盤價高點。
   - 出市信號：價格跌破 25 天前的收盤價低點。
   - 操作規則：買入並持有至 sell 信號出現。

3. **季節性策略**：
   - 入市信號：每月倒數第五個交易日買入比特幣。
   - 出市信號：新月的第三個交易日賣出比特幣。
   - 操作規則：定期買入並持有至指定.sell時間。

---

#### 回測績效
1. **MACD 策略**：
   - 年回報率：77%（2015 年至當前）。
   - 介入時間：54%。
   - 費用：與買後持有的策略相比，此策略雖然勝率高，但需注意其 signal 的 timeliness 和價格波動的敏感性。

2. **突破策略**：
   - 年回報率：未提及，但 trades 的平均回報率不明確。
   - 介入時間：56%。
   - 勝率：43%，虧損交易佔 57%。
   - 總體表現：回測結果顯示策略有效，但需注意其在市場 volatility 中的操作風險。

3. **季節性策略**：
   - 年回報率：41%。
   - 介入時間：23%。
   - 平均回報率：3.2% per trade。
   - 總體表現：此策略在 historical data 中表現穩定，但近期成效有所 attenuation。

*個人看法：季節性策略看似在比特幣市場中具有一定的有效性，但也可能受到市場結構變化或外部事件的影響。建議在實際操作前進一步驗證其 robustness。*

---

#### 結論
- 三種策略均展示了超越 buy-and-hold 戰略的回報率。
- 尤其是 MACD 和季節性策略，表現更加突出。
- 策略的有效性取決於市場條件和交易者的風險偏好。

*個人看法：本文提供了一些值得探討的交易策略，但需注意回測結果可能存在的 overfitting 演化。在實際交易中，建議結合多種指標或使用 machine learning 方法來提高 strategy 的 robustness 和 adaptability。此外，比特幣市場的高度波動性要求交易者密切跟蹤市場變化並設定嚴格的 risk management 機制。*

---

### 總結
本文介紹了三種基於技術分析和季節性模式的比特幣交易策略，並通過 historical backtesting 驗證了其有效性。雖然這些策略在過去表現優異，但需謹慎評估其在不同市場條件下的適用性和風險。
</details>

<details>
<summary>060. 200-Day MA Strategy (Backtest, Rules And Performance)</summary>

[[Youtube]](https://www.youtube.com/watch?v=dEZ6Wy_EYmU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章重點整理

## 主題  
本文探討了著名投資者Paul Tudor Jones使用200天移動平均線作為交易指標的原因及其應用策略。文章介紹了200天移動平均線在趨勢跟蹤和短期均值回歸策略中的作用，並通過回測分析評估其績效。

---

## 交易商品  
- 股指期貨：文中提到使用S&P 500指數（Spyders ETF, SPY）作為交易標的。
- 其他金融資產：文章未明確提及，但策略可跨商品應用。

---

## 使用指標  
1. **200天移動平均線**：用於趨勢判斷和策略過濾。  
2. **相對強度指數（RSI）**：在短期均值回歸策略中使用5天RSI指標。

---

## 策略細則  

### 趨勢跟蹤策略  
- **買入條件**：當S&P 500指數站上200天移動平均線時進入市場。  
- **賣出條件**：當指數跌破200天移動平均線時退出市場。  
- **持有時間**：長線投資，直至趨勢轉變。  

### 短期均值回歸策略  
- **基本規則**：  
  - 購買信號：5天RSI低於35。  
  - 賣出信號：5天RSI高於50。  
- **過濾條件**：加入200天移動平均線作為策略過濾器，要求價格需站上200天移動平均線才能生成交易信號。  

---

## 回測績效  

### 趨勢跟蹤策略  
- **回測時間段**：1960年至今。  
- **績效指標**：  
  - 年化報酬率：6.75%（不含股息），略低於買後持有的7%。  
  - 最大虧損：28%，大大小於買後持有的56%。  
  - 避免了2008年金融危機的大幅虧損，最大虧損降低55%。  

### 短期均值回歸策略  
- **基本績效**：  
  - 最大虧損：29%，顯示高波動性。  
  - 交易次數下降，但平均每筆交易收益和勝率提升。  
- **加入200天移動平均線後**：  
  - 收益曲線更平滑，最大虎損降低。  
  - 交易頻率降低，但勝率提高，_human bias_（人性的虧損負面效應）得以緩解。  

---

## 結論  
1. **200天移動平均線的有效性**：  
   - 作為趨勢指標，能有效過濾市場噪音，降低波動性。  
   - 在牛市中保持參與，避免熊市的重大虧損。  

2. **策略改進空間**：  
   - 可進一步優化交易信號生成規則或加入其他指標作為 supplemental filters。  
   - 適度調整過濾條件以平衡風險與收益。  

3. **實用性建議**：  
   - 200天移動平均線策略適合風險承受能力較低的投資者，特別是在大熊市來臨時能有效降低虧損。  
   - 短期均值回歸策略若加入趨勢過濾器，可提升執行續命力和績效穩定性。  

--- 

**結語**：200天移動平均線不僅是Paul Tudor Jones的首選指標，其簡單有效的特性使其成為長期投資和交易策略中的重要工具。
</details>

<details>
<summary>061. Oversold Trading Strategy (What Happens When Stock Markets Are Oversold?)</summary>

[[Youtube]](https://www.youtube.com/watch?v=few_gh6Td8E&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題：股票市場超賣狀態的概念與策略  
   - 超賣（Oversold）是指股市經歷一段持續下跌的時期，可能是數天、數周或數月。  
   - 理解超賣概念對於市場成功交易至關重要。  

### 2. 使用指標：相對強度指數（RSI）  
   - RSI用於衡量市場走勢的速度和力度。  
   - RSI低於20表示市場可能處於超賣狀態，預示短期反彈機會增加。  

### 3. 策略細則  
   - **買入條件**：當SP 500的日RSI低於20時，在收盤時買入。  
   - **.sell條件**：在收盤時賣出，當日盤高於昨日最高價時平倉。  
   - **交易策略**：簡單的均值回歸策略，基於超賣市場短期內可能反彈的假設。  

### 4. 回測績效  
   - **買入.sell規則**：在RSI低於20時買入，並在價格反彈至昨日最高價時賣出。  
   - **回測結果**：  
     - 累積收益：從10,000美元增長至130萬美元。  
     - 年化回報率：9.14%。  
     - 投資時間：僅16.8%的交易日參與市場。  
   - **風險調整後回報**：Risk-Adjusted Return = 9.14% / 16.8% ≈ 54，表示單位風險下的高報酬率。  

### 5. 結論  
   - 超賣市場短期內可能帶來較高的回報率。  
   - 基於RSI指標的簡單策略可以在控制風險的前提下實現穩定收益。  
   - 投資者應理解均值回歸原理，並善用技術指標進行交易決策。
</details>

<details>
<summary>062. 6 Larry Connors Trading Strategies</summary>

[[Youtube]](https://www.youtube.com/watch?v=gX8FjjKR7ec&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：六項拉裡·康納斯（Larry Connors）改進交易策略分析

#### 1. 主題  
本文介紹並分析了六種由拉裡·康納斯及其團隊開發的交易策略，這些策略均來源於其著作《High Probability ETF Trading》和《The Book of ETFs》。文章對每項策略進行了詳細闡述，包括策略細則、使用指標、回測績效等，並總結了若干主要啟示。

---

#### 2. 交易商品  
所有.strategy均基於以下交易商品：  
- 標普500指數（S&P 500）ETF（以SPY為代表）。  
- 策略也可用於期貨市場，但需自行為其他市場進行回測。  

---

#### 3. 使用指標  
各策略主要使用以下技術指標：  
1. **移動平均線（Moving Average）**，尤其是200日移動平均線（MA）。  
2. **相對強度指數（RSI）**。  
3. **高點和低點分析**。  

---

#### 4. 策略細則  
以下是六項策略的簡要描述：  

##### (1) **均值回歸策略（Mean Reversion Strategies）**  
- 基本思想：買入被市場低估的資產，即「抄底」。  
- 適用於標普500指數，自1985年以來表現良好。  

##### (2) **三日高低策略（Three-Day High/Low Strategy）**  
- 進場條件：價格站上200日移動平均線，且近三個交易日的高點和低點均創新低。  
- 策略罕見交易，年化回報率為3.6%，勝率79%。  

##### (3) **RSI 30 和 RSI 50 策略**  
- 進場條件：價格站上200日移動平均線且5日RSI低於30。  
- 出場條件：5日RSI突破50。  
- 年化回報率6.1%，勝率72%，風險調整後回報率高達52%。  

##### (4) **三日新 highs/ lows 策略**  
- 進場條件：價格站上200日移動平均線，且近三個交易日的最高價和最低價均創新低。  
- 年化回報率3.6%，勝率79%，最大回撤14%。  

##### (5) **RSI 30 和 RSI 50 策略（修改版）**  
- 與上述策略類似，但具體進場和出場條件有所不同。  
- 年化回報率6.1%，勝率72%，風險調整後回報率高達52%。  

##### (6) **均值回歸策略（另一種）**  
- 基本思想：買入被市場低估的資產，即「抄底」。  
- 年化回報率為3.6%，勝率79%，最大回撤14%。  

---

#### 5. 回測績效  
所有策略均基於SPY ETF進行歷史數據回測，主要績效指標包括：  
- **年化回報率**（Annualized Return）：最高為6.1%，最低為3.6%。  
- **勝率（Win Rate）**：大多數策略勝率在70%-80%之間。  
- **最大回撤（Max Drawdown）**：均低於15%，恢復速度較快。  
- **市場暴露時間（Market Exposure）**：大多數策略僅部分時間持有頭寸，平均市場暴露時間低於20%。  

---

#### 6. 總結與啟示  
##### (1) 均值回歸策略的有效性  
均值回歸策略在標普500指數上表現出色，但其未來效果無法保證，需密切跟蹤市場變化。  

##### (2) 200日移動平均線的濾損作用  
200日移動平均線有效區分牛市和熊市，顯著降低最大回撤，提高策略穩健性。  

##### (3) 策略之間的相容性問題  
六項策略雖然個體績效良好，但相互之間存在較高相似性，組合交易效果並不理想（年化回報率6.3%，勝率76%，平均收益下降）。  

##### (4) 市場暴露與風險控制  
多數策略保持低市場暴露，有利於同時運行其他 complementary 策略以提高整體市場參與度。  

##### (5) 風險提示  
所有回測結果基於 historical data，未來表現可能不同，投資者需謹慎評估市場環境和個人風險承受能力。  

--- 

**注意：以上內容為一般性描述，具體策略細節和歷史數據請參閱相關著作或專業研究報告。**
</details>

<details>
<summary>063. 3 Profitable Trading Strategies (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=j1qjX0Zxpd0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：三個盈利能力的交易策略

#### 1. 主題
本文介紹了三種盈利能力的交易策略，並基於S&P 500和NASDAQ 100進行回測，涵蓋均值回歸、趨勢跟隨以及兩者結合的混合策略。

---

#### 2. 交易商品
- **S&P 500 指數ETF（Spy）**
- **NASDAQ 100 指數ETF（QQQ）**

---

#### 3. 使用指標
1. **均值回歸策略**  
   - **橡皮筋策略**：基於短期波動進行交易，買弱賣強。
   
2. **趨勢跟隨策略**  
   - **金色交叉策略**：使用50日和200日移動平均線（MA）作為信號指標。

3. **混合策略**  
   - 結合均值回歸與趨勢跟隨，基於200日移動平均線判斷是否啟用均值回歸交易。

---

#### 4. 策略細則
1. **橡皮筋策略（Mean Reversion Strategy）**  
   - 基於短期價格波動進行高頻交易。
   - 規則：買入超賣市場，賣出超買市場。

2. **金色交叉策略（Trend Following Strategy）**  
   - 使用50日和200日移動平均線判斷主要趨勢方向。
   - 規則：當50日MA上穿200日MA時.buy，當50日MA下穿200日MA時.sell。

3. **混合策略（Combined Strategy）**  
   - 基於200日移動平均線判斷是否啟用均值回歸。
   - 當價格在200日MA之上時，執行均值回歸交易；否則休息或趨勢跟隨。

---

#### 5. 回測績效
1. **橡皮筋策略**  
   - S&P 500：年化報酬率8.7%。  
   - 持股時間短，平均約1-2天。

2. **金色交叉策略**  
   - S&P 500：年化報酬率7.4%，勝率63%。  
   - 持股時間長，平均約數月。

3. **混合策略**  
   - S&P 500：年化報酬率12.5%，勝率83%。  
   - NASDAQ 100：年化報酬率13.6%，勝率90%。  
   - 投資時長：71%。

---

#### 6. 結論
- **多策略組合的重要性**：單一策略鱤有生命周期，建議使用多種策略（如均值回歸與趨勢跟隨）及多元化的市場和時間框架。
- **分散化投資**：交易不同市場、資產類別、策略類型和時長可降低風險並提高報酬。
- **實證為基礎**：所有策略均基於歷史數據回測，但需注意未來表現可能受市場環境影響。

---

#### 7. 常見問題解答（FAQ）
1. **如何制定盈利能力的交易策略？**  
   - 依賴 historical backtesting，制定明確規則並進行模擬交易驗證。

2. **最賺錢的交易策略是什麼？**  
   - 無「最佳」策略，推薦使用多策略組合以分散風險。

3. **盈利能力的交易策略能持續多久？**  
   - 策略壽命有限，建議 diversification 以降低依賴度。

---

#### 8. 參考資料
- 文章來源：Trading Strategy Article
</details>

<details>
<summary>064. Stairs Trading Strategy (A Trend &amp; Pullback Combo) | +Backtest</summary>

[[Youtube]](https://www.youtube.com/watch?v=jk2RxsVKA6Y&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章重點整理

## 主題
- 介紹一種名為「樓梯交易策略」（Stairs Trading Strategy）的新穎交易方法。

## 交易商品
- 檢測對象：標普500指數（S&P 500）

## 使用指標
- 移動平均線：
  - 200日移動平均線（200-Day Moving Average）
  - 25日移動平均線（25-Day Moving Average）

## 策略細則
1. **進場條件**：
   - 收盤價必須高於200日移動平均線。
   - 收盤價必須低於25日移動平均線。
   - 若上述兩項條件均滿足，則在收盤時進場。

2. **出場條件**：
   - 當收盤價突破並站上25日移動平均線時，於收盤時出場。

## 回測績效
1. **年化回報率**：
   - 樓梯交易策略：6.1%
   - 資產配置法（Buy and Hold）：7.7%

2. **最大回撤**：
   - 策略的最大回撤栒氐於20%。
   - 策略的投資時間佔用率為23%，即每年僅23%的交易日進行操作。

## 文章未明確之處
1. **策略的有效性**：
   - 文章聲稱此策略在標普500指數上的表現優於買後不賣法，但未提供具體回測數據或.statistics。
   - 未提及策略在不同市場環境（如牛市、熊市）下的表現。

2. **風險管理**：
   - 文章未提及止損或止盈機制，也未討論該策略在市場大幅波動時的應對措施。

3. **交易成本**：
   - 未考慮交易手續費、滑點等實際交易成本對策略績效的影響。

4. **策略的靈活性**：
   - 策略是否適用於其他金融商品（如個股、債券、外匯等）？
   - 200日和25日移動平均線的選擇是否有最佳比例或調整空間？

## 結論
- 樓梯交易策略基於移動平均線的簡單交叉，理論上利用短期均線突破長期均線來捕捉市場趨勢。
- 回測結果表明該策略在回撤控制方面優於買後不賣法，但年化回報率稍低。
- 策略執行簡便，適合初級交易者，但仍需進一步驗證其在不同市場條件下的穩定性與收益能力。
</details>

<details>
<summary>065. 5 Swing Trading Strategies 2024 (Backtest And Settings)</summary>

[[Youtube]](https://www.youtube.com/watch?v=kWgUlIFAwqg&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：五個經過回測且䗪實的波段交易策略

---

#### **1. 主題與目的**
本文介紹了五個經過回測且有效的波段交易策略，旨在提供交易者多種選擇，並展示如何通過結合這些策略來提升整體績效。文章強調了每個策略的細則、回測結果以及組合策略的效果。

---

#### **2. 交易商品**
所有策略均基於以下交易商品：
- **標普500指數（S&P 500）**
- 其他未提及的資產類別（需參閱文章或作者網站）

---

#### **3. 使用指標**
文中提到的主要指標包括：
1. **IBS指標**：用於評估市場強弱，具體門檻值因策略而異。
2. ** historical high/low ranges**：基於過去N天的最高和最低價格來判斷入市時機。

---

#### **4. 策略細則**
以下是五個策略的簡要描述及其細則：

##### **策略1：基於IBS指標和歷史高點**
- **入市條件**：
  - 今日收盤價創下過去10天新高。
  - IBS指標低於0.15。
- **出市條件**：
  - 收盤價高於昨日收盤價。
- **細則**：
  - 交易者需在當日收盤後入市，次日觀察市場走勢。

##### **策略2：基於IBS指標和波動性**
- **入市條件**：
  - 收盤價創下過去N天新高。
  - IBS指標低於0.3。
- **出市條件**：
  - 收盤價高於昨日收盤價。

##### **策略3：基於波動性和IBS指標的組合**
- **入市條件**：
  - 今日波動範圍（日內高低差）小於過去六天的平均波動範圍。
  - 收盤價站上200天移動平均線。
- **出市條件**：
  - 收盤價高於昨日收盤價。

##### **策略4：基於歷史高點和IBS指標**
- **入市條件**：
  - 今日最高價創下過去10天新高。
  - IBS指標低於0.15。
- **出市條件**：
  - 收盤價高於昨日收盤價。

##### **策略5：未提及具體細則**
- 該策略為六年前制定， 최근에較好的效果，具體細則需參考原文或作者網站。

---

#### **5. 回測績效**
以下是每個策略的回測結果：

##### **策略1**：
- 年化回報率：3.24%。
- 平均持倉時間：<otch week（未明確）。
- 最大回撤：<8%。
- 交易次數：<161次。

##### **策略2**：
- 年化回報率：未提及。
- 最大回撤：<8%。
- 交易次數：<161次。

##### **策略3**：
- 年化回報率：未提及。
- 最大回撤：<8%。
- 交易次數：<161次。

##### **策略4**：
- 年化回報率：未提及。
- 最大回撤：<8%。
- 交易次數：<161次。

##### **策略5**：
- 年化回報率：未提及。
- 最大回撤：<8%。
- 交易次數：<161次。

##### **五個策略組合**：
- 初始資金：$100,000。
- 終值：$5.3 million（截至2023年）。
- 年化回報率：14.1%。
- 投資時長：<1980天。
- 交易次數：1131次。
- 平均每筆交易收益：<otch 0.38%。
- 總體績效：
  - 具有顯著的年化回報率，且整體投資時間僅為一半，顯示策略組合的有效性。
  - 在2011、2015和2018年出現虧損，但相較於牛市表現更穩健。

---

#### **6. 結論**
- **單一策略**：每個策略均經過嚴格回測，具有穩定的績效。
- **策略組合**：整體組合策略在風險控制和收益提升方面表現出色，特別是在市場波動性較高的時期。
- **建議**：
  - 初學者可從單一策略入手，逐步熟悉交易規則。
  - 高級交易者可嘗試結合多個策略，以進一步優化績效。
  - 更多詳細信息請參閱作者網站或原文。

---

此文為交易者提供了多種選擇，並展示了如何通過策略組合來提升整體交易績效。
</details>

<details>
<summary>066. 3 Swing Trading Strategies 2024 (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=lKzoUptU2io&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 小節一：主題  
- 討論三種Swing Trading策略在S&P 500指數中的應用。  

### 小節二：交易商品  
- S&P 500指數（ Standard & Poor's 500 Index）。  

### 小節三：使用指標  
1. **IBS指標**（未明確具體定義，但用於篩選.sell條件）。  

### 小節四：策略細則  
#### 策略一：  
- 前提：今日為星期一（第二天下跌收盤）。  
- 賣出條件：今日收盤價高於昨日最高價。  

#### 策略二：  
- 前提：今日收盤價創下5日新低。  
- 賣出條件：IBS指標低於0.25，且今日收盤價高於昨日最高價。  

#### 策略三：  
- 前提：今日盤中高點低於前一日的10日高點。  
- 賣出條件：IBS指標低於0.15，且今日收盤價高於昨日最高價。  

### 小節五：回測績效  
- 綜合三種策略形成投資組合。  
- 總體表現優於Buy and Hold策略。  
- 投資時間佔比約27%。  

### 小節六：結論  
- 提供多種Swing Trading策略，適合S&P 500指數交易。  
- 策略組合在效率和收益之間取得良好平衡。  
- 更多相似策略可於本網站查閱。
</details>

<details>
<summary>067. Simple VOLATILITY Trading Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=lPhVdBHQfHE&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 小節：文章主旨  
- 文章主要探討了市場波動性（Volatility）與股價走勢之間的關聯性，並提出了一種基於200天移動平均線的市場週期過濾器來分類牛熊市。  
- 認為在高波動性環境下，股票價格通常會下跌，這表明波動性與熊市存在正相關。  

### 小節：交易商品  
- 交易標的主要為股票（Stocks）。  

### 小節：使用指標  
- **200天移動平均線（200-Day Moving Average）**：用於作為市場週期的過濾器，判斷市場是否處於牛市或熊市。  
- **波動性（Volatility）**：作為影響股價走勢的重要指標。  

### 小節：策略細則  
1. 市場分類標準：  
   - 當股票價格跌破200天移動平均線時，市場被判定為熊市（Bear Market）。  
   - 當股票價格位於200天移動平均線上時，_market被判定為牛市（Bull Market）。  

2. 交易策略：  
   - 策略的信號發出點基於市場 regime 的過濾器。  
   - 不論市場處於牛市還是熊市，均建議持續執行交易策略，不必額外判斷買賣時機。  

### 小節：回測績效  
- 回測結果顯示，在高波動性環境下，該策略的表現優於低波動性環境。  
- 策略在不同市場週期中的穩定性和適應性得到了一定程度的驗證。  

### 小結  
- 文章強調了波動性對股價走勢的影響，並提出了一種基於200天移動平均線的簡單過濾器來分類市場週期。  
- 試圖通過數據分析表明，策略在高波動性環境下的表現更為優異，且不建議因市場週期変化而調整交易策略。
</details>

<details>
<summary>068. Gold Trading Strategy (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=mic1SPbN7cA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：基於隔夜持倉的黃金交易策略分析

#### 主題
文章探討了一種基於隔夜持倉（從收盤到次日開盤）的黃金及相關 ETF 交易策略，旨在揭示其潛在的盈利能力。

#### 交易商品
- **GDX**: 跟蹤黃金礦業公司的 ETF。
- **GLD**: 跟蹤黃金價格的 ETF。

#### 策略背景
- 觀察發現，從收盤到次日開盤（隔夜持倉）期間，黃金及黃金礦業 ETF 的收益表現穩定且呈上升趨勢。
- 相反，當日交易（買入開盤價、賣出收盤價）往往導致虧損。

#### 使用指標
- **Equity Curve**: 用於展示策略的累計收益曲線。
- 無具體技術指標提及，重點在於時間窗口的選擇和組合變量的應用。

#### 策略細則
1. **基礎策略**:
   - 從收盤到次日開盤持倉，無需頻繁交易。
2. **優化策略**:
   - 添加兩個輔助變量（未明確說明具體內容）以增強收益穩定性。
3. **適用性**:
   - 適用於長期投資者或自動交易系統。

#### 回測績效
- **基礎策略**:
  - 隔夜持倉的累計收益呈穩定上升趨勢，表現優於當日交易。
  - 當日交易的平均回報為略微負值，顯示其不具可持續盈利能力。
- **優化策略**:
  - 添加變量後，策略表現出持續穩定的正向回報，維持近二十年。

#### 結論
1. 隔夜持倉在黃金及黃金礦業 ETF 中展現出顯著的正向收益趨勢。
2. 該策略本身不具備足夠的交易規模，但可作為基礎策略與其他變量結合使用以提升盈利能力。
3. 文章提供了一個長期穩定的交易框架，適合進一步研究和優化。

#### 建議
- 對於感興趣的研究者或投資者，建議訪問文中提到的網站獲取更多細節信息。
</details>

<details>
<summary>069. DEMARKER TRADING STRATEGY  (BACKTEST)</summary>

[[Youtube]](https://www.youtube.com/watch?v=o_rgI0h9Qs8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
- 討論一種技術分析指標（Marker Indicator）及其在交易策略中的應用與優化。

### 2. 交易商品  
- 操作對象為S&P 500指數（Spider，SPY）。  

### 3. 使用指標  
- **Marker Indicator**：用於判斷超買（Overbought）和超賣（Oversold）水平。  

### 4. 策略細則  
- 初始策略：
  - 確定最佳的回顧期為5天。
  - 設定購買門檻為5。
  - 在指標達到80時賣出。

- 優化後策略：
  - 改用「.sell on strength」策略，即在當日收盤價高於昨日最高價時賣出。  

### 5. 回測績效  
- 初始策略 equity curve：  
  - 存在明顯的波動性和回撤（drawdowns）。  

- 優化後策略 equity curve：  
  - 策略性能顯著提升，具體數據未明確提及。  

### 6. 結論  
- 指標雖能提供買賣信號，但在市場波動性較大時可能存在局限性。
- 引入「.sell on strength」策略後，整體績效有所改善，但仍需進一步優化以應對市場變化。
</details>

<details>
<summary>070. The Failed Bounce Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=oh07KVESvjk&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題 (Theme)
   - **Failed Bounce Trading Strategy**: 文章介紹了一種名為「Failed Bounce」的交易策略，該策略最初於八年前發表在網站上。此策略的核心思想是利用價格波動中的failed bounce現象來捕捉市場機會。

### 2. 交易商品 (Asset Classes)
   - **股票 (Equities)**：主要適用於股票，特別是在1980年代晚期以來的表現。
   - **ETFs（交易所買賣基金）**：策略也可用於基於股權的ETFs，如.consumer staples（xlp）和QQQ等科技指數ETF。
   - **不建議用於商品或債券**: 策略在商品或債券上表現不佳。

### 3. 使用指標 (Indicators Used)
   - **IBS (Internal Bar Strength)**：文中提到IBS是一種 underrated 應被市場重視的指標，具體計算方式未提及，但強調其重要性。
     - **註解**: IBS用於評估市場內部強度，幫助判斷買賣時機。

### 4. 策略細則 (Strategy Details)
   - **進場條件**：
     - 昨日的IBS指數至少為0.6或更高。
     - 昨日的低點低於過去五天中的最低低點。
   - **出場條件**：
     - 今日收盤價高於昨日最高價時出場。
   - **操作方式**：
     - 短期回調（short-term pullbacks）時進場，強勢（strength）時出場。

### 5. 回測績效 (Backtesting Performance)
   - **數據範圍**: 自1976年起的資料。
   - **交易次數**: 204筆交易。
   - **平均每筆交易收益**: 0.86%。
   - **勝率**: 77%。
   - **淨利潤**: 450 (未明確貨幣單位)。
   - **年化回報**: 5.8%。
   - **投資時間比例**: 約8.5%的時間投入市場。
   - **風險調整後回報**: 67。

### 6. 結論 (Conclusion)
   - **策略有效性**：在股票和特定ETFs上表現良好，但對商品或債券效果不明顯。
   - **建議**：觀看該頻道的其他影片以進一步了解IBS指標，並訪問網站查看更多策略。

### 7. 其他 (Additional Information)
   - **公開資源**: 策略代碼和更多回測資料可在其官網找到。
   - **頻道號召**：鼓勵訂閱頻道、點贊及分享以獲取更多交易洞見。
</details>

<details>
<summary>071. Golden Cross Trading Strategy (Guide+Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=okJHlykwQYo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：Golden Cross 與其策略分析

#### 主題  
- 本文介紹了一種基於Golden Cross指標的交易策略，旨在降低熊市損失並在牛市中最大化收益。
- 策略的核心在於利用50日和200日移動平均線的交叉信號來進行買賣決策。

#### 交易商品  
- 檢測對象為標準普爾500指數（S&P 500）。

#### 使用指標  
- **Golden Cross Indicator**：基於50日短期移動平均線（DMA）和200日長期移動平均線（DMA）的交叉信號。
    - **Bullish Signal**：當50日DMA向上穿越200日DMA時，視為買入信號。
    - **Bearish Signal**：當50日DMA向下穿越200日DMA時，視為賣出信號。

#### 策略細則  
1. **進場條件**：
    - 50日DMA向上穿越200日DMA，買入標的資產。
2. **出場條件**：
    - 50日DMA向下穿越200日DMA，賣出標的資產。
3. **持有期**：  
    - 每次交易平均持有約350天。
4. **活動頻率**：  
    - 策略螠活性較低，總共產生32筆交易。

#### 回測績效  
- **回測時間跨度**：1960年至今。  
- **交易表現**：
    - 78%的交易為盈利 trades。
    - 平均每筆交易收益達15.4%。  
    - 年化收益率為6.6%。  
- **與「買入並持有」策略相比**：
    - 年化收益率略低（6.9% vs 6.6%）。  
    - 策略投資時間僅為69%，而「買入並持有」為100%。  
    - 最大回撤更低（33% vs 56%），顯示風險調整後回報更佳（9.5%）。  

#### 結論  
- **優點**：
    - 成功降低了熊市中的損失。
    - 風險調整後回報 superior。  
- **缺點**：
    - 年化收益率略低於「買入並持有」策略。  
    - 存在 whipsaw signals，可能增加交易成本。  
- **總結**：Golden Cross 策略在風險控制和熊市防禦方面表現優異，適合偏好降低市場參與度的投資者。

#### 附註  
- 文章末尾提及另一個短期策略（NR7 Strategy），並鼓勵讀者訪問 quantifiedstrategies.com 以獲取更多資源。
</details>

<details>
<summary>072. Doji Reversal Trading Strategy (Backtest + Candlesticks Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=p3St7_mOOOI&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

---

#### 1. 主題：Doji 燃燒棒模式與交易策略  
- Doji 是一種傳統的 Candlestick 模式，常被用於技術分析中，用以判斷市場情緒和價格走勢。  
- 該視頻探討了如何將 Doji 模式應用於股票市場交易，並通過回測來驗證其有效性。

---

#### 2. 交易商品：S&P 500 指數（Spy）  
- 文章中提到的交易標的為 S&P 500 指數（Spy），這是一種廣泛被使用的市場指標，代表美國股市整體表現。  

---

#### 3. 使用指標：Doji 燃燒棒模式和相對強度指數（RSI）  
- **Doji 燃燒棒模式**：四種類型的 Doji 模式被提及，包括：  
  - 中立性 Doji  
  - 陰墓estone Doji  
  - 龍吟 Doji  
  - 長腿 Doji。  
- **相對強度指數（RSI）**：用於過濾交易信號，買入條件為五日 RSI 小於 50。

---

#### 4. 策略細則  
- 買入條件：在-chart 中出現四種 Doji 模式之一時買入。  
- 賈售條件：初期策略為持有五天，後期加入強勢賣出_criteria（close 高於昨日最高價）。  
- RSI 過濾器：買入時要求五日 RSI 小於 50，以捕捉超賣市場機會。  

---

#### 5. 回測績效  
- 初期回測結果：  
  - 持有五天的平均收益率為 0.32%。  
  - 結果略優於隨機時間區間的表現。  
- 加入 RSI 過濾器後：  
  - 平均收益率提高至 0.54%。  
  - 交易筆數減少至 62 筆，但勝率和收益提升。  

---

#### 6. 結論  
- Doji 模式在歷史回測中表現不錯，但需結合其他指標（如 RSI）來進一步優化策略。  
- 視頻作者建議觀看更多相關內容以深入了解 Candlestick 模式的性能和應用。  

---

#### 7. 其他提及點  
- 該團隊已對所有已知的 Candlestick 模式進行回測並編寫了相應的交易碼，可在其網站上購買研究報告和回測代碼。  
- 最佳的十種 Candlestick 模式表現優於「Buy and Hold」策略，投資時間僅為後者的 35%。  

---

此整理基於文章內容，涵蓋了主題、交易商品、使用指標、策略細則、回測績效和結論等主要方面，並以小節形式清晰分類。
</details>

<details>
<summary>073. EASTER Trading Strategy (Holiday Effect in The Stock Market)</summary>

[[Youtube]](https://www.youtube.com/watch?v=pL9F9DSIOVg&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理與分析

#### 主題  
本文探討了基督教節日——復活節（Easter）對美國股市交易的影響，並提出了兩種基於復活節期間的交易策略。

---

#### 交易商品  
主要研究對象為標準普爾500指數（S&P 500），這是一種廣泛用于衡量美國股市整體表現的股票市場指數。

---

#### 策略細則  

1. **Easter Strategy**  
   - **買入時機**：在復活節前一周的周五收盤時買入。  
   - **賣出時機**：持有至 Holy Thursday（耶穌受難日）收盤時賣出，共計4個交易日。  
   - **特點**：策略基於復活節期間股市的良好表現。

2. **Holy Thursday Strategy**  
   - **買入時機**：在復活節周的周三收盤時買入。  
   - **賣出時機**：次日（即Holy Thursday）收盤時賣出，僅持倉24小時。  
   - **特點**：策略簡單且執行容易。

---

#### 回測績效  

1. **Easter Strategy**  
   - **平均收益**：63年來平均每筆交易的收益率為0.77%。  
   - **近期表現（2000年後）**：平均每筆交易收益率提升至1.49%。  
   - **虧損情況**：虧損相對較小，但收益通常更為顯著。

2. **Holy Thursday Strategy**  
   - **平均收益**：63筆交易的平均每筆收益率為0.35%。  
   - **勝率**：68%。  
   - **Profit Factor（收益風險比）**：4.1，表現優良。  
   - **排名**：被列入美國年度五大最佳交易日之一。

---

#### 結論  
復活節期間的股市表現通常較為理想，兩種策略均展示了可觀的回測績效。  
- **Easter Strategy** 適合長線投資者，持倉時間較長但收益穩定。  
- **Holy Thursday Strategy** 執行簡單，適合短線交易者，勝率和收益風險比均表現出色。  

本文強調了節日效應在股市中的重要性，並鼓勵讀者探索更多交易策略以提升投資績效。
</details>

<details>
<summary>074. Closed-End Fund Strategy: Lower Risk, Higher Reward</summary>

[[Youtube]](https://www.youtube.com/watch?v=qL9gnzI5Akc&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

# 文章整理報告

## 主題  
本篇文章介紹了一種.Closed-End Fund (CEF) 的交易策略，該策略基於每日價格與淨資產價值（NAV）之間的差異進行交易，旨在通過降低市場暴露來減少最大回撤。

---

## 交易商品  
- .Closed-End Fund (CEF)，具體以Ticker Code "ETG"為例。

---

## 使用指標  
- **相對強度指數（RSI）**：策略基於2日相對強度指數的交叉信號進行交易決策。
  - 短期RSI用於評估市場超買或超賣狀態。

---

## 策略細則  
1. **進場條件**：  
   - 當2日相對強度指數（RSI）交叉跌破10時，於收盤價進場建立多頭倉位。
   
2. **出場條件**：  
   - 當2日相對強度指數（RSI）交叉突破60時，於收盤價出場平倉。

---

## 回測績效  
- **總交易次數**：212筆  
- **平均報酬率**：48%  
- **市場暴露時間**：133%（策略在市場中持有的平均時間）  
- **最大回撤**：26%  

---

## 結論  
1. 與「買進並持有」策略相比，此策略顯著降低了最大回撤（74% vs. 26%）。  
2. 策略時間效率高，僅需短暫暴露於市場即可實現較高的報酬率。  
3. 此類swing trading策略可作為風險管理的有效工具，適合追求穩定報酬的投資者。

---

## 參考資源  
- 更多類似策略可在文章提及的網站上找到。
</details>

<details>
<summary>075. These Are The Worst Stocks To Buy - Keep Away</summary>

[[Youtube]](https://www.youtube.com/watch?v=qqiONddSlOs&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
本文探討了長期投資中應避免購買的股票類型，並通過歷史數據指出某些特定股票在過去60年中未能帶來正回報。

### 2. 交易商品  
- **低市值（Small Cap）股票**：這些股票通常市場流動性較低，風險較高。  
- **高波動性（High Volatility）股票**：價格波動劇烈，難以預測。  
- **不確定商業模式的公司**：業務不穩定或前景不明朗的企業。  
- ** penny stocks（ Penny Stock 確為小額股票，價格通常低於5美元）**：價格極低且流動性差的股票。

### 3. 使用指標  
- **市值（Market Value）**：作為篩選標準之一，低市值股票表現較差。  
- **波動性（Volatility）**：高波動性與長期負收益相關。  

### 4. 策略細則  
- 避免投資於低市值、高波動性的股票。  
- 排除具有不確定商業模式的公司。  
- 減少對 penny stocks 的關注，以降低投資風險。  
- 採用「排除法」（Exclusionary Approach），通過避免劣質資產來提升整體投資組合的表現。  

### 5. 回測績效  
- 歷史數據顯示，自甘迺迪總統以來，某些股票組別（尤其是低市值、高波動性的小盤股）持續產生負收益。  
- 長期持有這些股票的投資策略並未帶來正向回報。  

### 6. 結論  
- **長期投資需謹慎**：選擇優質資產是關鍵，避免低質量或高風險的股票。  
- **排除法的重要性**：通過篩選和排除表現不佳或高風險的股票，可以提高整體投資組合的表現。  
- **風險管理**：投資者應關注波動性較高的股票，並評估其商業模式的穩定性，以降低投資風險。
</details>

<details>
<summary>076. 8 Quantitative Trading Strategies | (Backtests, Settings and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=rlSkRMmycWo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

## 文章重點整理

### 1. 主題：量化交易策略介紹

- **主題**：本文主要介紹了八種量化交易策略，並解釋了這些策略如何通過自動化系統進行交易。
- **目的**：展示量化交易的威力與潛力，鼓勵讀者嘗試自己開發和實施交易策略。

### 2. 交易商品

- **金融工具**：
  - 股票指數（如S&P 500、Nasdaq 100）
  - 長期公債ETF（如TLT）
  - 其他未明確提及的金融工具。

### 3. 使用指標

- **策略使用的技術指標**：
  - 移動平均線（MA）
  - 布林帶（Bollinger Bands）
  - 積_hopcroft
  - 言論無法進一步探討具體指標，因部分策略未公開。

### 4. 策略細則

- **主要策略**：
  1. **股息成長股戰略**：基於股利增長進行投資。
  2. **均值回歸策略**：利用價格趨勢的均值回歸特性。
  3. **價量分析**：結合價格和成交量變化。
  4. **機器學習模型**：使用數據挖掘技術預測市場走勢。
  5. **波動性捕捉**：基於波動性指標進行交易。
  6. **長期趨勢追蹤**：跟蹤主要指數的長期走勢。
  7. **季節性模式**：利用歷史數據中的季節性規律。
  8. **短期均線交叉**：基於短期移動平均線的交叉信號。

### 5. 回測績效

- **整體表現**：
  - 年回報率：整體表現穩定，部分策略年回報率高達25%。
  - 最大回撤：通常較小且短暫，顯示策略魯棒性。
  - 跑贏指數：多數策略在長時間內跑贏買後持有策略。

### 6. 結論與建議

- **結論**：
  - 量化交易是一種高效、自動化的投資方式。
  - 雖然需要一定的技術門檻，但通過系統化學習和實踐可以掌握。
  
- **建議**：
  - 初學者應該從簡單策略開始，逐步 complexities.
  - 建議使用回測平臺進行策略測試，避免依賴直覺交易。
  - 強調記錄交易日誌的重要性，用於後續策略優化。

### 7. 教育資源與鼓勵

- **教育資源**：
  - 提供三支績效優異的交易策略組合（三長三短策略）。
  - 鼓勵讀者探索更多視頻和文章以學習量化交易。

### 8. 注意事項

- **風險提示**：
  - 文章內容不構成投資建議，僅供教育參考。
  - 強調市場風險存在，需根據個人Risk tolerance進行投資。

---

## 英文摘要

This article provides an introduction to eight quantitative trading strategies, highlighting their application in automated systems. The strategies cover a range of financial instruments, including stock indices and long-term Treasury bond ETFs. Key features include the use of technical indicators such as moving averages and Bollinger Bands, along with systematic approaches like mean reversion and momentum trading. Backtesting performance shows stable returns, often exceeding buy-and-hold benchmarks, with modest drawdowns. The article concludes that quantitative trading is a powerful yet accessible approach for investors willing to learn and implement systematic strategies. It encourages readers to explore further resources and emphasizes the importance of disciplined strategy development and backtesting.
</details>

<details>
<summary>077. Stocks vs Interest Rates Trading Strategy</summary>

[[Youtube]](https://www.youtube.com/watch?v=ro4ck8Z1rYw&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章要點整理

#### 1. 主題  
- 探討債券市場波動對股票投資的影響。
- 分析債券與股票之間的關係，揭示一種基於此關係的投資策略。

#### 2. 財務理論與債券特性  
- 利率直接影響債券和股票的價值。  
  - **低利率環境**：促使投資者轉向風險資產（如股票），因其提供較高回報。  
  - **高利率環境**：降低風險資產的吸引力，因持有債券的固定收益相對更有競爭力。  
- 債券特性：  
  - 固定票息率，每年支付，直至到期日。  
  - 利率上漲時，債券價格下跌以反映新利率水平。  
  - 債券 perceived as less risky than stocks due to seniority in bankruptcy claims.  

#### 3. 股票與債券的逆周期關係  
- 假設：上升的債市（即債券價格上漲）導致利率下降，使股票更具吸引力。  
- 需要驗證此假說是否成立。

#### 4. 投資策略細則  
- 使用Spy和TLT兩個ETF進行交易：  
  - **Spy**：跟蹤標普500指數（S&P 500）。  
  - **TLT**：跟蹈美國20年期公債。  
- 操作規則：  
  - 當TLT的收盤價突破其n日移動平均線（MA）時，買入Spy並持有直至賣出信號出現。  
  - 當TLT的收盤價跌破其n日移動平均線時，賣出Spy並退出市場，直到再次觸發買入信號。  

#### 5. 回測結果  
- 測試不同移動平均天數（5到100天，間隔5天），共20次回測。  
- **重要發現**：  
  - 當TLT價格高於其移動平均線時，Spy的平均收益較高且穩定。  
  - 策略的有效性在不同移動平均天數下均表現一致。  

#### 6. 具體案例分析（15日移動平均）  
- **期間**：2003年至今。  
- **績效指標**：  
  - Spy年化收益率：9.8%。  
  - 策略年化收益率：8.85%，投資天數佔比僅54%。  
  - 平均每筆交易收益：0.51%。  
  - 最大回撤：31%。  

#### 7. 反向策略的結果  
- 若將買賣信號反轉（即債券下跌時買入股票），績效顯著惡化，具體內容參見其他影片。

#### 8. 結論  
- 債市上漲期間，股市表現強勁。  
- 使用TLT的移動平均線作為買賣信號，可有效捕捉股票市場的收益，降低風險敞口。  
- 推薦結合此策略與其他投資方法以優化整體績效。  

#### 9. 其他提示  
- 視頻鼓勵訂閱頻道並訪問網站以獲取更多策略和資源。
</details>

<details>
<summary>078. OPEX Trading Strategy (Backtest &amp; Results)</summary>

[[Youtube]](https://www.youtube.com/watch?v=sDOfLm6Y6G4&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：Options Expiration Week Effect (Opex Week)

#### 1. 主題  
- 探討期權到期周（Opex Week）對金融市場的影響。  
- 展示三種基於Opex Week的交易策略及其表現。

#### 2. 交易商品  
- 標普500指數（S&P 500），以ETFspy作為 proxies。  
- 其他防禦型股票：XLV（醫療保健）和XLU（公用事業）。  

#### 3. 使用指標  
- 無具體技術指標，策略基於市場行為和Opex Week的特性。  

#### 4. 策略細則  
##### (1) 第一種策略  
- 在Opex周的周一開盤買入spy，於Opex日收盤賣出。  
- 投資時間佔比約18%，平均每筆交易持續不到5天。  

##### (2) 第二種策略（exclusive for paying members）  
- 僅在Opex周的周一開盤買入特定防禦型股票（XLV和XLU），於Opex日收盤賣出。  
- 年化回報4.5%，投資時間佔比少於10%。  

##### (3) 第三種策略  
- 在Opex日開盤做空spy，於當日收盤迴補倉位。  
- 平均收益0.16%，可進一步優化以提高收益。  

#### 5. 回測績效  
##### (1) 第一種策略  
- 資本翻倍時間：約2年（CAGR為3.1%）。  
- 平均每周收益：0.3%。  

##### (2) 第二種策略  
- 年化回報：4.5%。  
- 平均每筆交易收益：0.72%。  

##### (3) 第三種策略  
- 平均收益：0.16%。  

#### 6. 結論  
- Opex Week存在顯著的市場效應，可作為交易機會。  
- 這種效應並非獨立策略，但與其他參數結合使用時能帶來利潤。  
- Opex日通常對多頭不利，提供空頭交易的機會。  
- 建議投資者深入理解Opex機制及市場行為以優化交易策略。  

---

### 關鍵術語  
1. **Options Expiration Week (Opex Week)**：期權到期周，指每月第三個星期五（美國）及其前後的一周，是大量期權合約到期的時期。  
2. **Compound Annual Growth Rate (CAGR)**：年化複合增長率，衡量投資回報的長期增長率。  
3. **Pen Risk**：樁 риск，指在期權到期時，標的資產價格接近行權價時的不確定性風險。  
4. **Quadruple Witching Day**：四重witching day，指同時到期的股票期權、指數期權、期貨和外匯合約的日期（通常為每季度末）。
</details>

<details>
<summary>079. Heiken Ashi Candlestick Trading Strategy: (Backtest + Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=sG6Gsxf0I5o&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 一、主題
- 探討Hikanashi（平均線圖）作為一種源自日本的圖表技術，在現代交易策略中的應用及其盈利能力。

### 二、交易商品
- Hikanashi是一種基於價格數據的圖表表示方法，用於識別趨勢或 consolidation 階段，而非直接代表實際價格。

### 三、使用指標
- **Hikanashi**：一種通過平滑處理OHLC（開、高、低、收）值來消除價格噪聲的趨勢跟蹤指標。
- **傳統日本蠟燭圖**：作為補充工具，用於輔助交易決策。

### 四、策略細則
1. **買入條件**：
   - 當Hikanashi的收盤價突破其開盤價時買入。
   
2. **賣出條件**：
   - 當Hikanashi的收盤價跌破其開盤價時賣出。

3. **時間框架**：
   - 最佳適用時間框架為長期（如月線），不適合短期交易（如日內交易或波段交易）。

4. **計算方式**：
   - Hikanashi通過計算當前和前一期的價格平均值來生成新的開盤價和收盤價，從而消除價格波動的噪聲。

### 五、回測績效
1. **測試對象**：S&P 500指數。
2. **時間範圍**：1960年至今（月度數據）。
3. **績效指標**：
   - 年化收益：4.77%。
   - 最大回撤：30%。
   - 勝率：低，符合趨勢跟蹤策略的特性。

### 六、結論
- Hikanashi作為圖表技術，在消除價格噪聲和識別趨勢方面具有優勢，但其並非直接反映實際價格，因此不能直接用於交易。
- 儘管Hikanashi在長周期（如月線）上的表現優於Buy and Hold策略的最大回撤，但在收益上略遜於後者。
- 建議交易者在使用Hikanashi制定策略前，進行充分的歷史數據測試。
</details>

<details>
<summary>080. Sugar Futures TRADING STRATEGY (Backtest and Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=sH70Ldu5YOQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 一、主題  
- 文章主要探討糖（Sugar）作為重要商品之一，在日常消費中對健康和財務造成的潛在影響。  
- 強調糖交易的風險及其對個人和金融市場的可能危害。  

---

### 二、交易商品  
- ** commodities**: 糖（Sugar）。  
- 糖被廣泛消費，但過量攝取可能導致糖尿病等健康問題。  

---

### 三、使用指標  
- **350-Day Moving Average (DMA)**: 用於判斷價格趨勢。  
- **7-Day ATR (Average True Range)**: 用於衡量市場波動性，作為買賣信號的輔助指標。  

---

### 四、策略細則  
1. **買入條件**:  
   - 當價格突破350天移動平均線（DMA）加上7天ATR時，買入。  
2. **賣出條件**:  
   - 當價格跌破350天移動平均線（DMA）減去7天ATR時，賣出。  

---

### 五、回測績效  
- 文章提及該策略的 equity curve（權益曲線），但未提供具體數值或詳細分析。  
- 結果似乎不符合作者的理想交易表現。  

---

### 六、結論  
1. **警示信息**:  
   - 過多糖分攝入可能導致健康問題，類似地，糖交易可能對財務造成重大風險。  
2. **交易策略建議**:  
   - 作者本人未嘗試任何糖相關的交易策略。  
3. **推薦資源**:  
   - 文章末尾提供了一個網址（quantifiedstrategies.com），鼓勵讀者進一步研究和了解更多信息。
</details>

<details>
<summary>081. A SIMPLE Trading Strategy With A 91.03% Win Rate</summary>

[[Youtube]](https://www.youtube.com/watch?v=shgOIrJdj8s&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 本文整理重點

#### 主題  
- 文章介紹了一種名為「Triple RSI Trading Strategy」的交易策略，其勝率高達91%。  
- 策略旨在利用長期上升趨勢中的短期回撤（pullbacks）進行交易。

---

#### 交易商品  
- 使用標普500指數（S&P 500）作為-proxy，並使用SPY ETF（Spider Shares）作為代表。

---

#### 使用指標  
1. **相對強度指數（RSI）**：用於衡量短期過買或過賣狀態。  
   - 使用5日RSI指標。  
2. **200日移動平均線（MA）**：用作趨勢判斷和濾鏡，確保交易在上升趨勢中進行。

---

#### 策略細則  
1. **進場條件**：  
   - 5日RSI低於30。  
   - 5日RSI連續三天下跌。  
   - 5日RSI在63個交易日前曾經低於30。  
   - 收盤價高於200日移動平均線（MA）。  

2. **出場條件**：  
   - 5日RSI突破50。

3. **濾鏡**：  
   - 確保市場處於上升趨勢，200日MA用作濾鏡。

---

#### 回測績效  
1. **交易次數**：  
   - 自1993年以來共計78筆交易。  

2. **平均收益**：  
   - 每筆交易平均收益率為1.4%。  

3. **勝率**：  
   - 91%的交易為盈利交易。  

4. **持有時間**：  
   - 平均每筆交易持有時間為6天。

---

#### 結論  
- 文章認為該策略在回測期間表現良好，勝率高且平均收益率穩定。  
- 推薦進一步探索網站（quantifiedstrategies.com）上的其他交易策略。

---

#### 存疑部分或缺失  
1. **進場條件**：  
   - 5日RSI低於30且連續三天下跌的具體計算方式未明確。  

2. **數據來源**：  
   - 文章未提及回測數據的具體來源和時間範圍。  

3. **風險管理**：  
   - 策略中未提到風險管理和損失控制機制。  

4. **市場適用性**：  
   - 該策略主要針對美國股市，其他市場的表現未提及。
</details>

<details>
<summary>082. Coppock Curve Trading Strategy (Backtest &amp; Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=tnUZLLUGpo8&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 介紹Copic曲線策略（Copic Curve Strategy），一種已存在超過60年的投資策略。

#### 使用指標  
- **Copic 曲線**：基於 economist Copic 在1960年代提出的指標。  
- 計算方式：使用11和14兩個速率變化值的加權移動平均，代表市場週期的早期上漲階段和晚期上漲階段。

#### 策略細則  
1. **買入條件**：Copic曲線 crossover 上穿其10月移動平均線。  
2. **賣出條件**：Copic曲線 crossover 下穿其10月移動平均線。  

#### 回測績效  
- **研究時間範圍**：1960年至2023年，對S&P 500指數進行回測。  
- **平均年化回報率**：6.11%，略低於S&P 500的7.03%。  
- **最大回撤**：Copic曲線策略為3.16%，顯著低於S&P 500的52.56%。  
- **風險調整後回報率**：Copic曲線策略為8.29%，高於S&P 500的7.03%。

#### 結論  
- Copic曲線策略是一種簡單且有效的投資策略，能夠幫助投資者在股票市場中賺取利潤並降低風險。  
- 對於尋找長期投資策略的投資者來說，Copic曲線策略值得進一步研究和考慮。
</details>

<details>
<summary>083. Small Cap Effect Strategy: Outperform 99% Of Investors</summary>

[[Youtube]](https://www.youtube.com/watch?v=vwKX101clTU&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 本文重點整理

#### 主題  
- 小盤股效應（Small Cap Effect），又稱為小盤股溢酬（Small Cap Premium）。  
- 解釋了小型公司長期表現優於大型公司的現象。  

#### 相關理論與模型  
- 與Fama的三因子模型密切相關，用以解釋股票回報的多種因素。  

#### 交易商品  
- 小型股（Small Cap Stocks）。  

#### 使用指標  
- 公司規模：衡量公司的市值大小。  
- 值股與成長股：質值股（Value Stocks） vs. 成長股（Growth Stocks）。  
- 質量因子：例如「Robust」指標，用於評估公司質量。  

#### 策略細則  
1. 避開波動性過高的股票，以降低風險。  
2. 長期持有小型 stocks 有望實現較高回報。  
3. 小型價值股（Small Cap Value Stocks）表現優於小型成長股（Small Cap Growth Stocks）。  

#### 回測績效  
1. 自1963年以來，小型股整體表現超越大型股。  
2. 1940年代初投資小型股，$100的本金到現在將大幅增值。  
3. 質量因子在小型股中效果顯著：1965年投入$100，截至今天價值約為$276,000。  

#### 結論  
- 長期投資於小型股和高質量股票可帶來穩定且豐厚的回報。  
- 投資策略應結合規模、價值與質量等多重因素以提升效果。
</details>

<details>
<summary>084. Best Bitcoin Trading Strategy (Rules &amp; Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=xSpWak84AjA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章整理：比特幣動量交易策略

#### 1. 主題
- **動量交易**：一種基於價格趨勢強度的交易策略。
- **Bitcoin市場**：本文專注於比特幣市場的動量交易。

#### 2. 交易商品
- **Bitcoin**：文章圍繞比特幣的交易策略展開討論。

#### 3. 使用指標
- **25天最高價（High of Close）**：用作動量分析的關鍵指標。
- **收盤價（Close Price）**：作為價格趨勢的主要觀察對象。

#### 4. 策略細則
1. **買入條件**：
   - 當收盤價上穿25天最高價時，做多（.buy at close）。
   
2. **賣出條件**：
   - 當收盤價下穿25天最高價時，做空（.sell at close）。

#### 5. 回測績效
- **交易次數**：累計179筆交易。
- **平均收益**：每筆交易平均收益率為2.35%。
- **年化複合成長率**：達55.7%，表現亮眼。
- **最大回撤**：僅23%，風險相對可控。

#### 6. 結論
- **策略有效性**：動量交易在比特幣市場中顯示出顯著的盈利能力。
- **建議**：トレーダーが recent price trends を活用し、本文で説明した規則に従って取引を行うことで利益を上げることが可能である。

---

以上整理涵蓋了文章的核心內容，結構清晰，條理分明。
</details>

<details>
<summary>085. Crude Oil Trading Strategies (Backtest &amp; Settings)</summary>

[[Youtube]](https://www.youtube.com/watch?v=xkEKJ7GJnt0&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
- 探討 crude oil（原油）作為交易商品的潛力及其複雜的市場特性。  
- 強調開發和測試一個有效的原油交易策略的重要性。

### 2. 交易商品  
- Crude Oil Futures Contract：文中以原油期貨合約為例進行分析。

### 3. 使用指標  
- **25-day Average of the daily High minus the Low**（25日平均價差）：用於計算價格波動範圍。  

### 4. 策略細則  
- **規則一**：計算過去25個交易日的高低價差平均值。  
- **規則二**：交易時間限定為每周的星期二或星期四。  
- **規則三**：今日收盤價必須低於昨日收盤價減去規則一所計算的範圍。  
- **規則四**：於次一交易日的收盤時賣出。

### 5. 回測績效  
- **總交易次數**：341次。  
- **平均收益/交易**：0.25單位（具體貨幣或合約單位未明確）。  
- **勝率**：58%（略高於隨機概率）。  
- **平均盈利交易大於平均虧損交易**：表明策略在長期中具有盈利能力。

### 6. 結論  
- Crude Oil 是一個具有高潛力的交易資產，但其市場複雜且受多種因素影響。  
- 成功的關鍵在於開發經過充分測試的交易策略，以避免 costly mistakes。  
- Back Testing（回測）是評估策略有效性的關鍵步驟，能夠揭示策略的優缺點並進行必要的調整。  
- 通過歷史數據分析優化策略，可提升交易決策的 informedness 和 profitability。
</details>

<details>
<summary>086. SECTOR ROTATION Trading Strategy (Backtest And Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=yOvQBxyqX2E&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 本文介紹了**量化策略（Quantified Strategies）**的**板塊輪動交易策略（Sector Rotation Trading Strategy）**，並強調其為一種基於數據驅動、經過驗證且能產生穩定收益的交易方法。

---

#### 交易商品  
1. **標普500指數（S&P 500）**：使用ETF Spy進行交易。  
2. **美國長期公債（Long-Term Bonds）**：使用ETF TLT進行交易。  
3. **國際成熟市場股票（International Developed Stocks）**：使用ETF EFA進行交易。  
4. **新興市場股票（Emerging Market Stocks）**：使用ETF EEM進行交易。

---

#### 使用指標  
- **-relative strength（相對強度）**：基於板塊過去一個月的價格表現來確定表現最佳的板塊。

---

#### 策略細則  
1. 每個月計算四個板塊的相對強度，選擇表現最好的板塊。  
2. 舉行相應的ETF（如Spy、TLT、EFA、EEM）進行交易。  
3. 保持該頭寸一個月，然後重複上述步驟，滾動至新的最佳板塊。  
4. 通過數據分析而非市場預測來降低情緒化交易的影響。

---

#### 回測績效  
- 策略經過歷史數據的嚴格回測（Back Testing），結果顯示其表現良好且具備穩定性。  
- 該策略被證實是一種有效的、數據驅動的交易方法。

---

#### 結論  
1. **板塊輪動交易策略**是一種基於數據、經過驗證且能產生穩定收益的交易方法，值得考慮。  
2. 量化策略強調_proof（證明）的重要性，並相信回測結果可以驗證策略的有效性。  

---

#### 增值信息  
- 觀看者可能對其他高利潤策略感興趣，例如文中提及的一個「範圍交易策略」（Range Trading Strategy）。
</details>

<details>
<summary>087. CCI Trading Strategy (Backtest &amp; Trading Rules)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zFldiNwEsKo&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
- 強調介紹 **CCI指標**（Commodity Channel Index），一種不太為人所熟知的技術指標。  
- 探討CCI指標在交易策略中的應用，特別是用於趨勢反轉的判斷。  

#### 交易商品  
- 研究對象：S&P 500指數（Standard & Poor's 500 Index）。  

#### 使用指標  
- **CCI指標**：衡量證券當前價格水平相對於某一平均價格水平的偏移程度，用於識別超買或超賣狀態。  

#### 策略細則  
1. **CCI計算方式**：基於一定回顧期（look back period）的平均價格水平，公式複雜，建議交由交易平臺自動計算。  
2. **最佳參數設定**：通過後測試，發現使用9天的中等回顧期效果最為理想。  
3. **交易信號**：  
   - **買進條件**：CCI指標跌破-90。  
   - **.sell條件**：今日收盤價突破昨日最高價。  

#### 回測績效  
1. **歷史表現**：  
   - 最大回撤（Maximum Drawdown）*為23%。  
   - 1993年，本金10萬美元可增長至100萬美元，收益率達10倍。  
2. **交易次數**：累計464筆交易。  

#### 結論  
- CCI指標在S&P 500指數上的應用表現出色，具備穩健的風險收益比。  
- 儘管交易次數較多，但策略整體績效可觀，適合用於趨勢交易策略的制定與優化。  

*Note: The maximum drawdown is modest at 23%.
</details>

<details>
<summary>088. Stocks During War And Conflict (Profit from War Stocks)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zJaolkzOkWQ&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 文章重點整理

#### 主題  
本文探討戰爭對股票市場的影響，分析歷史上重大衝突期間及之後股市的表現，並提出投資者在面對戰爭時應採取的策略。

#### 交易商品  
- 股票市場（以S&P 500為例）  
- 黃金  
- 石油  
- 固定收益資產（債券）  

#### 使用指標  
- 標普500指數（S&P 500）表現  
- 防禦支出與股票市場波動性的關係  
- 市場 volatility（波動性）  

#### 策略細則  
1. **戰爭期間的股市表現**：  
   - 歷史上，重大衝突爆發後，股市的最大跌幅通常不超過20%。  
   - 戰爭可能刺激政府支出和經濟活動，從而對股市產生積極影響。  
   - 戰爭往往在市場預期之中，因此其實際爆發並未引發顯著的恐慌或波動。  

2. **市場反應的時間性**：  
   - 在戰爭爆發前，股市通常已出現下跌，反映了市場的預期。  
   - 例如，在珍珠港事件前，美國股市已下跌，而在戰後幾周內迅速反彈， Dow Jones指數在戰爭結束前上漲超過60%。  

3. **波動性的變化**：  
   - 戰爭期間市場波動性通常下降，表現出反直覺的穩定性。  
   - 防禦支出增加與股市波動性降低呈負相關關係。  

4. **地域因素的影響**：  
   - 在本土發生的戰爭對實體經濟和股市造成毀滅性影響。  
   - 例如，二戰後的德國、俄羅斯在1917年至1991年期間的股市表現不佳。  

5. **其他資產類別的反應**：  
   - 黃金價格在戰爭消息傳出時通常上漲，但隨後可能回落。  
   - 石油和債券等其他資產的表現因具體情況而異。  

#### 回測績效  
- 歷史數據顯示，股市在戰爭期間的波動性較低且表現相對穩定。  
- 戰爭結束後，股市往往出現反彈，如珍珠港事件後Dow Jones指數上漲超過60%。  

#### 結論  
1. **投資者應對策略**：  
   - 若本地市場未直接捲入衝突，可遵循「買預期，賣事實」的原則（即在戰爭傳聞時買入，在戰爭結束時賣出）。  
   - 戰爭通常已被市場消化，因此其爆發後股市的波動性有限。  

2. **風險提示**：  
   - 本土戰爭對經濟和股市有嚴重破壞作用，需謹慎對待。  
   - 不同資產類別的反應各異，投資者應綜合考慮多種因素。  

3. **總體建議**：  
   - 在和平時期進行多元化投資以分散風險。  
   - 戰爭期間關注防禦性行業（如國防、公用事業等）的表現。
</details>

<details>
<summary>089. Relative Vigor Index (RVI) Strategy (Backtest)</summary>

[[Youtube]](https://www.youtube.com/watch?v=zLFujYKDyGA&list=PLHFlSdhbIZ6TEeEg4cHQ-3888yUnHZs5v)

### 1. 主題  
- **Relative Vigor Index (RVI)**：介紹了一種罕見使用的技術指標——相對活力指數（RVI），並探討其在交易策略中的應用潛力。

### 2. 使用的交易商品  
- **GLD ETF**：回測研究中使用了追蹤黃金價格的ETF（GLD）作為交易標的。

### 3. 技術指標——相對活力指數 (RVI)  
- **定義**：RVI是一種技術指標，用於衡量價格運動的動量，通過比較收盤價與交易範圍來計算。  
- **構成部分**：包括一個名為「信號線」（signal line）的簡單移動平均線（Simple Moving Average, SMA）。  
- **原理**：在上漲趨勢中，價格通常會以高於開盤價的形式收盤；而在下跌趨勢中，則以低於開盤價的形式收盤。RVI基於此特點來評估市場力量。

### 4. RVI 的計算步驟  
- **分子（Numerator）**：衡量價格的動量或活力。  
- **分母（Denominator）**：通常為交易範圍（high-low）。  
- **RVI 計算**：分子除以分母，得到相對 vigor 指數。  
- **信號線計算**：使用簡單移動平均線（SMA）來平滑 RVI 結果。

### 5. RVI 交易策略細則  
- **買入條件**：  
  - RVI 上穿其信號線。  
  - 綠iday 指標（RSI）的5日均值需低於50。  

- **賣出條件**：  
  - 信號線上穿 RVI。  

### 6. 回測績效  
- **交易結果**：  
  - 平均每筆交易收益為0.44%。  
  - 獲利率（Win Rate）為51%，屬於中等水準。  
  - 獲利交易的平均規模遠超過虧損交易，表明勝者大於敗者的特點。  

### 7. 策略的有效性與局限性  
- **適用性**：策略在 GLD ETF 上表現良好，但對於其他資產（如標普500指數或債券）效果不佳。  
- **結論**：不同資產的價格運動特性不同，因此策略的效果可能因市場而異。

### 8. 結論  
- **研究意義**：展示了 RVI 指標在特定市場條件下的潛力，但仍需進一步驗證其對其他資產的有效性。  
- **建議**：投資者可根據自身交易目標和市場特性，調整策略參數或指標組合。
</details>

