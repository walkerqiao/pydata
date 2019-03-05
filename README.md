Python数据分析学习整理
---------


## pandas
[pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html)是一个Python包，提供快速、灵活和丰富的数据结构, 旨在轻松直观的处理关系型(relational)数据或标记型(labeled)数据。它的目标是成为在Python中进行实际的、真实的数据分析的基本高层构建块。此外，它还有更广泛的目标，即成为任何语言中最强大和最灵活的开源数据分析/操作工具。它已经很好的朝这个目标前进了。

pandas特别适合多种不同类型的数据:
- 具有异构类型列的表格数据，如在SQL表或Excel电子表格中的数据。
- 有序和无序(不一定是固定频率的)时间序列数据。
- 带有行和列标签的任意矩阵数据(同种类型或异构数据)。
- 任何其他形式的观测/统计数据集。数据实际上根本不需要标记就可以放入pandas数据结构中。

pandas的两个基本数据结构是Series(一维的)和数据帧(二维的)， 处理绝大多数金融、统计、社会科学和许多工程领域的典型用例。对于R语言用户来说，DataFrame提供了R语言data.frame所提供的一切，甚至更多。pandas是建立在numpy之上的，旨在与许多其他第三方库很好的集成在科学计算环境中。

以下是pandas能够做得很好的一些事情:
- 轻松的处理浮点和非浮点数据中缺失的数据(以NaN表示)。
- 大小可变: DataFrame以及更高维度的对象中可以随意插入和删除列。
- 自动化和显示数据对齐: 对象可以显示的与标签集对齐，或者用户可以忽略这些标签，让Series, DataFrame等等自动在计算中为你对齐。
- 功能强大、灵活的分组功能，可对数据集执行拆分、应用、合并操作(split-apply-combine operation), 用于聚合和转换数据。
- 使得它很容易将其它Python语言和NumPy中不规则、索引不同的数据转换为DataFrame对象。
- 基于智能标签的切片、复杂索引(fancy indexing奇特索引)以及大型数据集的子集。
- 直观的合并和连接数据集。
- 灵活的重塑数据集和旋转数据集(reshape and pivote)。
- 轴的层次标签(每个刻度可以有多个标签)。
- 强大的I/O工具，可以从单纯的文件(csv, 以及各种分割符分割内容的), excel文件, 数据库中加载数据，以及向超高速HDF5个市中保存和加载数据。
- 时间序列的特定功能: 日期范围生成和频率转换、移动窗口统计、移动窗口线性回归、日期前移和滞后等等。

其中很多原则都是为了解决使用其它语言/科学研究环境时经常遇到的缺点。对于数据科学家来说，处理数据通常分为多个阶段: 数据标准化(munging)、数据清洗、数据分析建模、让后将分析结果组织成适合绘图或表格显示的形式。pandas是完成这些所有任务的理想工具。

其他一些注意事项:
- pandas很高效。很多低级的算法位已经在cpython代码中进行了广泛的调整。然而，和其他一般化的所有工具一样，通常都会牺牲性能(sacrifices performance)。因此，如果将重点放在应用的单个特性上，可能会构建出一个更加高效的专用工具。

pandas是statsmodels的依赖项，它是Python统计计算生态系统的重要组成部分。

pandas在生产中广泛的应用于金融应用。

数据结构:

1. Series: 1维标记同类型数组。(1D labeled homogeneously-typed array).
2. DataFrame: 一般的二维标签、大小可变的表格结构，带有潜在的异构类型的列。(General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column
).

### 为什么使用多种数据结构?
考虑pandas数据结构的最佳方式是它作为低维数据的灵活容器。例如，DataFrame是Series的容器，Series是标量的容器。


> 标量(Scalar): 只有大小没有方向的量。向量(Vector): 既有大小，还有方向的量。我们希望能够以字典的形式向这些容器插入和移除对象。

此外，我们希望公共API函数的合理默认行为考虑到时间序列和横切面数据集合的典型方向。当使用ndarray存储2维和3维数据时，用户在编写函数时需要考虑数据集的方向；轴被认为是或多或少是等效的(除非C或Fortran连续性对性能有影响)。在pandas中，轴的作用赋予数据更多的语义意义。也就是说，对于特定的数据集，可能有一种正确的方法来确定数据的方向。因此，目标是减少编写下游函数中的数据转换所需的脑力劳动。

例如，对于表格数据(DataFrame)，考虑索引(行)和列(而不是0和1轴)在语义上更有帮助。通过DataFrame的列进行迭代，从而产生更可读的代码:
```
for col in df.columns:
    series = df[col]
    # do something with series
```

### 数据可变性和复制
所有的pandas数据接哦股都是值可变的(它们包含的值是可以更改的)，但是大小不一定是可以改变的。不能更改Series的长度，但例如，可以将列插入到DataFrame中。但是，绝大多数方法都会生成新的对象，并且不会影响输入数据。一般来说，我们喜欢在合理的情况下保持不变。


## pandas.DataFrame

### 方法介绍

#### 1. DataFrame.abs()
该方法返回Series/DataFrame每个元素的绝对值。
> 注意: 对于复数输入，1.2 + 1j, 绝对值是√a2+b2。



#### 2. DataFrame.

## 术语
- 移动窗口统计: moving window statistics
- 移动窗口线性回归: moving window linear regressions
- 日期前移和滞后: date shifting and lagging
