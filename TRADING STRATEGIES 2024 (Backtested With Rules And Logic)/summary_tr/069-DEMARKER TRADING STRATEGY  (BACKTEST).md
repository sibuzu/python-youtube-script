交易策略涉及使用市场指标来识别过分买卖的水平。 优化间谍后，确定了最佳参数：5天的回顾期为5％，卖出阈值为80％。 但是，这种初始方法导致了大量的下降。 为了提高性能，进行了两个修改：

1. **出售状况** ：而不是仅仅依靠指标达到80％，而是关闭交易，当时交易已关闭：
   - The close crosses above yesterday's high (indicating strength).
   -关闭量低于昨天的低点（表明弱点）。

2. **趋势线检查** ：添加了一个额外的条件，即根据趋势线以上还是低于趋势线的价格下跌或关闭交易。

股票曲线表明，这些修改减少了缩减并提高了整体盈利能力，从而实现了更强大的策略。 最终的方法是在指标达到5％并在与价格强度和趋势线路中断有关的指定条件下出售时购买。