import pandas as pd
import os

path = os.getcwd()+'\\DD.csv'
f = open(path)
data = pd.read_csv(f)
print(data.ix[:, 'OUT_LINE'])


#统计认证次数
