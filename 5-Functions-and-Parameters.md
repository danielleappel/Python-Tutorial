# Functions and parameter passing

## Syntax for functions

Python uses the key word `def` to declare new functions. The general format of a Python function is:

    >def function_name(argument1, argument2, ...):
        >statement1
        >statement2
        >...
        >return something
All of the code in the function must be indented more than the declaration. Functions are helpful to minimize repeated code. Why write a tedious chunk of code repeatedly when you could just use a function? 

How to call a function:
- Use its **name** (`function_name()` above)
- List the **arguments**, also known as inputs and parameters, go inside of the parentheses (`argument1` and `argument2` above)
- The function can **return** any type of object, or it might not. Unlike Java, Python is not required to return anything. If it does return something, you can set a variable equal to the result of the function call. If there is nothing returned, then `something` would equal `None` which is perfectly legal in Python.
    - Return statements always end a function.

For example, consider this code in [`functions_and_parameters.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/functions_and_parameters.py):

    >def multiply(a, b):
        >return a * b
- The function name is `multiply()`, 
- The arguments are two numbers `a` and `b`
- The product is the returned value. 

This code can be run as follows in `main()`

    >def main():    
        >a = 12
        >b = 3
        >product = multiply(a,b)
        >print("The product of %d and %d is %d." %(a, b, product))
And outputs

    The product of 12 and 3 is 36.
Of course, you do not have to use variables for the inputs to `multiply()`. The calculation could have easily been achieved by this line instead `product = multiply(12,3)`, but using numbers in code leaves too much room for so called "magic numbers".

Now, consider the problem as above, but if this function gets no arguments (ie is called as `multiply()` instead of `multiply(12,3)`), we want it to multiply default values of 6 and 7. This can be accomplished with slight modifications. The modified code, along with its call and sample output are below

    >def multiply(a = 6, b = 7):
        >return a * b

    >def main():    
        >product = multiply()
        >print("The product is %d." %product)

    The product is 42.

## The main() function

With that example in mind, it will be easier to understand what is happening in the `main()` function that was mentioned above. When Python runs a file, it runs sequentially through the file to find code to run. However, it does not go inside a function unless there is specific call to that function, so if your code is only functions, Python will not run anything. The convention is to execute code in the `main()` function that *calls* other methods, like we did above by calling `product()` in the main function above. But how does Python know to go into the `main()` function? It has a name property. Specifically, when run from standard input, a script, or an interactive prompt, a module's `__name__` is set to `__main__`. Essentially, running the `main()` function boils down to a conditional "idiom" which must be included to call `main()`

    >if __name__ == "__main__":
        >main()
These two lines are usually included at the end of a file. Unlike entry point languages like Java where you must declare `main()` in a specific way, you could replace the call to `main()` with a call to any other function. Python has no specified entry point, so it can be entered anywhere. However, I'll stick to convention by using the `main()`.

## Arguments

Python can easily handle multiple arguments of any object type. However, if a function needs more than 5 or 6 inputs, it's likely that it is trying to do too much or that an underlying object or data structure should be utilized.

Special care should be taken with the order of the arguments. Whatever order they take in the function definition, determines how you will call the function.

### Optional arguments

What if we want a limited number of the arguments to be optional? Python offers optional arguments, as demonstrated by this variant of the `multiply()` function above.

    >def multiply(a, b = 1, c = 1, d = 1, e = 1):
        >return a * b * c * d * e
When calling this function, you must give it at least one parameter, and at most five parameters, as demonstrated below by 5 different, legal calls and their outputs

    >def main():    
        >product = multiply(10)
        >product = multiply(10,2)
        >product = multiply(10,2,7)
        >product = multiply(10,2,7,9)
        >product = multiply(10,2,7,9,2)

    The product is 10.
    The product is 20.
    The product is 140
    The product is 1260.
    The product is 2520.
But this approach can also be clunky. What if we wanted to average the inputs, instead of multiply? There is no way to know how many optional parameters you have, so this would be impossible.

### Tuple packing and unpacking
What if want any number of arguments? Python offers tuple packing with a `*` operator. Here's how it works with the `multiply()` code

    >def multiply(*args):
        >product = 1
        >for element in args:
            >product *= element
        >return product

Looping through the elements like this is called argument tuple packing. Now, `multiply()` can be called with any number of arguments, as demonstrated below

    >def main():  
        >product = multiply()  
        >product = multiply(10)
        >product = multiply(10,2)
        >product = multiply(10,2,7)
        >product = multiply(10,2,7,9)
        >product = multiply(10,2,7,9,2)
        >product = multiply(10,2,7,9,2,...)
Each list of numbers is now a tuple. For example, in the fourth line, `multiply()` is passed a tuple with 3 elements: `(10,2,7)`. This approach is advantageous to optional variables because argument tuple packing allows the coder to calculate the number of arguments using `len(args)`. It is also important to note that `multiply()` can only take numeric inputs, anything else will produce an error.
The values of each respecitve `product` is given below

    The product is 1.
    The product is 10.
    The product is 20
    The product is 140.
    The product is 1260.
    The product is 2520. 

Going back to the original `multiply()` code, we can use the `*` operator to unpack the argument, allowing you to feed a single tupple to a function that accepts multiple arguments.

    >def multiply(a, b):
        >return a * b

    >def main():    
        factors = (6, 7)
        >product = multiply(*factors)
        >print("The product is %d." %product)

    The product is 42.

The `*` operator can be used on any iterable object in Python, like lists and sets.

### Dictionary packing/unpacking
Python also supports a `**` operator that is very similar to the `*` operator. The key difference is that `**` allows dictionary packing/unpacking. There is an example in 

## Recursive functions

Python supports recursive functions. Consider the simple recursive function to calculate the factorial of a given number, which can be found in [`functions_and_parameters.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/functions_and_parameters.py)

    >def factorial(n):
        >if  n == 1:
            >return n
        >else:
            >return n * factorial(n-1)
