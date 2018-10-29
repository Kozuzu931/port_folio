#!/usr/bin/env python
"""
Modified Bessel function of the first kind of real order.

In Scipy,

scipy.special.iv(v, z) = <ufunc 'iv'>

    Parameters:
    v : array_like
    Order. If z is of real type and negative, v must be integer valued.
    z : array_like of float or complex
    Argument.
    Returns:
    out : ndarray
    Values of the modified Bessel function.

Example:
  import scipy.special as sp
  sp.special.iv(v, z)
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp


# range of x
x_left_max = 0
x_right_max = 5
num_sample = 1000

x = np.linspace(x_left_max, x_right_max, num_sample)
# subplots()
fig, ax = plt.subplots(1,1)
# Set the data limits for the x/y-axis
ax.set_xlim([x_left_max, x_right_max])
ax.set_ylim([0, x_right_max])

max_n = 6
v = list(range(max_n))

for n in v:
    bessel_term = sp.iv(n, x)
    ax.plot(x, bessel_term, label='n={}'.format(n))
    ax.legend()
    plt.draw()
    plt.waitforbuttonpress()

plt.show()