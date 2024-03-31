import math

def f(x):
   return x * math.cos(x) - 2 * x**3 + 3 * x - 1

# Implementing Bisection Method
def bisection(a, b, e):
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Iteration", "a", "b", "c", "f(a)", "f(b)", "f(c)", "Error"))
    step = 1
    condition = True
    while condition:
        c = (a + b)/2
        fa = f(a)
        fb = f(b)
        fc = f(c)
        error = (b - a) / 2
        
        print('{:<10d} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f} {:<10.6f}'.format(step, a, b, c, fa, fb, fc, error))

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        step += 1
        condition = abs(fc) > e

    print('\nRequired Root is : %0.8f' % c)


# Input Section
a = float(input('Enter a: '))
b = float(input('Enter b: '))
e = float(input('Tolerable Error: '))

# Checking Correctness of initial guess values and bisecting
if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a, b, e)
