# Control Flow
*Code for this lesson can be found at [`control_flow.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow.py), and extra examples of control structures can also be found at [`control_flow_perfect_num.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow_perfect_num.py) and [`control_flow_guessing_game.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow_guessing_game.py).*

As RealPython.com says, control flow "directs the order and execution of statements in the program." The structure of a general Python block:

    >block command:
        >statement1
        >statement2
        >...
    >next code...
The block commands dictates how and when the statements are run, and come in several flavors. We can have conditionals (if/else, switches), loops (for, while), and functions. Python decides when a block is finished by comparing whitespace (tabs). If the next line has less indentation, the statement/block is ended. In this case, the line with `next code...` is less indentented than the previous line, so Python knows only to start the `next code...` once all of the indented statements are executed and the block statement is over.

The code used in this post is in [`control_flow.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow.py). Try downloading the code and changing pieces of the code to better understand the structure.

# Conditionals
The most general structure of a conditional block is

    >if boolean_statement:
        >statement1
        >statement2
    >else:
        >statement3
        >statement4
If the boolean_statement is true (like `14 == 12+2` or even just the Boolean value - `True`), `statement1` and `statement2` will be executed. If the Boolean statement is `False`, `statement3` and `statement4` will be executed.

## One-condition if/elif/else statement
Consider the following problem. We want to check if a person's `lottery_ticket` is equal to 10. If it is, we want to print that they won! If their ticket has any other number, they have lost, so we print try again. This can be implemented using the code below

    >lottery_ticket = 10
    >if lottery_ticket == 10:
        >print("You win!\n")
    >else:
        >print("Try again.\n")
And this code will output

    You win!
If you change the first line to read `lottery_ticket = 7` (or any other number, as long as you do not choose 10), the code will output

    Try again.

We can also use `if` statements with lists. Imagine that we have a list of registered students, and we want to check if Jessica is registered. We can achieve this with an `if` statement.

    >students = ["Jessica","Bella","Sam","Juan"]
    >if "Jessica" in students:  # one line if
        >print("Jessica is registered for classes.\n")
    >print("Done with the if, even if Jessica isn't in the list, this statement will print.")
This outputs:

    Jessica is registered for classes.
    Done with the if, even if Jessica isn't in the list, this statement will print.
This `if` statement also differs from the previous because it has no `else` clause. An `else` clause is not required in Python, so this is a perfectly legal conditional statement. The second print statement (after the conditional statement is *over*) will execute whether Jessica is registered or not.

We can also make other changes, like negating the a Boolean value with the `~`. This can make code more readable. Consider a restaurant with a fixed capacity. If it is not at capacity, then we can seat new customers:

    >at_capacity = False
    >if ~ at_capacity: print("We can seat you now.\n")
This prints

    We can seat you now.
This statement also demonstrates that short `if` clauses can be executed on a single line, but do this thoughtfully because it can make your code less readable. 

