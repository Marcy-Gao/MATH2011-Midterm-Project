import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - 2*x - 5

def f_prime(x):
    return 3*x**2 - 2



# Bisection Method
def bisection_method(a, b, tol=1e-7, max_iter=100, precision=np.float64, root_truth=2.09455148154232659):
    a = precision(a)
    b = precision(b)
    iter_count = 0
    roots = []  
    errors = []  
    while iter_count < max_iter:
        c = precision((a + b) / 2)
        roots.append(c)  
        error = abs(c - root_truth)
        errors.append(error)  
        if precision(abs(f(precision(c)))) < tol:
            break 
        iter_count += 1
        if f(precision(a)) * f(precision(c)) < 0:
            b = c
        else:
            a = c
    return roots, errors, iter_count  

# Newton's Method
def newtons_method(x0, tol=1e-7, max_iter=100, precision=np.float64, root_truth=2.09455148154232659):
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
        if precision(abs(fx)) < tol:
            break  
        x = precision(x - fx / fpx)
        iter_count += 1
    return roots, errors, iter_count   

precisions = [np.float16, np.float32, np.float64, np.longdouble]
tolerances = [1e-7]
root_truth = 2.09455148154232659 

results_bisection = []
results_newton = []


for precision in precisions:
    for tol in tolerances:
        # Bisection method
        roots_bis, errors_bis, iter_bis = bisection_method(2, 3, tol=tol, precision=precision, root_truth=root_truth)
        results_bisection.append((precision, tol, roots_bis, errors_bis, iter_bis))
        
        # Newton's method
        roots_newt, errors_newt, iter_newt = newtons_method(2.5, tol=tol, precision=precision, root_truth=root_truth)
        results_newton.append((precision, tol, roots_newt, errors_newt, iter_newt))


# Plot

for i, precision in enumerate(precisions):
    plt.figure(figsize=(8, 6))
    filtered_results = [result for result in results_bisection if result[0] == precision]
    for result in filtered_results:
        errors_bis = result[3]
        tol = result[1]
        plt.plot(range(len(errors_bis)), errors_bis, label=f'Tolerance: {tol}', marker='o')
    plt.title(f"Bisection Method Error vs Iterations for Precision {precision}")
    plt.xlabel("Iteration Count")
    plt.ylabel("Error")
    plt.ylim(0, 0.05)
    plt.legend()
    plt.show()


    # Newton's Method Plot for current precision
    plt.figure(figsize=(8, 6))
    filtered_results = [result for result in results_newton if result[0] == precision]
    for result in filtered_results:
        errors_newt = result[3]
        tol = result[1]
        plt.plot(range(len(errors_newt)), errors_newt, label=f'Tolerance: {tol}', marker='x')
    plt.title(f"Newton's Method Error vs Iterations for Precision {precision}")
    plt.xlabel("Iteration Count")
    plt.ylabel("Error")
    plt.ylim(0, 0.05)
    plt.legend()
    plt.show()
