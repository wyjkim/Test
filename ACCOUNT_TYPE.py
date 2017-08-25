import pandas as pd
import os

path = os.getcwd()+'\\DD.csv'
f = open(path)
data = pd.read_csv(f)
print(data.ix[:, 'ACCOUNT_TYPE'])


#统计上线用户类型
