### 2.年龄分类器

#### 问题描述

请编写一个程序，根据用户输入的一个人的年龄，程序将判断说明这个人是婴儿、儿童、青年人或者成年人。

分类的原则如下：

1. 如果此人是1岁甚至更小，则为婴儿(infant)

2. 如果此人大于1岁，但小于13岁，则为儿童(child)

3. 如果此人至少13岁，但小于20岁，则为青年人(teenager)

4. 如果此人至少20岁，则为成年人(adult)

如果输入的数小于等于0，则输出“Error”


#### 输入形式

整数（表示年龄）

#### 输出形式

infant  or child  or  teenager  or adult  or Error

#### 样例输入

```bash
18
```

#### 样例输出

```bash
teenager
```

#### 样例说明

输入不需要提示

```python
age=#blank

if  #blank start
        # blank end
        print("infant")
elif  1<age<13:
        print("child")
elif  13<=age<20:
        print("teenager")
elif  age>=20:
        print("adult")
else:
        print("Error")
```
