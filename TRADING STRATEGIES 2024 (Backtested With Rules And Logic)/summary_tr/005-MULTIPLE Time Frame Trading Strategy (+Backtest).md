所描述的交易策略是 **多时间交易策略** 旨在在短期撤回期间进入交易时利用长期趋势。 这是一个简明的摘要：

### 关键组件：
1. **长期趋势过滤器** ：关闭必须高于250天前的关闭。
   - This ensures that the asset is in an uptrend over the long term.

2. **中间趋势过滤器** ：闭合必须高于22天前的关闭。
   - This confirms that the asset is trending upward on a medium-term basis.

3. **短期回调条目** ：今天的结束必须是封闭的三天低点。
   - This means entering the trade when the price pulls back to a short-term support level.

4. **退出规则** ：当收盘价高于昨天的收盘价时，卖出。
   - This exit rule aims to lock in profits as soon as the price moves upward from the entry point.

### 例子：
该策略应用于 **XLP ETF**，跟踪消费者主食，并取得以下结果：

- **交易数量** ：316
- **平均每次交易** ：0.28％
- **获胜率** ：73％
- **最大减收** ：-10％
- **利润因子** ：2

### 策略评估：
该策略表现出合理的性能，并具有不错的获胜率和利润率。 但是，每次交易的平均增长相对较低，这可能表明该策略依赖于频繁的小胜利而不是偶尔的大收益。

### 结论：
该策略结合了多个时间范围，以使条目与长期趋势保持一致，同时使用短期回调进行条目。 它似乎适合XLP ETF，但可能需要对其他资产和市场状况进行测试。 有关更多详细信息，您可以参考来源或联系创建者。