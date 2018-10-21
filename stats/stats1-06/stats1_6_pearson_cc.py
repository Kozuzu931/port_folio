#!/usr/bin/env python

import numpy as np
import scipy.stats as ss

import pandas as pd

x=np.array([0,0,0,1,1,1,1])
y=np.arange(7)

# create a dataframe from numpy arrays
#d = {'x': x, 'y': y}
df = pd.DataFrame(data=np.stack((x, y), axis=1))

n = len(x)
sx = np.sqrt(np.sum(np.abs(x - x.mean())**2)/(len(x)-1))
sy = np.sqrt(np.sum(np.abs(y - y.mean())**2)/(len(y)-1))

cc = sum(((x - x.mean())/sx) * ((y - y.mean())/sy))/(n - 1)
print("Self - CC: {:.3f}".format(cc))

cc = np.corrcoef(x, y)[0, 1]
print("numpy - CC {:.3f}".format(cc))

cc, p_value = ss.pearsonr(x, y)
print("Scipy - CC : {:.3f} and p-value: {:.3f}".format(cc, p_value))

cc = df.corr(method="pearson") #also available ‘kendall’ and ‘spearman’
                               # covariance matrix
print("CC by pandas dataframe: {:.3f}".format(cc[0][1]))