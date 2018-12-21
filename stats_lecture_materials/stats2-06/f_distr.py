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
ax.set_xlim([x_left_max, x_right_max])
ax.set_ylim([0, 2.5])
# Set the title of the graph
plt.title(r'F-Distribution (PDF, central)')

# degrees of freedom for sample 1
df1 =[1, 2, 5, 10, 100]
# degrees of freedom for sample 2
df2 =[1, 1, 2, 1, 100]

# Plot probability density function
for d1, d2 in zip(df1, df2):
    y = ss.f.pdf(x, d1, d2, loc=0, scale=1)
    ax.plot(x, y, alpha=0.6, label='d1={}, d2={}'.format(d1, d2))
    ax.legend()
    plt.draw()
    plt.waitforbuttonpress()

plt.savefig("f_distr_pdf.png")
# Do not prevent the following codes to be executed
# with block=False
plt.show(block=False)

# clear figure
plt.cla()

# Plot cumulative distribution function
for d1, d2 in zip(df1, df2):
    y = ss.f.cdf(x, d1, d2, loc=0, scale=1)
    ax.plot(x, y, alpha=0.6, label='d1={}, d2={}'.format(d1, d2))
    ax.legend()
    plt.draw()
    plt.waitforbuttonpress()
# Set the title of the graph
plt.title(r'F-Distribution (CDF, central)')
plt.savefig("f_distr_cdf.png")
plt.show()