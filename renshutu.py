import pandas as pd

import numpy as np


import matplotlib as mpl

import matplotlib.pyplot as plt

traffic=pd.DataFrame(pd.read_csv('DD.csv'))

plt.hist(traffic['LOG_ID'])

plt.show()
