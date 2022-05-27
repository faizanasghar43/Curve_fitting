
# importing the required module
import matplotlib.pyplot as plt
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


r = sum_fun(stats.zscore(x)*stats.zscore(y), 9)  # r_values using z_scores
r = r/9
print("r = ", r)
div_std = np.std(y)/np.std(x)      # std being divided to multiply with r_value and obtain slope
slope = r*div_std

intercept = np.mean(y) - slope*np.mean(x)

true_value_error_finder(x, y, slope, intercept)


plt.plot(x, y, 'o')
slide_slope, intercept_slide = np.polyfit(x, y, 1)
plt.plot(x, slide_slope*x + intercept_slide)
plt.show()
