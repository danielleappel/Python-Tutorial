# This is my code to demonstrate how scope and binding work in Python

z = 4
m = 42

def square(n):
    """Square a given number.

    Keyword arguments:
    n -- the number to square
    """
    x = n * n
    print("  x inside square(y) is %d" %x)
    return x

def foo():
    """Simple function to access global variable, z."""
    print("z inside foo() is %d" %z)

def double():
    """Double the global variable z."""
    global z
    print("  z inside double() before doubling is %d" %z)
    z *= 2
    print("  z inside double() after doubling is %d" %z)

def double_wrapper_global():
    """Call double_global()."""
    m = 10
    def double_global():
        """Double the global variable m."""
        global m
        print("  nested global m before doubling is %d" %m)
        m *= 2
        print("  nested global m after doubling is %d" %m)
    print("local m before doubling is %d" %m)
    double_global()
    print("local m after doubling is %d" %m)

def double_wrapper_nonlocal():
    """Call double_nonlocal()."""
    n = 35
    print("n in double_wrapper_nonlocal() before double_nonlocal() is %d" %n)
    def double_nonlocal():
        """Double the nonlocal variable n."""
        nonlocal n
        print("  n in double_nonlocal() before doubling is %d" %n)
        n *= 2
        print("  n in double_nonlocal() after doubling is %d" %n)
    double_nonlocal()
    print("n in double_wrapper_nonlocal() after double_nonlocal() is %d" %n)

def main():
    # Same named variable in a for loop
    x = 7
    print("x before the for loop is %d" %x)
    for x in range(10):
        print("  x inside the for loop is %d" %x)
    print("x after the for loop is %d" %x)

    print("\n")

    sum = 0
    print("sum before the for loop is %d" %sum)
    for x in range(10):
        sum += x+1
        print("  sum of the first %d terms is %d" %(x+1, sum))
    print("sum after the for loop is %d" %sum)

    print("\n")

    # Same named variable in a function
    x = 9
    y = 11
    print("y before square(y) is %d" %y)
    print("x before square(y) is %d" %x)
    result = square(y)
    print("y after square(y) is %d" %y)
    print("x after square(y) is %d" %x)
    print("And the result of square(y) is %d" %result)

    print("\n")

    # Global variables
    foo()

    print("\n")

    double()
    global z
    print("global z after double() is %d" %z)

    print("\n")

    # Nested global variables
    double_wrapper_global()
    global m
    print("global m after double_wrapper_global() is %d" %m)

    print("\n")

    # Non-local variables
    double_wrapper_nonlocal()

    print("\n")

    # Pass-by-reference with mutable data types
    a = ["c","a","t"]
    b = ["d","o","g"]
    print("a before changes is %s" %a)
    print("b before changes is %s" %b)
    a = b
    b[1] = "u"
    print("a after changes is %s" %a)
    print("b after changes is %s" %b)

    print("\n")

    # Pass-by-value with immutable data types
    c = ("c","a","t")
    d =("d","o","g")
    print("c before changes is ", c)
    print("d before changes is ", c)
    c = d
    d += ("s",)
    print("c after changes is ", c)
    print("d after changes is ", d)

if __name__ == "__main__":
    main()