Let's break this down. 
- Its name is `factorial()`
- Its argument is `n`,
- Its returns the value of the factorial of `n`.
- The *base case* is `if  n == 1: return n`.
- The *recursive case* is `else: return n * factorial(n-1)` because it recalls the same function with a smaller argument.

It can be called through `main()`

    >def main():
        >n = 4
        >fac = factorial(n)
        >print("The factorial of %d is %d" %(n, fac))
It outputs

    The factorial of 4 is 24
To understand what this code is doing, use the table below
| n |          return                 |
|---|---------------------------------|
| 4 | return 4 * factorial(3)         |
| 3 | return 4 * 3 * factorial(2)     |
| 2 | return 4 * 3 * 2 * factorial(2) |
| 1 | return 4 * 3 * 2 * 1            |

For a more advanced recursive example, consider the code in [`fern_recursive.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/fern_recursive.py). It uses matrices from the package `numpy` to recursively generate the `(x,y)` coordinates of a fern. It also uses plotting tools from the `matplotlib` package that works like MATLAB. The fern generator also uses a "wrapper" function to begin the recursive function. An image of what it plots can be found here: [`fern_recursive.png`](https://github.com/danielleappel/Python-Tutorial/blob/main/Images/fern_recursive.png) and below:

![Recursive Fern Fractal](https://github.com/danielleappel/Python-Tutorial/blob/main/Images/fern_recursive.png)

Try changing the value of `n`; it determines the number of dots plotted. As the value of `n` decreases, the code will run quickly and the graph will be more sparse. If the value increases, the code will take longer to run, but the graph will be denser. Make sure not to make `n` too big! Python has a limit of 1000 on how many times a function can be recrusively called and thus put on the call stack. If you make `n` greater than 1000, it will crash because there are more stack frames than the default stack depth.

To get around this, we could certainly use the package `sys` to increase the recursion limit, but that does not address the root of the problem: Python does not support *tail call optimization*. Tail call elimination is designed to speed up recursion by allowing tail calls that eliminate the need to put a new stack frame on the call stack for each recursive call.

How can we make this function run for larger values of `n` without tail call optimization? The answer is to abandon recursion, and produce the much cleaner, iterative version of this code, which can be found here: [`fern_iterative.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/fern_iterative.py), and its corresponding image here: [`fern_iterative.png`](https://github.com/danielleappel/Python-Tutorial/blob/main/Images/fern_iterative.png) and below:

![Iterative Fern Fractal](https://github.com/danielleappel/Python-Tutorial/blob/main/Images/fern_iterative.png)

## Multiple return statements
A useful attribute of Python is that a function can return more than one value. The general form of this is

    >def function_name(argument1, argument2, ...):
        >statement1
        >statement2
        >...
        >return thing1, thing2, ...
It's simple enough, just seperate the different returns with commas. Consider the example below:

The following code in [`functions_and_parameters.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/functions_and_parameters.py) takes a string and splits it in half by indexing it like an array, then returns both halves. The subsequent call in `main()` is also shown

    >def string_split(s):
        >midpoint = len(s)//2
        >return s[ : midpoint], s[midpoint : ]

    >def main():
        >s = "Hello."
        >(first, second) = string_split(s)
        >print("The first half of the string %s is %s and the second half is %s" %(s,first, second))
        
        >t = "Goodbye."
        >result = string_split(t)
        >print("The two halfs of the string %s is %s" %(t, result))
This code outputs

    The first half of the string Hello. is Hel and the second half is lo.
    The two halfs of the string Goodbye. is ('Good', 'bye.')
The section with string `s`, assigns the two returned strings into two variables `first = 'Good'` and `second = 'lo.'`. On the other hand, the section with string `t` takes the result and assigns it to just one variable, a: `result = ('Good', 'bye.')`. If you set a single variable equal to a multiple return function, it will give you a list of all of the return values.

## Lambda expressions
Lambda expressions, often called anonymous functions, are a more compact version of functions than those listed above, using just the keyword `lambda`. These functions can include any number of arguments and a single expression to perform. The general form is

    >lambda argument1, argument2, ... : expression
Consider this example in [`functions_and_parameters.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/functions_and_parameters.py) that uses a lamda expression to create a multiply function

    >def make_multiplier(n):
        >return lambda x: x * n
    >def main():
        >mul_by_12 = make_multiplier(12)
        >print("Some multiples of 12 are: ", mul_by_12(0), mul_by_12(1), mul_by_12(2))
It prints 
    Some multiples of 12 are: 0 12 24
Where `0 = 0 x 12`, `12 = 1 x 12`, and `24 = 2 x 12`.

This may seem like a strange departure, but it is just syntactic sugar for a normal function statement.

## Pass-by reference vs. value

First, what is the difference between pass-by reference and pass-by value? 
    - Pass-by reference gives a reference to where a variable resides in memory.
        - Changes to the variable inside of a function will affect the value in the calling environment.
    - Pass-by value passes a copy of the original object to the function.
        - Changes to the variable inside of a function will not affect the value in the calling environment since it's just a copy.
With Python, however, this distinction is fuzzy. It is not pass-by reference, but can achieve that functionality. It is also not pass-by value either.

### A brief discussion of the scope of variables:
Python has two basic scopes: Local and Global. Local variables are defined in functions or loops, and are only accessible within the function or loop. Global variables on the other hand, can be accessed from anywhere in a file. 

### A brief discussion on object assignment:
When Python assigns a name to a variable, it is like having the name point at an object that hold the value of the variable:

    >x = 42
    >x = 3
This code has `x` point at an object that holds 42. Then `x` is unbound and rebound to an object holding 3.

### Back to pass-by type
A reference in Python behaves differently in Python than other languages. It does not point to a specific memory location, but rather, to an object.

Python sometimes behaves like a *pass-by reference* language. A list of numbers can have elements swapped, like this code in [`functions_and_parameters.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/functions_and_parameters.py):

    >def swap(A, i, j):
        >temp = A[i]
        >A[i] = A[j]
        >A[j] = temp
    >def main():
        >A = [1, 2, 3, 4]
        >swap(A,2,3)
        >print("A is: "A)
It outputs

    A is: [1, 2, 4, 3]
and succesfully swaps A[2] and A[3]. But it is not always so simple. Consider this loop that tries to change each value of A

    >for element in A:
        >element = 7
        >print(element)
    >print("A is: ", A)
It outputs

    i: 7
    i: 7
    i: 7
    i: 7
    A is: [1, 2, 4, 3]
It successfully assigns the value of `i` to be 7, but is unable to change the values of `A`. In the first execution of the for loop, `i` pointed to 1. It was then unbound, and rebound to point to 7. This code never actually changed `A` because the connection to the original object was lost. In this example, Python acted like a *pass-by value* language.

To successfully change the values of `A`, try this loop that specifically references `A`

    >for i in range(len(A)):
        >A[i] = 7
        >print("i: %d, A[i]: %d" %(i,A[i]))
    >print("A is: ", A)
which outputs

    i: 0, A[i]: 7
    i: 1, A[i]: 7
    i: 2, A[i]: 7
    i: 3, A[i]: 7
    A is: [7, 7, 7, 7]
In general, when Python passes 
1. immutable objects (like string, bool, int, long, tuple, etc.) Python *passes-by value*.
2. mutable objects (list, dictionary, set, et.) Python mostly *passes-by reference* (but cannot reassign the entire mutable object).

The thing to remember here is that functions in Python cannot change the value of an argument by reassigning the value of the local variable since the connection to the initial object is gone. Essentially, a function is passed a reference to an object, and this reference is passed by value. This is sometimes called *pass-by assignment*.

## Documentation strings

Python functions have their own form of comments to describe each function. While they are optional, writing good documentation strings is essential to writing good code in Python. The general form is

    >def function_name(argument1, argument2, ...):
        >"""Description of the function
        >
        >More information...
        >...
        >"""
There is a description of the function, followed by an intentionally blank line (if there is more to describe, otherwise the docstring can be just a single line) to seperate the high level description and the other information about the function. 

Docstrings are useful for people who are unfamiliar with your code. For instance, you can run a `help` command to understand the `multiply()` function in [`functions_and_parameters.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/functions_and_parameters.py)

    >help(multiply)

    Help on function multiply in module __main__:

    multiply(factor1, factor2)
        Return the product of two numbers.

        Keyword arguments:
        factor1 -- the first factor
        factor2 -- the second factor

### Annotations
There is also another special kind of commenting, called annotations. Sometimes they offer little information, but can be helfpul as labels of the various data types in the actual function. This information could also go in the docstring, but it is more recognizable inside the function. For example, consider this annotated version of `multiply()`

    >def multiply_annotated(factor1 : int = 7, factor2 : int) -> int:
    """Return the product of two numbers.

    Keyword arguments:
    factor1 -- the first factor
    factor2 -- the second factor
    """
        >return factor1 * factor2
`multiply_annotated` is syntactically equivalent to the earlier `multiply()` function (the compiler won't even care if you suddenly change the type of a variable that is declared to be another type via annotations) and gives the reader the gist of a function with just a glance. Notice also, if there is a default value for a variable, like for `factor1` above, it goes after the annotation.

### Side effects
Since Python can modify an mutable from within a function, changes inside the function also cause changes in the calling environment. This is called a side effect. Pay extra attention to these, and make sure to mention them in docustrings.

It is usually preferable to use `return` values to avoid side effects.

# Sources

- Docs.Python.org, https://docs.python.org/3/library/__main__.html, Accessed October 14, 2020.
- Docs.Python.org, https://docs.python.org/3/tutorial/controlflow.html, Accessed October 14, 2020.
- RealPython.com, https://realpython.com/python-pass-by-reference/, Accessed October 14, 2020.
- RealPython.com, https://realpython.com/python-main-function/, Accessed October 14, 2020.
- RealPython.com, https://realpython.com/python-thinking-recursively/, Accessed October 14, 2020.
- RealPython.com, https://realpython.com/defining-your-own-python-function/#pass-by-value-vs-pass-by-reference-in-pascal, Accessed October 14, 2020.
- TutorialsPoint.com, https://www.tutorialspoint.com/python/python_functions.htm, Accessed October 14, 2020.
- Wikipedia.org, https://en.wikipedia.org/wiki/Tail_call, Accessed October 14, 2020.
