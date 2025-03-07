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
