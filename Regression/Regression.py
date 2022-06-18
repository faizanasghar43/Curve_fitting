
# importing the required module
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def sum_fun(arr):
    sum_ = 0
    for i in range(len(arr)):
        sum_ = arr[i]+sum_
    return sum_


def true_value_error_finder(x_, y_, m, c):
    true_values_ = np.zeros(len(y_))
    err = np.zeros(len(y_))
    for i in range(len(x_)):
        true_values_[i] = c + m * x_[i]
        err[i] = (true_values_[i] - y[i])/true_values_[i]
        err[i] *= 100
        print((true_values_[i], "-", y[i]), "/", true_values_[i], " ) * 100 \n")
        print(" \n Error at ", i, " th iteration error is ", err[i], " % \n")
    print("True VALUES func = ", true_values_, "\n ERROR FROM FUNCTION = ", err)
    print("\n\n\nError = ", np.mean(true_values_) - np.mean(err))


x = [0, 1, 2, 3, 4]
y = [1, 1.8, 3.3, 4.5, 6.3]
# x = [46 ,65, 53 ,38 ,61 ,89 ,59 ,60 ,73]
# y = [940, 790, 910, 1020, 540, 340, 810, 720, 830]

correlation_coefficient = sum_fun(stats.zscore(x)*stats.zscore(y))  # correlation coefficient  using z_scores
correlation_coefficient /= 9
print("r = ", correlation_coefficient)
div_std = np.std(y)/np.std(x)      # std being divided to multiply with correlation coefficient and obtain slope
slope = correlation_coefficient*div_std
intercept = np.mean(y) - slope*np.mean(x)
true_value_error_finder(x, y, slope, intercept)
print("slope\n", slope)
print("intercept\n", intercept)


x = np.array(x)
y = np.array(y)
plt.plot(x, y, 'o')
slope, intercept = np.polyfit(x, y, 1)
plt.plot(x, slope*x + intercept)
plt.show()



