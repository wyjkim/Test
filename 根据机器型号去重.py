from pandas import Series, DataFrame
import pandas as pd
import os

path = os.getcwd()+'\\DD.csv'
f = open(path)
data = pd.read_csv(f)


IsDuplicated = data.duplicated()

print(IsDuplicated)
print( type(IsDuplicated))

data = data.drop_duplicates()

