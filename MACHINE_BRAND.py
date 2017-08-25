import pandas as pd
import os

path = os.getcwd()+'\\DD.csv'
f = open(path)
data = pd.read_csv(f)
print(data.ix[:, 'MACHINE_BRAND'])


#统计机器类型
