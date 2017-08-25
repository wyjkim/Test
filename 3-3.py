import pandas as pd

import numpy as np


import matplotlib as mpl

import matplotlib.pyplot as plt

traffic=pd.DataFrame(pd.read_csv('DD.csv'))

plt.hist(traffic['END_DATE'])

plt.show()
