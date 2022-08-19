# li jia hao
# 时间：2022/8/18 15:36
#异常值检测
import pandas as pd
import matplotlib.pyplot as plt

pay_ratio = pd.read_excel('D:\数模\\2021赛题\E\附件1.xlsx')

# 绘制单条折线图，并在折线图的基础上添加点图

plt.plot(pay_ratio.No, # x轴数据

pay_ratio.data, # y轴数据

linestyle = '-', # 设置折线类型

linewidth = 2, # 设置线条宽度

color = 'steelblue', # 设置折线颜色

marker = 'o', # 往折线图中添加圆点

markersize = 4, # 设置点的大小

markeredgecolor='black', # 设置点的边框色

markerfacecolor='black') # 设置点的填充色

# 显示图形

plt.show()
# 添加上下界的水平参考线(便于判断异常点，如下判断极端异常点，只需将2改为3)

plt.axhline(y = pay_ratio.data.mean() - 2* pay_ratio.data.std(), linestyle = '--', color = 'gray')

plt.axhline(y = pay_ratio.data.mean() + 2* pay_ratio.data.std(), linestyle = '--', color = 'gray')

outlier_ll = pay_ratio.data.mean() - 2* pay_ratio.data.std()

outlier_ul = pay_ratio.data.mean() + 2* pay_ratio.data.std()


# 寻找异常点

pay_ratio.loc[(pay_ratio.data > outlier_ul) | (pay_ratio.data<outlier_ll)]
