#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


# Step 1. Load the csv data
# loadtxt() will not work since we have string at the last column
# data = np.loadtxt('iris.csv', delimiter=',', skiprows=1)
data = np.genfromtxt('data/iris.csv', delimiter=',',dtype='f8,f8,f8,f8,S20', skip_header=1)

data = tuple(data)

# for iris setosa
setosa_sepal_attr = [[x[0], x[1]] for x in data if x['f4'] == b'Iris-setosa' ] # List Comprehensive, remember it?
setosa_sepal_attr = np.asarray(setosa_sepal_attr) # Convert into numpy array

x1 = setosa_sepal_attr[:, 0] # Array slicing, the first column containing the data of sepal length
y1 = setosa_sepal_attr[:, 1] # Array slicing, the second column containing the data of sepal width


# for iris virginica
virginica_sepal_attr = [[x[0], x[1]] for x in data if x['f4'] == b'Iris-virginica' ] 
virginica_sepal_attr = np.asarray(virginica_sepal_attr) 
print("There are {} samples for virginica".format(len(virginica_sepal_attr)))

x2 = virginica_sepal_attr[:, 0]
y2 = virginica_sepal_attr[:, 1]

# for iris versicolor
versicolor_sepal_attr = [[x[0], x[1]] for x in data if x['f4'] == b'Iris-versicolor' ] 
versicolor_sepal_attr = np.asarray(versicolor_sepal_attr) 
print("There are {} samples for vesicolor".format(len(versicolor_sepal_attr)))
x3 = versicolor_sepal_attr[:, 0]
y3 = versicolor_sepal_attr[:, 1]


# make a scatter plot with plot()
plt.plot(x1, y1,'o', color='black')
plt.title('Scatter plot by plot()')
plt.legend(['setosa'])
plt.show()

# make a scatter plot with scatter()
plt.scatter(x1, y1)
plt.title('Scatter plot by scatter() for setosa')
plt.legend(['setosa'])
plt.show()

# plot the three species together
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.scatter(x3, y3)
legend_txt = ['setosa', 'virginica', 'versicolor']
plt.legend(legend_txt)
plt.title('Sepal attributes for 3 species by scatter()')
plt.show()

# Difference between plot() and scatter()
# | -- https://matplotlib.org/tutorials/colors/colormaps.html
color_map = plt.cm.get_cmap('rainbow')

plt.scatter(x1, y1, s=20, alpha=0.2)
plt.scatter(x2, y2, s=20, alpha=0.2)
plt.scatter(x3, y3, s=50, alpha=0.2)
legend_txt = ['setosa', 'virginica', 'versicolor']
plt.legend(legend_txt)
plt.title('Sepal attributes for 3 species by scatter()')
plt.show()
