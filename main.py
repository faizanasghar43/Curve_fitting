
# importing the required module
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import scipy.stats as stats


def sum_fun(arr, size):
    sum_ = 0
    for i in range(size):
        sum_ = arr[i]+sum_
    return sum_


def true_value_error_finder(x_, y_, m, c):
    true_values_ = np.zeros(len(y_))
    err = np.zeros(len(y_))
    for i in range(len(x_)):
        true_values_[i] = c + m * x_[i]
        err[i] = true_values_[i] - y[i]
    print("True VALUES func = ", true_values_, "\n ERROR FROM FUNCTION = ", err)
    print("\n\n\nError = ", np.mean(true_values_) - np.mean(err))


x = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
y = [5, 6, 7, 6, 9, 8, 7, 10, 12, 12]
# x = [46 ,65, 53 ,38 ,61 ,89 ,59 ,60 ,73]
# y = [940, 790, 910, 1020, 540, 340, 810, 720, 830]

slope, intercept, r_value, p_value, std_err = linregress(x, y)
print("Slope =", slope)
print("Intercept =", intercept)
print("r_value", r_value)
print("p_value", p_value)
print("std_error in % ", std_err*100, "%")
r = sum_fun(stats.zscore(x)*stats.zscore(y), 9)
r = r/9
print("r = ", r)
div_std = np.std(y)/np.std(x)
slide_slope = r*div_std

intercept_slide = np.mean(y) - slide_slope*np.mean(x)

true_value_error_finder(x, y, slide_slope, intercept_slide)

x = np.array(x)
y = np.array(y)
plt.plot(x, y, 'o')
slide_slope, intercept_slide = np.polyfit(x, y, 1)
plt.plot(x, slide_slope*x + intercept_slide)
plt.show()
