"""
fibonacci

functions to compute fibonacci numbers

Complete problems 2 and 3 in this file.
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


# Question 2
"""
Fibonacci numbers calculated using recursion
"""
def fibonacci_recursive(n):
    # Check for base cases.
    if (n == 1) or (n == 0):
        return n
    else:
        # Recursive component.
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Question 2
"""
Fibonacci numbers calculated using iteration
"""
def fibonacci_iter(n):
   # Check for base cases.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Iterative component.
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    # Print the first 30 Fibonacci numbers using both functions.
    for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]:
        print("fibonacci_recursive({}) = {}".format(n, fibonacci_recursive(n)))
        print("fibonacci_iter({}) = {}".format(n, fibonacci_iter(n)))
# Question 3
def fibonacci_power(n):
    """
    Computes the nth fibonacci number using matrix exponentiation

    Assume n is a nonegative integer
    """
    def matrix_mult(A, B):
        """
        Multiplies two 2x2 matrices A and B
        """
        return np.array([[A[0,0]*B[0,0] + A[0,1]*B[1,0], A[0,0]*B[0,1] + A[0,1]*B[1,1]],
                         [A[1,0]*B[0,0] + A[1,1]*B[1,0], A[1,0]*B[0,1] + A[1,1]*B[1,1]]])

    def matrix_power(A, n):
        """
        Computes the nth power of a 2x2 matrix A using exponentiation by squaring
        """
        if n == 0:
            return np.eye(2)  # Identity matrix
        elif n == 1:
            return A
        elif n % 2 == 0:
            half_power = matrix_power(A, n // 2)
            return matrix_mult(half_power, half_power)
        else:
            return matrix_mult(A, matrix_power(A, n - 1))

    # The transformation matrix for Fibonacci sequence.
    F = np.array([[1, 1],
                  [1, 0]])

    if n == 0:
        return 0
    else:
        result_matrix = matrix_power(F, n - 1)
        return result_matrix[0, 0]


if __name__ == '__main__':
    # Print the first 30 Fibonacci numbers using the matrix function.
    for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]:
        print("fibonacci_power({}) = {}".format(n, fibonacci_power(n)))


if __name__ == '__main__':
    """
    this section of the code only executes when
    this file is run as a script.
    """
    def get_runtimes(ns, f):
        """
        get runtimes for fibonacci(n)

        e.g.
        trecursive = get_runtimes(range(30), fibonacci_recusive)
        will get the time to compute each fibonacci number up to 29
        using fibonacci_recursive
        """
        ts = []
        for n in tqdm(ns):
            t0 = time.time()
            fn = f(n)
            t1 = time.time()
            ts.append(t1 - t0)

        return ts


    nrecursive = range(35)
    trecursive = get_runtimes(nrecursive, fibonacci_recursive)

    niter = range(10000)
    titer = get_runtimes(niter, fibonacci_iter)

    npower = range(10000)
    tpower = get_runtimes(npower, fibonacci_power)

    ## write your code for problem 4 below...

def positive(ns, ts):
    """Drop n = 0 and zero runtimes, which can't be drawn on a log axis."""
    pairs = [(n, t) for n, t in zip(ns, ts) if n > 0 and t > 0]
    return [p[0] for p in pairs], [p[1] for p in pairs]

fig, ax = plt.subplots(figsize=(10, 6))

# The following code plots lines for the runtimes of all three algorithms.
ax.plot(*positive(nrecursive, trecursive), linewidth=2, label='Recursive')
ax.plot(*positive(niter, titer), linewidth=2, label='Iterative')
ax.plot(*positive(npower, tpower), linewidth=2, label='Matrix power')

# Both axes are set to log, as specified in the assignment.
ax.set_xscale('log')
ax.set_yscale('log')
# Labels are the required font size.
ax.set_xlabel('n', fontsize=16)
ax.set_ylabel('Runtime (seconds)', fontsize=16)
ax.set_title('Runtime of Fibonacci algorithms', fontsize=16)
ax.tick_params(axis='both', which='both', labelsize=16)
ax.legend(fontsize=16)

# Graph is saved to a file and displayed.
plt.tight_layout()
plt.savefig('fibonacci_runtimes.png', dpi=150)
plt.show()