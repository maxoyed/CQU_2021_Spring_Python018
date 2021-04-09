### 1. 小费、税和消费总额

#### 问题描述

请编写一个程序来计算餐厅某次点餐的消费总额。程序要求用户输入点餐的费用，然后计算税率为10%的小费和税率为7%的消费税。最后显示各项金额和消费总额。小数点后保留4位小数。

#### 输入形式

点餐消费总额
#### 输出形式

The consumption is 【小数点后保留4位小数】, the tip is 【小数点后保留4位小数】, the tax is 【小数点后保留4位小数】,so the total consumption is 【小数点后保留4位小数】

#### 样例输入

```bash
100
```

#### 样例输出

```bash
The consumption is 100.0000, the tip is 10.0000, the tax is 7.0000,so the total consumption is 117.0000
```

```python
consumption=eval(input())
# blank start
# blank end
# blank start
# blank end

total=consumption+tip+tax
print("The  consumption  is  %.4f,  the  tip  is  %.4f,  the  tax  is  %.4f,so  the  total  consumption  is  %.4f"%(consumption,tip,tax,total))
```
