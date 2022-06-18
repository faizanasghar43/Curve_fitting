"""Problem Statement:
Implement Newton-Raphson method using MATLAB to compute the drag coefficient c needed
for a parachutist of mass m = First Two Digits of Your Registration Number ÷ 2 kg to have a
velocity of Second Last Digit of Your Registration Number + 40 m/s after free falling for time t =
Last Digit of your Registration Number + 5 secs. Note: The acceleration due to gravity is 9.81
m/s 2 .
The drag coefficient is given by

.
b. Choose an appropriate initial guess to start iterations in order to achieve convergence. If the
solution diverges re-choose the initial guess.
c. Calculate the approximated error after every iteration and tabulate your results.
d. The ending criteria of the numerical computation is such that the consecutive calculations
have a precision of 1e-4 (For Even Registration Number) and 1e-5 (For Odd Registration
Number).
e. Plot the computed drag coefficient values with respect to the number of iterations to show
convergence.
f. Validate the computed value."""


import sympy as s
from tabulate import tabulate


def newton_raphson_method(initial_guess):
    count = 0
    prev_c = initial_guess
    next__c = next_c(prev_c)
    count += 1
    error = abs(calculate_error(next__c, prev_c))
    data = [[count, prev_c, next__c, error, f_of_c_calculator(38, 42, 6, next__c)]]
    print(tabulate(data, headers=["Iteration", "Previous c", "Next c", "True Error", "f(c)"]))

    while abs(f_of_c_calculator(38, 42, 6, next__c)) >= 0.00001:
        prev_c = next__c
        next__c = next_c(prev_c)
        error = abs(calculate_error(next__c, prev_c))
        count += 1
        data = [[count, prev_c, next__c, error, f_of_c_calculator(38, 42, 6, next__c)]]
        print(tabulate(data, headers=["Iteration", "Previous c", "Next c", "True Error", "f(c)"]))
    return next__c


def next_c(c_val):
    return c_val - (f_of_c_calculator(38, 42, 6, c_val)/derivative_calculation(c_val))


def calculate_error(new_c, old_c):
    error = ((new_c-old_c)/new_c)*100
    return error


def f_of_c_calculator(mass_, velocity_, time_, c):
    g_mass_ = mass_
    print("mass = ", mass_)
    print("velocity = ", velocity_)
    print("time = ", time_)
    print("c will be = ", c)
    g_mass_ *= 9.8
    exp_ = (c / mass_) * time_
    exp_ *= -1
    f_of_c = (g_mass_ / c) * (1 - 2.71828 ** exp_)
    f_of_c -= velocity_
    print("Putting in equation of function is \n f(c) = ((g_ * m_) / c_) * (1 - s.exp((-1)*c_*t_/m_)) - v_")
    print(f_of_c)
    return f_of_c


def derivative_calculation(c_val):
    m_, v_, t_, g_, c_ = s.symbols('m_, v_, t_, g_, c_')
    f = ((g_ * m_) / c_) * (1 - s.exp((-1)*c_*t_/m_)) - v_
    fn = f.diff(c_)
    fn = fn.evalf(subs={m_: 38, g_: 9.8, c_: c_val, t_: 6, v_: 42})
    return fn


