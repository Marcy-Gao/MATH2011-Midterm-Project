import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 5

def f_prime(x):
    return 3*x**2 - 2

# Bisection Method
def bisection_method(a, b, tol=1e-7, max_iter=60, precision=np.float64, root_truth=2.09455148154232659):
    a = precision(a)
    b = precision(b)
    iter_count = 0
    roots = []  
    errors = []  
    while iter_count < max_iter:
        c = precision((a + b) / 2.0)
        roots.append(c)  
        error = abs(c - root_truth)
        errors.append(error)  
        print(f"Bisection iteration {iter_count + 1}: Root estimate = {c}, Error = {error}")
        if precision(abs(f(precision(c)))) < tol:
            break 
        iter_count += 1
        if f(precision(a)) * f(precision(c)) < 0:
            b = c
        else:
            a = c
    print(f"precision {precision}, Bisection iteration {iter_count + 1}: Root estimate = {c}, Error = {error}")
    return roots, errors, iter_count  

# Newton's Method
def newtons_method(x0, tol=1e-7, max_iter=60, precision=np.float64, root_truth=2.09455148154232659):
    x = precision(x0)
    iter_count = 0
    roots = []  
    errors = []  
    while iter_count < max_iter:
        fx = precision(f(x))
        fpx = precision(f_prime(x))
        roots.append(x)  
        error = abs(x - root_truth)
        errors.append(error)  
        print(f"Newton's iteration {iter_count + 1}: Root estimate = {x}, Error = {error}")
        if precision(abs(fx)) < tol:
            break  
        x = precision(x - fx / fpx)
        iter_count += 1
    print(f"precision {precision}, Newton's iteration {iter_count + 1}: Root estimate = {x}, Error = {error}")
    return roots, errors, iter_count  

# Main script for testing with different precisions
precisions = [np.float16, np.float32, np.float64, np.longdouble]
tolerances = 1e-7

results_bisection = []
results_newton = []
root_truth = 2.09455148154232659     

for precision in precisions:
        tol = tolerances
        # print(f"\nBisection Method (Precision: {precision}, Tolerance: {tol}):")
        roots_bis, errors_bis, iter_bis = bisection_method(2, 3, tol=tol, precision=precision, root_truth=root_truth)
        results_bisection.append((precision, tol, roots_bis, errors_bis, iter_bis))

        
        #print(f"\nNewton's Method (Precision: {precision}, Tolerance: {tol}):")
        roots_newt, errors_newt, iter_newt = newtons_method(2.5, tol=tol, precision=precision, root_truth=root_truth)
        results_newton.append((precision, tol, roots_newt, errors_newt, iter_newt))


