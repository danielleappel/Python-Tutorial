# This is my code about functions and parameters in Python

def multiply(factor1, factor2):
    """Return the product of two numbers.

    Keyword arguments:
    factor1 -- the first factor
    factor2 -- the second factor
    """
    return factor1 * factor2

def factorial(n):
    """Recursively return the factorial.
    
    Keyword arguments:
    n -- the number to take factorial of
    """
    if  n == 1:
        return n
    else:
        return n * factorial(n-1)

def string_split(s):
    """Split and return both halves of a string.
    
    Keyword arguments:
    s -- the string to split
    """
    midpoint = len(s)//2
    return s[ : midpoint], s[midpoint : ]

def make_multiplier(n):
    """Creates a multiplier.

    Keyword arguments:
    n -- the number to multiply by
    """
    return lambda x: x * n

def f(x):
    """Try to reassign the value of x

    Keyword arguments:
    x -- the original numerical value of x
    """
    x = 2

def swap(A, i, j):
    """Swap the values A[i] and A[j].

    Keyword arguments:
    A -- the array of interest
    i -- the first index
    j -- the second index
    """
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def average_age_packing(**d):
    """Calculate the average age.

    Keyword arguments:
    **d -- the dictionary to use containing vals of the ages
    """
    sum = 0
    for key, val in d.items():
        sum += val
    return sum/len(d)

def f(a, b, c):
    """Demonstrate argument dictionary unpacking.

    Keyword arguments:
    a, b, c -- anything to print
    """
    print("a unpacked is: ", a)
    print("b unpacked is: ", b)
    print("c unpacked is: ", c)


def main():
    
    factor1 = 12
    factor2 = 3
    product = multiply(factor1,factor2)
    print("The product of %d and %d is %d." %(factor1, factor2, product))

    n = 4
    fac = factorial(n)
    print("The factorial of %d is %d" %(n, fac))

    s = "Hello."
    (first, second) = string_split(s)
    print("The first half of the string %s is %s and the second half is %s" %(s, first, second))
    t = "Goodbye."
    result = string_split(s)
    print("The two halfs of the string %s is %s" %(t, result))

    mul_by_12 = make_multiplier(12)
    print("Some multiples of 12 are: ", mul_by_12(0), mul_by_12(1), mul_by_12(2))

    A = [1, 2, 3, 4]
    swap(A, 2, 3)
    print("A is: ", A)

    for element in A:
        element = 7
        print("element: %d" %element)
    print("A is: ", A)

    for i in range(len(A)):
        A[i] = 7
        print("i: %d, A[i]: %d" %(i, A[i]))
    print("A is: ", A)

    help(multiply)

    avg_age_packing = average_age_packing(dani=22, johnny=24, bella=6) # Argument dictionary packing
    print("The average calculated with argument dictionary packing is %d." %avg_age_packing)

    dictionary = {'a': 22, 'b': 24, 'c': 6} # Argument dictionary unpacking
    d = {'a': 'foo', 'b': 25, 'c': 'qux'}
    f(**dictionary)

if __name__ == "__main__":
    main()
