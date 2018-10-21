#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:52:40 2018

@author: davecao
"""

# %% 1. Import numpy,statsmodels, matplotlib

# numpy
import numpy as np
# statsmodels
import statsmodels.api as sm
# matplotlib
import matplotlib.pyplot as plt

# %% author
__author__ = "Kousuke Tsuchiya"
__studentId__ = "s1f101700158"


# %% 2. Read the data file -  task7_1_1_data.csv by numpy'loadtxt()
data = np.loadtxt("data/task7_1_1_data.csv", comments="#",delimiter=",")
# %% 3. Simple linear regression
x = data[:, 0]
Y = data[:, 1]
# %% 4. Construct a scatter plot and draw the regression line
# See the tutorial
X = sm.add_constant(x)
plt.scatter(x, Y, color="red", alpha=0.5)
# Model: y ~ ax + c
model = sm.OLS(Y, X)
results = model.fit()
# Write down c value obtained from OLS
__constant__ = results.params[0]
# Write down a value
__slope__ = results.params[1]
# Write down the condition number
__condo__ = results.condition_number

# %% Construct a scatter plot and draw the regression line in the same graph
# Graph attributes: label, legend
### Regression line
x_pred = np.linspace(x.min(), x.max(), 50)
x_pred2 = sm.add_constant(x_pred)
y_pred = results.predict(x_pred2)

plt.plot(x_pred, y_pred, '-', color='darkorchid', linewidth=0.5)
txt = "y={:.2f}x+{:.2f}".format(results.params[1], results.params[0])
plt.legend([txt, "data"], frameon=True)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()


# Set attributes for graph
plt.show()