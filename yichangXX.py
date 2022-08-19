# li jia hao
# 时间：2022/8/18 19:43
# 导入第三方模块

import pandas as pd

import matplotlib.pyplot as plt

# 导入数据

sunspots = pd.read_excel(r'D:\数模\\2021赛题\E\附件1.xlsx')

# 绘制箱线图(1.5倍的四分位差，如需绘制3倍的四分位差，只需调整whis参数)

plt.boxplot(x = sunspots.data, # 指定绘制箱线图的数据

whis = 1.5, # 指定1.5倍的四分位差

widths = 0.7, # 指定箱线图的宽度为0.8

patch_artist = True, # 指定需要填充箱体颜色

showmeans = True, # 指定需要显示均值

boxprops = {'facecolor':'steelblue'}, # 指定箱体的填充色为铁蓝色

# 指定异常点的填充色、边框色和大小

flierprops = {'markerfacecolor':'red', 'markeredgecolor':'red', 'markersize':4},

# 指定均值点的标记符号(菱形)、填充色和大小

meanprops = {'marker':'D','markerfacecolor':'black', 'markersize':4},

medianprops = {'linestyle':'--','color':'orange'}, # 指定中位数的标记符号(虚线)和颜色

labels = [''] # 去除箱线图的x轴刻度值

)

# 显示图形

plt.show()

Q1 = sunspots.data.quantile(q = 0.25)

Q3 = sunspots.data.quantile(q = 0.75)

# 基于1.5倍的四分位差计算上下须对应的值

low_whisker = Q1 - 1.5*(Q3 - Q1)

up_whisker = Q3 + 1.5*(Q3 - Q1)

# 寻找异常点

sunspots.data[(sunspots.data > up_whisker) | (sunspots.data<low_whisker)]