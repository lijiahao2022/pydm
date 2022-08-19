# li jia hao
# 时间：2022/8/1 10:58
import pandas as pd
data=pd.read_excel('表1.xlsx')
print(data)
'''
print(data)
print(data[data.x>800])
data.y[data.x>900]=0
print(data)
'''
i=0
for item in range(1,11):
    if data.iloc[i,1]>1500:
        data.drop(data.index[i],inplace=True)
        i=i-1
    i=i+1
print(data)
