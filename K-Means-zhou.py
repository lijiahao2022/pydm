import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_excel(r'D:\数模\\2021赛题\E\附件1.xlsx')
# '利用SSE选择k'
SSE = []  # 存放每次结果的误差平方和
for k in range(1, 21):
    estimator = KMeans(n_clusters=k)  # 构造聚类器
    estimator.fit(np.array(data))
    SSE.append(estimator.inertia_)
X = range(1, 21)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X, SSE, 'o-')
plt.show()