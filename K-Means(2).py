# li jia hao
# 时间：2022/8/20 19:49
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from sklearn.cluster import KMeans
# 导入
import pandas as pd

path = r'D:\数模\2021赛题\B/附件2.xlsx'

data = pd.read_excel(path, header=0)

data1 = data.values[1:10, 1:3]
# 平均学分绩
x = data.values[1:10, 1]
# 面向对象成绩
y = data.values[1:10, 2]

# 这里已经知道了分4类，其他分类这里的参数需要调试
model = KMeans(n_clusters=3)

# 训练模型
model.fit(data1)

# 预测全部203条数据
all_predictions = model.predict(data1)
# print(all_predictions)
# 将名字与类别转化成字典进行一一对应
# 全局字典
a = {}


def one():
    aa = 0
    bb = 0
    cc = 0
    for i in range(len(all_predictions)):
        # 循环给字典赋值
        a[data.values[i, 0]] = all_predictions[i]
        if all_predictions[i] == 0:
            aa += 1
        if all_predictions[i] == 1:
            bb += 1
        if all_predictions[i] == 2:
            cc += 1
    # print(a)
    aa1 = aa / len(all_predictions)
    bb1 = bb / len(all_predictions)
    cc1 = cc / len(all_predictions)
    print('\n')
    print('所有药材中预测为0的概率', aa1)
    print('所有药材中预测为1的概率', bb1)
    print('所有药材中预测为2的概率', cc1)
    values1 = [aa1, bb1, cc1]
    colors = ['green', 'red', 'orange']

    plt1.title('乙烯')

    plt1.pie(values1, autopct='%3.1f %%', colors=colors)
    plt1.show()

    plt.scatter(x, y, c=all_predictions)
    plt.title('分成三类')
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel('乙醇转化率')
    plt.ylabel('乙烯选择性')
    plt.show()


one()