If we have an `if` statement with multiple cases, it might be useful to have an else-if statement. Python provides this functionality with an `elif`. There is a subtle difference between `if` and `elif` statements. Multiple `if` statements can be executed if they are all true, but an `elif` statement can only be executed if none of the preceding `if`/`else` statements in the same block have been true.

    >temp = 81
    >if temp > 80:
        >print("We could go to the beach!")
    >if temp > 70:
        >print("We could go for a walk.")
    >elif temp > 60:
        >print("We could go for a run")
    >elif temp > 65:
        >print("We could bike.)
    >else:
        >print("It's too cold.")
It prints:

    We could go to the beach!
    We could go for a walk. 
The only time the first `elif` statement will ever be executed is if `temperature` is greater than 60 degrees and less than 70 degrees, so that all preceding statements are false. The second `elif` statement will *never* be executed because if `temperature > 65`, then clearly `temperature > 60` too and since a previous statement was true, the second `elif` will be skipped.

## Multi-statement if/elif/else clause
There is another type of `if` statement in Python that allows you to check a condition and if it is true, execute multiple statements, otherwise execute another set of statements:

    >month = 11
    >if month == 12: print("It's December"); print("It's still December"); print("It's really still December\n")
    >if month == 11: print("It's November"); print("It's still November"); print("It's really still November\n")
It prints

    It's November
    It's still November
    It's really still November
Since `month` is not equal to 12, none of the print statements after it are executed. Instead, since `month==11`, all three November print statements are executed. The general form of this statement is

    >if boolean_statement: statement1; statement2; statement3
    >else: statement4; statement5; statement6
If the `boolean_statement` is true, all `statement1`, `statement2`, and `statement3` will be execused. Otherwise, execute `statement4`, `statement5`, and `statement6`.

## Multi-condition if/elif/else statement
We can add requirements from the lottery example above. All winners must be 18 years of age or older:

    >lotter_ticket == 10
    >age = 14
    >if lottery_ticket == 10 and age >= 18:
        >print("You win!\n")
    >elif lottery_ticket == 10:
        >print("You won, but you're too young to collect your prize :(\n")
    >else:
        >print("Try again.\n")
This would output

    You won, but you're too young to collect your prize :(
We could even add more conditions. Imagine now that you can only win the lottery with a winning ticket, and either be of age, or be with a guardian:

    >has_guardian = True
    >if lottery_ticket == 10 and (age >= 18 or has_guardian):
        >print("You win!\n")
    >elif lottery_ticket == 10:
        >print("You won, but you either need a guardian or you need to come back when you're older.\n")
    >else:
        >print("Try again.\n")
Which would now output

    You win!
because ticket matches and even though the player is less than 18, they brought a guardian, and may collect their prize.

Python is a short-circuit evaluation language - which means that it only executes multiple conditions if they are absolutely necessary to calculate the boolean value. 

These multi-condition `if` statements narrowly avoid an error by utilizing the short-circuit evaluation structure of Python to avoid division by zero:

    >age = 22
    >if age == 22 or 1/0 == 2345:
        >print("You win! (and thankfully didn't divide by zero!)\n")
    >else:
        >print("Try again.\n")
Since this uses an `or` statement, if the first condition is true, then the second does not need to be evaluated. It outputs

    You win! (and thankfully didn't divide by zero!)
If `age == 23` (or any other number), the expression `1/0` will be evaluated, which would cause an error.

We can play the same game with `and` statements. If the first condition is false, then the whole thing must be false. So as long as `age` is not equal to 16, there will be no error

    >if age == 16 and 1/0 == 2345:
        >print("You win! (but actually, this is impossible.)\n")
    >else:
        >print("Try again. (but at least you didn't divide by zero!)\n")
It outputs:

    Try again. (but at least you didn't divide by zero!)

## Nested if statements
Nested `if` statements are extremely intuitive in Python. Take the following code example to calculate details about a dog

    >weight = 12.3
    >height = 5
    >if (weight > 10):
        >if (height > 5.5):
            >print("Your dog is tall and heavy.")
        >else:
            >print("Your dog is short and heavy.")
    >else:
        >if (height > 5.5):
            >print("Your dog is tall and thin.")
        >else:
            >print("Your dog is short and thin.")

It outputs 

    Your dog is very short and stocky.
It works by evaluating for 4 different possibillities. It first check the height for being tall or short, and then checks the weight to see if the dog is tall or short, and prints the result. 

## The ternary operator of Python
Other languages, like Java and C have ternary operators that operate as follows

    >boolean_statement? statement 1: statement 2;
Python has a similar operator, but it is a little different. It's basic structure is

    >statement1 if boolean_statement else statement2

The following code expresses this using Python's "ternary" operator. If a shopper has less than 15 items, then they may use the express lane.

    >num_items = 14
    >print("Please proceed to the", "regular lane.\n" if (num_items > 15) else "express lane.\n")
which outputs

    Please proceed to the express lane.
Equivalently, we can invert `statement1` and `statement2` and use Python's `if not` version of the ternary operator:

    >print("Please proceed to the", "express lane.\n" if not (num_items > 15) else "regular lane.\n")
Not surprisingly, it also outputs

    Please proceed to the express lane.
The following code uses the ternary operator to assign a value to `x` and `y`, and then computes |x|+|y| with the piecewise definition of the absolute value function

    >x = 12 if (42 == 42) else 14
    >print("x is %d.\n" %x)

    >y = -15
    >z = (-y if (y < 0) else y) + (-x if (x < 0) else x)
    >print("|%d|+|%d| = %d.\n" %(x,y,z) )
And yields

    |12|+|-15| = 27.
In effect, it chooses `x` to be equal to 12 (because clearly 42==42 is always `True`). It assigns -15 to `y`, and then takes the absolute value of each number with a ternary statement.

## Dangling else
In some programming languages, it is possible to have a "dangling else" problem as illustrated by some psuedo code below

    >if (boolean_value1)
        >statement1;
        >... ;
    >if (boolean_value2)
        >statement3;
        >... ;
    >else
        >statement1;
        >... ;
The problem is that the code above is ambiguous. It is unclear which `if` statement the `else` belongs with. Could these be nested `if` statements? Clearly, this is a problem. Python sidesteps this problem entirely by utilizing the whitespace. Nested `if` statements must be indented more than the outer statement

# Loops

The general structure of Python loops are

    >for/while boolean_value:
        >statement1
        >statement2
        >...
Consider this simple loop. It calculates the `factorial(n)=n!`

    >factorial = 1
    >n = 5
    >while n > 1:
        >factorial *= n
        >n -= 1
    >print("The factorial of 5 is %d\n" %factorial)

| n | factorial |
|---|-----------|
| 5 |     5     |
| 4 |     20    |
| 3 |     60    |
| 2 |     120   |

It counts from 5 down to 1 (although is not executed when `n=1` because `n` is not greater than 1) and multiplies `factorial` by `n` each time. It outputs

    The factorial of 5 is 120

Keep in mind that `while` loops check the condition at the beginning of the loop. What will this code output? How many times will the loop run?

    >num_buckets = 0
    >while num_buckets >= 1:
        >num_buckets -= 1 
    >print("There are %d buckets left\n" %num_buckets)
It will output

    There are 0 buckets left
because it doesn't meet the condition `0 >/= 1`, the loop never runs.

On the other hand, what will the result of this code be?
    
    >num_buckets = 0
    >while num_buckets >= 0:
        >num_buckets += 1    
    >print("There are %d buckets left\n" % num_buckets)
This code will actually never stop running. It is an *infinite loop*. It starts when `buckets = 0`, and enters the `while` loop. It is then incremented, and thus will always be greater than or equal to 0. This code is commented out in [`control_flow.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow.py) so as to allow the rest of the code to run, but try running it and see what happens!

## For loops
Many languages, like Perl and Java offer two seperate commands: `for` and `foreach`. Python, offers the functionality of both commands with just the keyword `for`.

Consider this first simple `for` loop that compute the sum of squares of numbers less than 15

    >sum_of_squares = 0
    >for i in range(1,15):
        >sum_of_squares += i**2
    >print("The sum of the squares up to 14^2 is: %d\n" %(sum_of_squares))
What are the values of `i` and `sum_of_squares` as this runs?

| n   | sum_of_squares |
|-----|----------------|
| 1   |     1          |
| 2   |     5          |
| 3   |     14         |
| ... |     ...        |
| 14  |     1015       |

It indexes from 1 up to 14 and squares that index, adding it onto `sum_of_squares` for each index. It outputs

    The sum of the squares up to 14^2 is: 1015
The `foreach`/iterable functionality can be easily achieved using a list. Imagine we want to loop through each element in a list of Christmas movies and print each title
    >print("My favorite Christmas movies are:")
    >christmas_movies = ["The Grinch", "Home Alone", "Elf"]
    >for movie in christmas_movies:
        >print(" %s" %movie)

which prints
    My favorite Christmas movies are:
        The Grinch
        Home Alone
        Elf.

This functionality can also be applied to each character in a string

    >word = "dog"
    >for letter in word:
        >print(letter)

Not surprisingly, this code yields

    d
    o
    g
A possible limitation of this approach can occur if we wanted to loop through the characters, and we also needed the index value, but can easily be resolved by looping like this

    >word = "dog"
    >for i in range(len(word)):
        >print("Letter %d is %s" %(i,word[i]))
This code prints both the index and the character at that index

    Letter 0 is d
    Letter 1 is o
    Letter 2 is g
We can also loop over every element in a dictionary in Python. The following code uses a dictionary to store information about a car, and uses a `for` loop to print all of the details

    >print("\nMy car details are as follows:")
    >car = {
        >"Make": "Lexus",
        >"Model": "CT200H",
        >"Year": "2011",
        >"Color": "red"
    >}
    >for trait in car:
        >print(" %s: %s" %(trait, car[trait]))
This code prints

    My car details are as follows:
        Make: Lexus
        Model: CT200H
        Year: 2011
        Color: red

## Nested for loops
To represent a 2D space, we can use a nested for loop to iterate over all every row in each column. The following code demonstrates this by printing a design

    >for col in range (5):
        >stars = ""
        >for row in range(col):
            >stars += "*"
        >print(stars)
and makes this 2D pattern

    *
    **
    ***
    ****

## Switch/case statements
While Python does not have a built-in `switch` statement, a similar effect can be achieved by using a dictionary

    >grade = 7
    >switch = {
        >"1" : "F",
        >"2" : "F",
        >"3" : "F",
        >"4" : "F",
        >"5" : "F",
        >"6" : "D",
        >"7" : "C",
        >"8" : "B",
        >"9" : "A",
        >"10" : "A+"
    >}
    >letter_grade = switch[str(grade)]
    >print("\nMinnie's grade this quarter is %s.\n" %letter_grade)
and assigns the student a letter grade based on the digit of their grade (integers from 1 to 10, inclusive).

    Minnie's grade this quarter is C.

The ternary operator is also very useful for checking multiple conditions to function like a `switch` statement

    >season = ("spring" if (3 <= month <= 5) else 
                >"summer" if (6 <= month <= 8) else
                >"fall" if (9 <= month <= 11) else
                >"winter"
                >)
    >print("Welcome to the", season, "season.\n")
Which prints 

    Welcome to the fall season.

## Break and continue statements
Sometimes it can be beneficial to have no code under a conditional or a loop, but Python requires there to be at least one statement. You might also need to exit a conditional or loop before the conditions to exit are met. To achieve these goals, Python provides break, continue, and pass statements.

Consider looping through each element from 2 to 7, inclusive. If the element % 4 == 1, we want to print a statement and then exit the loop. Otherwise, add the value of the element to `y`.

    >y = 0
    >for x in range(2,8):
        >if x % 4 == 1:
            >print("About to break...\n")
            >break
        >else:
            >y += x
            >print("x = %d, y = %d" %(x, y))
This code prints

    x = 2, y = 2
    x = 3, y = 5
    x = 4, y = 9
    About to break...
It continues looping for `x = 2, 3, 4` and then exits when `x = 5` because `5 % 4 == 1`.

We can also use a break to stop a loop at the first instance of something. The code below prints all of the leap years until a future year is reached or a leap year is found that is both divisible by 100 and by 400

    >curr_year = 1980
    >future_year = 2020
    >while curr_year <= future_year:
        >curr_year += 1
        >if curr_year % 4 == 0:
            >if curr_year % 100 == 0 and curr_year % 400 == 0:
                >print("%d is a leap year." %curr_year)
                >break
            >elif curr_year % 100 != 0:
                >print("%d is a leap year." %curr_year)
        >else:
            >continue
            >print("This will never run")
The `break` makes sure that the loop is ended after the first leap year that is divisible by 100 and 400. The `continue` handles all of the years that are not divisible by 4 because they clearly cannot be leap years, so we continue to the next loop value immediately. Any code below it will never be executed as you can see in the output of this code

    1984 is a leap year.
    1988 is a leap year.
    1992 is a leap year.
    1996 is a leap year.
    2000 is a leap year.

## Pass statements
Python also provides a similar statement: `pass` statements. They differ from `continue` statements by not forcing the next loop value to begin, and instead allow more statements to follow after them, like in this code

    >x = 15
    >sum_of_evens = 0
    >while (x > 1):
        >if (x%2 == 1):
            >pass
            >print("Pass %d" %x)
        >else:
            >sum_of_evens += x
        >x -= 1
    >print("\nThe sum of even numbers less than or equal to 15 is: %d" %sum_of_evens)
It prints

    Pass 15
    Pass 13
    Pass 11
    Pass 9
    Pass 7
    Pass 5
    Pass 3

    The sum of even numbers less than or equal to 15 is: 56
because this code uses a pass, it is still allowed to execute the `print` command that falls after it.

The benefit of using a pass statement can be most readily seen in this broken code

    >x = 15
    >sum_of_evens = 0
    >while (x > 1):
        >if (x%2 == 1):
        >else:
            >sum_of_evens += x
        >x -= 1
    >print("\nThe sum of even numbers less than or equal to 15 is:", sum_of_evens)
This code cannot be run because it has no statement after the `if`. It is commented out in [`control_flow.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow.py) because it results in an error. However, if you add a `pass` (but don't use a `continue` loop here or you'll get an infinite loop because `x` would never be decremented) after the `if` line, this code will run perfectly.

# More examples
I have written a number of other codes in this repository, called [`control_flow_guessing_game.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow_guessing_game.py) and [`control_flow_perfect_num.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow_perfect_num.py). Check them out! They also play with the control structures of functions in Python. The general structure of a function is

    >def function_name( input1, input2, ... ):
        >statement1
        >statement2
        >...
If a Python document has no functions, (like the code in [`control_flow.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow.py) ), it runs  mostly sequentially; top to bottom, executing each block (the only exceptions to the sequential flow is when the loops run). 

On the other hand, the code in [`control_flow_perfect_numb.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow_perfect_num.py) executes the loop in the `main()` function first, and then calls the `is_perfect()` function on the natural numbers from 1 to 500.

The code in [`control_flow_guessing_game.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/control_flow_guessing_game.py) uses loops and conditionals to host a simple guessing game. It even uses time delays with the code `time.sleep(0.5)` (but they only make it run more smoothly, they do not change the functionality). It also utilizes another Python feature: `try`/`except` statements which allow you to try something that might cause an error. If it does cause an error, then you can use a while loop to continue asking for input until the user enters the type of input you want.

# Sources
- Book.pythontips.com https://book.pythontips.com/en/latest/ternary_operators.html Accessed October 2, 2020.
- Docs.Python.org https://docs.python.org/3/reference/compound_stmts.html Accessed Ocotober 2, 2020.
- Docs.Python.org https://docs.python.org/3/tutorial/errors.html Accessed Ocotober 2, 2020.
- RealPython.com https://realpython.com/python-conditional-statements/#one-line-if-statements Accessed October 2, 2020.
- RealPython.com https://realpython.com/python-while-loop/ Accessed October 2, 2020.
- Wikipedia.org https://en.wikipedia.org/wiki/Short-circuit_evaluation#:~:text=Short%2Dcircuit%20evaluation%2C%20minimal%20evaluation,the%20expression%3A%20when%20the%20first Accessed October 2, 2020.
