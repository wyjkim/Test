import pandas as pd

import numpy as np


import matplotlib as mpl

import matplotlib.pyplot as plt

traffic=pd.DataFrame(pd.read_csv('DD.csv'))

plt.hist(traffic['zinc_copper'])

plt.show()


   # 统计上线用户活跃度，绘图
