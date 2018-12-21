#!/usr/bin/env python

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt



# range of x 
x_left_max = -3
x_right_max = 3

x_norm = np.arange(x_left_max, x_right_max, 0.01)
y_norm = ss.norm.pdf(x_norm)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_norm, y_norm)
legend_info = ["std normal distr"]
ax.legend(legend_info)
plt.xlabel("random variable x")
plt.ylabel("P(X)")
# t-distribution
degreeOfFreedoms = [1, 2, 3, 5, 10, 30]

for d in degreeOfFreedoms:
    y_t = ss.t.pdf(x_norm, d, loc=0, scale=1)
    ax.plot(x_norm, y_t)
    legend_info.append("df={}".format(d))
    ax.legend(legend_info)
    plt.draw()
    plt.waitforbuttonpress()
