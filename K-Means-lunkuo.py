import pandas as pd
import numpy as np
data=pd.read_excel("D:/数模/2021赛题/E/附件1.xlsx")
from sklearn import preprocessing
data_scaled=preprocessing.scale(data)
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
X=data_scaled
scores=[]
for i in range(2,11):
    km=KMeans(n_clusters=i,init='k-means++',n_init=10,max_iter=300,random_state=0)
    km.fit(X)
    scores.append(metrics.silhouette_score(X,km.labels_,metric='euclidean'))
plt.figure(dpi=150)
plt.plot(range(2,11),scores,marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('silhouette_score')
plt.show()