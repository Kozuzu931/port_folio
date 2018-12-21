#!/usr/bin/env python

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


# ss.chi2.pdf(x, df, loc, scale):
#       A chi-squared continuous random variable.
# ss.chisquare(f_obs, f_exp=None, ddof=0, axis=0):
#      Calculate a one-way chi square test.
# ss.chi2_contingency(observed, correction=True, lambda_=None):
#      Chi-square test of independence of variables in a contingency table.

# range of x
x_left_max = 0
x_right_max = 8
num_sample = 1000

x = np.linspace(x_left_max, x_right_max, num_sample)

# subplots()
fig, ax = plt.subplots(1,1)
# Set the data limits for the x/y-axis
ax.set_xlim([x_left_max, x_right_max])
ax.set_ylim([0, 1])
# Set the x/y label
plt.xlabel('$\chi^2$')
plt.ylabel(r'$f(\chi^2)$')
# Set the title of the graph
plt.title(r'$\chi^2\ \mathrm{PDF\; Distribution}$')

# degree of freedoms for chi-squared distribution
degreeOfFreedoms = [1, 2, 3, 4, 5, 6, 7, 8,  9]

for k in degreeOfFreedoms:
    y = ss.chi2.pdf(x, k)
    ax.plot(x, y, alpha=0.6, label='chi2 k={}'.format(k))
    ax.legend()
    plt.draw()
    plt.waitforbuttonpress()

plt.show()