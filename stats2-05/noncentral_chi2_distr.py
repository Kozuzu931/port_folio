#!/usr/bin/env python

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# range of x
x_left_max = 0
x_right_max = 8
num_sample = 1000

x = np.linspace(x_left_max, x_right_max, num_sample)

# subplots()
fig, ax = plt.subplots(1,1)
# Set the data limits for the x/y-axis
ax.set_xlim([x_left_max-0.5, x_right_max])
ax.set_ylim([0, 0.3])
# Set the x/y label
plt.xlabel('$\chi^2$')
plt.ylabel(r'$f(\chi^2)$')
# Set the title of the graph
plt.title(r'$\chi^2\ \mathrm{PDF\; Distribution(noncentral)}$')

# k: degree of freedoms for chi-squared distribution
df = [2, 4]
# lambda: non-centrality parameters
lambda_params = [1, 2, 3]
for k in df:
    for nc in lambda_params:
        y = ss.ncx2.pdf(x, k, nc)
        ax.plot(x, y, alpha=0.6, label='k={} $\lambda={}$'.format(
                k, nc))
        ax.legend()
        plt.draw()
        plt.waitforbuttonpress()

plt.show()