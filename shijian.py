import pandas as pd
df = pd.read_csv("DD.csv")
pd.DataFrame(df,columns = ['START_DATE','END_DATE'])
df['START_DATE_END'] = df['START_DATE']-df['END_DATE']
df


# 统计用户上线时间
