# Naming, scope, and binding

## Using the same name
### In a for-loop
Consider the following code and its output in [scope_binding.py](https://github.com/danielleappel/PLP/blob/master/PLP6/scope_binding.py)

    >def main():
        >x = 7
        >print("x before the for loop is %d" %x)
        >for x in range(10):
            >print("  x inside the for loop is %d" %x)
        >print("x after the for loop is %d" %x)

    x before the for loop is 7
      x inside the for loop is 0
      x inside the for loop is 1
      x inside the for loop is 2
      x inside the for loop is 3
      x inside the for loop is 4
      x inside the for loop is 5
      x inside the for loop is 6
      x inside the for loop is 7
      x inside the for loop is 8
      x inside the for loop is 9
    x after the for loop is 9
The first thing to happen in `main()` is an assignment of the variable `x` to the integer value 7. Then the value of `x` is reassigned to the values 0 through 9 sequentially as the loop progresses. Since 9 is that last value assigned to `x` in the loop, it is the new value of `x` even after the loop terminates. In short, we successfully updated the value of `x` from within a for loop.

Similarly, this next code excerpt also in [scope_binding.py](https://github.com/danielleappel/PLP/blob/master/PLP6/scope_binding.py) reassignes the value of `sum` throughout a loop

    >def main():
        >sum = 0
        >print("sum before the for loop is %d" %sum)
        >for x in range(10):
            >sum += x
            >print("sum of the first %d terms is %d" %(x, sum))
        >print("sum after the for loop is %d" %sum)
And the output is

    sum before the for loop is 0
      sum of the first 1 terms is 1
      sum of the first 2 terms is 3
      sum of the first 3 terms is 6
      sum of the first 4 terms is 10
      sum of the first 5 terms is 15
      sum of the first 6 terms is 21
      sum of the first 7 terms is 28
      sum of the first 8 terms is 36
      sum of the first 9 terms is 45
      sum of the first 10 terms is 55
    sum after the for loop is 55
Again, we successfully edited the value of `sum` from within a for loop.

### In a function
Consider this `square()` function and the code that calls it in `main()` in [scope_binding.py](https://github.com/danielleappel/PLP/blob/master/PLP6/scope_binding.py)

    >def square(n):
        >x = n * n
        >print("  x inside square(y) is %d" %x)
        >return x

    >def main():
        >x = 9
        >y = 11
        >print("y before square(y) is %d" %y)
        >print("x before square(y) is %d" %x)
        >result = square(y)
        >print("y after square(y) is %d" %y)
        >print("x after square(y) is %d" %x)
        >print("And the result of square(y) is %d" %result)
It outputs

    y before square(y) is 11
    x before square(y) is 9
      x inside square(y) is 121
    y after square(y) is 11
    x after square(y) is 9
    And the result of square(y) is 121
There are two different scopes at play here: the `main()` block and the `square()` block. Each one defines a variable `x`, but they assign it different values. In `main()`, `x = 9`. However, in `square()`, `x` is defined as `11 * 11 = 121`. The interesting part is that this assignment does not affect the scope in `main()` after `square()` finishes running. The value of `x` in `main()` is still 9.

Essentially, changing a variable (as long as it does not contain the word `global` or `nonlocal`) within a function will *not* change variables of the same name that are in other functions.

## Globally accessible variables
Unlike some coding languages, in functions, Python assigns the default variable type as local, unless otherwise specified by the `global` or `nonlocal` keywords. This is to mitigate *side effects* since changes to local variables within a function or loop will not affect the variables in the rest of the program.

On the other hand, if a variable is declared outside of a function (like the line `z = 4` at the top of [scope_binding.py](https://github.com/danielleappel/PLP/blob/master/PLP6/scope_binding.py)), then it is automatically a `global` variable.

To illustrate how this actually works, consider the following code and its output

    >z = 4
    >def foo():
        >print("z inside foo() is %d" %z)

    z inside foo() is 4
Here, we are able to access the, in this case, global value of `z` from within `foo()` to print its value. However, if we try to change the value of `z`, we will no longer be allowed to access the global value of `z` without declaring it as global.

This code yields the following error

    >z = 4
    >def double():
        >print("  z inside double() before doubling is %d" %z)
        >z *= 2
        >print("  z inside double() after doubling is %d" %z)

    >main():
        >double()

    UnboundLocalError: local variable 'z' referenced before assignment
To make this code work, we need to tell Python that the variable `z` is a global variable by using the keyword `global` as demonstrated below

    >z = 4
    >def double():
        >global z
        >print("  z inside double() before doubling is %d" %z)
        >z *= 2
        >print("  z inside double() after doubling is %d" %z)

    >main():
        >double()
And outputs

    z inside double() before doubling is 4
    z inside double() after doubling is 8
Since `z` is a global variable, we are able to change it from within the `double` function. You can check that the value of `z` really changed by accessing the global variable `z` in `main()`

    >double()
    >global z
    >print("global z after double() is %d" %z)

      z inside double() before doubling is 4
      z inside double() after doubling is 8
    global z after double() is 8

### Nested global variable
If we wanted to use a nested function and the `global` keyword, interesting things start to happen. Consider this variation of the code for `double()` above

    >def double_wrapper_global():
        >m = 10
        >def double_global():
            >global m
            >print("  nested global m before doubling is %d" %m)
            >m *= 2
            >print("  nested global m after doubling is %d" %m)
        >print("local m before doubling is %d" %m)
        >double_global()
        >print("local m after doubling is %d" %m)

    >def main():
        >double_wrapper_global()
        >global m
        >print("global m after double_wrapper_global() is %d" %m)
And it outputs 

    (1) local m before doubling is 10
    (2)   nested global m before doubling is 42
    (3)   nested global m after doubling is 84
    (4) local m after doubling is 10
    (5) global m after double_wrapper_global() is 84
There are three scopes in the call to `double_wrapper_global()`: the scope of `main()`, `double_wrapper_global()`, and `double_global()`. In `double_wrapper_global()`, a local variable `m = 10` is created. This explains the output of line (1) above. When `double_global()` is called, it binds `m` to the global variable `m = 42` that is declared at the top of [scope_binding.py](https://github.com/danielleappel/PLP/blob/master/PLP6/scope_binding.py), resulting in line (2) above. The value of `m` in `double_global()` is then doubled to equal 84. Any other variables referencing the global `m` will also now be equal to 84. That's where the two outputs of 84 in line (3) and (5) come from. Line (4), on the other hand, reflects the value of `m` that is in the scope of `double_wrapper_global()` - it only has a copy of the local variable `m` which equals 10 here. Therefore, the local `m` is unchanged.

## Non-local variables
As a parallel to global type, Python also supports non-local variables inside of nested functions. It's similar to the global type since it allows you to access variables outside of their normal scope, but its access more limited. The `nonlocal` keyword causes the respective variable to be bound to a previously bound variable in the closest proceeding scope (excluding global variables). 

Consider a third variation of the `double()` code:

    >def double_wrapper_nonlocal():
        >n = 35
        >print("n in double_wrapper_nonlocal() before double_nonlocal() is %d" %n)
        >def double_nonlocal():
            >nonlocal n
            >print("  n in double_nonlocal() before doubling is %d" %n)
            >n *= 2
            >print("  n in double_nonlocal() after doubling is %d" %n)
        >double_nonlocal()
        >print("n in double_wrapper_nonlocal() after double_nonlocal() is %d" %n)

    >def main():
        >double_wrapper_nonlocal()
    
    n in double_wrapper_nonlocal() before double_nonlocal() is 35
      n in double_nonlocal() before doubling is 35
      n in double_nonlocal() after doubling is 70
    n in double_wrapper_nonlocal() after double_nonlocal() is 70
In `double_wrapper_nonlocal()`, a local variable `n = 35` is declared before calling the nested function `double_nonlocal()`. By declaring `n` to be a nonlocal variable in the inner function `double_nonlocal()`, it can point to the same value of 35 as declared in the outer function. We can even change the value of `n` in both the inner function `double_nonlocal()`, and the wrapper `double_wrapper_nonlocal()` to be 70 since they point to the same object.

## Assignment
As discussed in [PLP5-Functions_and_Parameters.md](https://github.com/danielleappel/PLP/blob/master/PLP5/PLP5-Functions_and_Parameters.md), Python passes mutable objects (like lists) by reference and immutable objects (like ints, strings, and tuples) by value. The difference between the two can be seen in two similar examples: one with a list, and one with a tuple.

### With a list
Consider the following code and its output in `main()` in [scope_binding.py](https://github.com/danielleappel/PLP/blob/master/PLP6/scope_binding.py)

    >a = ["c","a","t"]
    >b = ["d","o","g"]
    >print("a before changes is %s" %a)
    >print("b before changes is %s" %b)
    >a = b
    >b[1] = "u"
    >print("a after changes is %s" %a)
    >print("b after changes is %s" %b)

    a before changes is ['c', 'a', 't']
    b before changes is ['d', 'o', 'g']
    a after changes is ['d', 'u', 'g']
    b after changes is ['d', 'u', 'g']
Lists are passed by reference in Python, so when we assign `a = b`, it assigns the variables `a` and `b` to both point to the same object in memory. So when we change `b`, it also changes `a`.

### With a tuple
Conversely, changing a tuple will create a new object, as demonstrated below

    >c = ("c","a","t")
    >d =("d","o","g")
    >print("c before changes is ", c)
    >print("d before changes is ", c)
    >c = d
    >d += ("s",)
    >print("c after changes is ", c)
    >print("d after changes is ", d)

    c before changes is  ('c', 'a', 't')
    d before changes is  ('c', 'a', 't')
    c after changes is  ('d', 'o', 'g')
    d after changes is  ('d', 'o', 'g', 's')
When we assigne `c = d`, the two variables `c` and `d` both point to the same object in memory briefly. However, as soon as we make changes to either object, this will no longer be the case. Adding `"s"` to the end of `d` makes `d` point to the newly created tuple with 4 elements. In this case, Python passes-by-value.

## Sources
- Docs.python.org, https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python, Accessed October 26, 2020.
- Docs.python.org, https://docs.python.org/3/reference/simple_stmts.html, Accessed October 26, 2020.
- Medium.com, https://medium.com/broken-window/many-names-one-memory-address-122f78734cb6, Accessed October 26, 2020.
- Programiz.com, https://www.programiz.com/python-programming/global-keyword, Accessed October 26, 2020.
- W3schools.com, https://www.w3schools.com/python/ref_keyword_nonlocal.asp, Accessed October 26, 2020.


