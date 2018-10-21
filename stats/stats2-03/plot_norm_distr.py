import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


# range of x 
x_left_max = -3
x_right_max = 3

file_basename = "critical_approach"
suffix = ".png"

# 0 for lower/left-tailed
# 1 for upper/right-tailed
# 2 for two-tailed 
file_names = ["left_tailed", "right_tailed", "two_tailed"]
left_tailed, right_tailed, two_tailed = range(3) 

test_types = 2

# Set the significance level, alpha = 5%
alpha = 0.05
x_critical_val = ss.norm.ppf(1-alpha)

# Set up filename
filename = file_basename + file_names[test_types] + suffix

if test_types == two_tailed:
    x_critical_val = ss.norm.ppf(1-alpha/2)  

prob_left = ss.norm.cdf(x=-x_critical_val, loc=0, scale=1) 
prob_right = 1 - ss.norm.cdf(x=x_critical_val, loc=0, scale=1) 
prob_between = 1 - (prob_left + prob_right)

if test_types == left_tailed or test_types == two_tailed:
    # plot left tail
    x_left = np.arange(x_left_max, -x_critical_val, 0.01)
    y_left = ss.norm.pdf(x_left)                      
    plt.fill_between(x=x_left, y1=y_left, facecolor='red', alpha=0.35)
    if test_types != two_tailed:
        x_right = np.arange(-x_critical_val, x_right_max, 0.01)
        y_right = ss.norm.pdf(x_right)
        plt.fill_between(x=x_right, y1=y_right, facecolor='blue', alpha=0.35)
        plt.text(x=x_left_max, y=0.03, s="alpha = {}% \n rejected".format(alpha*100))
        plt.text(x=x_left_max+2.0, y=0.03, s=" 1 - alpha = {}% \n retained ".format((1-alpha)*100))

if test_types == right_tailed or test_types == two_tailed:
    # plot right tail
    x_right = np.arange(x_critical_val, x_right_max, 0.01)
    y_right = ss.norm.pdf(x_right)                      
    plt.fill_between(x=x_right, y1=y_right, facecolor='red', alpha=0.35)
    if test_types != two_tailed:
        x_left = np.arange(x_left_max, x_critical_val, 0.01)
        y_left = ss.norm.pdf(x_left)                      
        plt.fill_between(x=x_left, y1=y_left, facecolor='blue', alpha=0.35)
        plt.text(x=x_critical_val+0.5, y=0.03, s="alpha = {}% \n rejected".format(alpha*100))
        plt.text(x=x_critical_val-3.5, y=0.03, s="1 - alpha = {}% \n retained ".format((1-alpha)*100))
         

if test_types == two_tailed:
    # plot central
    x_central = np.arange(-x_critical_val, x_critical_val, 0.01)
    y_central = ss.norm.pdf(x_central) 
    plt.fill_between(x=x_central, y1=y_central, facecolor='blue', alpha=0.35)

    plt.text(x=x_left_max, y=0.03, s="alpha/2 = {}% \n reject the null hypothesis".format(alpha*100/2))
    plt.text(x=-0.2, y=0.1, s="{}%(1-alpha) \n retain the null hypothesis".format((1-alpha)*100))
    plt.text(x=x_critical_val+0.5, y=0.03, s="alpha/2 = {}% \n reject the null hypothesis".format(alpha*100/2))

plt.xlabel("z value")
plt.savefig(filename)
plt.show()
