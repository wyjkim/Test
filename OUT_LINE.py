import pandas as pd

import numpy as np


import matplotlib as mpl

import matplotlib.pyplot as plt

traffic=pd.DataFrame(pd.read_csv('DD.csv'))

plt.hist(traffic['OUT_LINE'])

plt.show()


#根据统计的认证人数，绘图
