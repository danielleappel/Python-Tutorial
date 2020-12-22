# Naming conventions and data types

Code for this section is provided in [`data_types.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/data_types.py) in the Code folder.

## But first, a quick note on conventions
While the following rules and conventions usually leads to better code (as in more readable and easier to debug), they are not all fast and steady rules. Furthermore, not everyone follows these conventions, but they are a good place to start.

## Naming conventions

### General
* Avoid general names
* Avoid wordy names
* Names can contain letters - lower and uppercase
* Names can contain digits (but not as the first character)
* Names can contain underscores (and even begin/end with underscores, but these have special meanings).

The most important thing to remember is to strike a balance between specificity and brevity.

For example, don't use `numbers` (too general, could be numbers for *anything*) or `list_of_my_tracking_numbers_for_my_packages` (this name is far too long), try `tracking_numbers`.

### Function and variable names
PEP 8 (the Python Enhancement Proposal) suggests that function and variable names should be all lowercase with underscores to separate words as necessary, but this is not enforced by the interpreter.

### Naming constants 
Constants are usually written in all capitals with underscores to separate words as necessary, for example `MAX_CAPACITY` or `TOTAL`.

### Class names
PEP 8 recommends using CapWords/CamelCase convention, for example `StudentAdmin`.

## Data types
Python does not require code to declare the type of a variable, so writing code is fast andd simple. Variables of one type can also be changed to any value of any data type because Python is ***dynamically typed***. In other words, variables can change type.

Python is also ***strongly typed*** because the interpreter keeps track of all of the variable types in code. It prevents you from doing something like adding a string to a number because there is no definition for that operator. The benefit of a strongly typed language is that it provides error messages so that the coder can realize that they are performing undefined operations on their variables.

Consider the code in [`data_types.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/data_types.py) as an example of the dynamic aspects of Python

    >x=7
    >print("\n",x)
    
    >x="rain"
    >print(x)
Above, `x` starts as an integer, and is then reassigned to a string. This code outputs

      7
      rain
### Integers
Consider this excerpt from [`data_types.py`](https://github.com/danielleappel/Python-Tutorial/blob/main/Code/data_types.py)

      >fall_goals = 14
      >spring_goals = 19
      >total_goals = fall_goals + spring_goals

      >print ("\nIn the fall, the soccer team scored ",fall_goals," goals. In the spring, they scored ",spring_goals, " for a total of ",total_goals," goals.")
This code outputs

      In the fall, the soccer team scored  14  goals. In the spring, they scored  19  for a total of  33  goals.
Clearly, an integer can be added to an integer in Python.

### Floats

First, consider two floats, can we add them?

      >oz_honey = 1/3
      >oz_agave = 2.1
      >oz_sweetener = oz_honey + oz_agave

      >print("\nThere are ",oz_sweetener," ounces of sweetener")
Yes we can. The code outputs

      There are  2.4333333333333336  ounces of sweetener
Can we turn a float into an integer? Yes, the following code takes the value stored in `oz_sweetener` and narrows the float to make it an integer

      >oz_sweetener_rounded = round(oz_sweetener)
      >print("\nOr ",oz_sweetener_rounded," ounces, rounded.")
It outputs

      Or  2  ounces, rounded.
Now, consider a float and an integer. From `data_types.py`

      >weight = 12
      >weight_gain = 2.2
      >final_weight = weight + weight_gain

      >print ("\nThe penguin's initial weight was ",weight, " lbs. She gained ",weight_gain," pounds to weight a total of ",final_weight," lbs.\n")
This code outputs

      The penguin's initial weight was  12  lbs. She gained  2.2  pounds to weight a total of  14.2  lbs.
Clearly, the sum of a float (`2.2` in this case) and an integer (`12` here) is a float (`14.2`).

### Strings
The following code fragment from `data_type.py` demonstrates how to create strings

      >greeting_1 = "Hello."
      >greeting_2 = "Hi!"
      >greeting_3 = greeting_1+" "+greeting_2
      
      >print(greeting_3)
It prints

      Hello. Hi!
In Python, strings can be concatenated together by addition. creating `greeting_3` actually concatenates 3 strings together:
1. `greeting_1` ("Hello.")
2. `greeting_2` ("Hi!)
3. a one space string (" ")

A string however cannot be added to numerical values. Can we add a string to an integer?
      
      >sentence = "The quick brown fox jumps over the lazy dog."
      >int_value = 16
      >x = sentence + int_value
No. Python will not allow `sentence` to be added to `int_value` because an integer cannot be added to a string, no matter how much we play with it, it will not work. If `sentence` contained numbers, it could be cast as an integer or float and added to `int_value` (See `Type Conversions` below), but this cannot be done here.

      Traceback (most recent call last):
      File ".\data_types.py", line 45, in <module>
      x = sentence + int_value
      TypeError: can only concatenate str (not "int") to str
Likewise, adding a float to a string is forbidden as demonstrated by this code and it's output.

      >float_value = 16.5
      >y = sentence + float_value

      Traceback (most recent call last):
      File ".\data_types.py", line 48, in <module>
      y = sentence + float_value
      TypeError: can only concatenate str (not "float") to str
Since these lines cause errors, they have been commented out in the file `data_types.py`.

### Booleans
Booleans in Python or represented as either `True` or `False`. The following code utilizes Boolean values and given with each output beneath the respective code.

      >won_game = True
      >if won_game:
          >print("\nCongratulations! You won the  game.\n")
      >else:
          >print("\nYou lost the game. Play again  soon!\n")

      Congratulations! You won the game.
      
      >paid_in_advance = False
      >print("It is ",paid_in_advance," that you have paid in advance.")

      It is  False  that you have paid in advance.
Operations can be performed on these booleans, where addition represents a logical or and multiplication represents a logical and

      >print("\nTrue or False is ", won_game + paid_in_advance, " (True)")
      True or False is  1  (True)


      >print("\nTrue and False is ", won_game * paid_in_advance," (False)")
      True and False is  0  (False)

A boolean can be added to both integers and floats. The boolean value is a `0` if it is `False` and a `1` if it is `True`

      >print("\n",int_value," + True gives", int_value + bool_value)
      10 + True gives 11


      >print("\n",float_value," + True gives", float_value + bool_value)
      12.2 + True gives 13.2

On the other hand, the following code cannot be run because a boolean cannot be added to a string. No matter how much we play with it, it will not work. If the string contains numbers, it can be cast as an integer or float or boolean (See `Type Conversions` below) and added, but that is not the case here. The error message this code produces is also below.

      >print(sentence + bool_value)

      Traceback (most recent call last):
      File "c:/Users/danie/OneDrive/Desktop/Simmons/CS330/PLP/Python/data_types.py", line 65, in <module>
      print(sentence + bool_value)
      NameError: name 'sentence' is not defined

### Arrays
Arrays are simple to create and use in Python. The following creates two arrays of strings and then adds them together. The output is also below

      >fast_food = ["Burger King","Wendy\'s","McDonald\'s"]
      >print("\nThe fast food restaurants are: ",fast_food)

      The fast food restaurants are:  ['Burger King', "Wendy's", "McDonald's"]
      
      >sit_down = ["Red Robin", "Olive Garden", "PF. Chang\'s"]
      >print("\nThe sit down restaurants are: ",sit_down)

      The sit down restaurants are:  ['Red Robin', 'Olive Garden', "PF. Chang's"]
      
      >restaurants = fast_food + sit_down
      >print("\nAll of the restaurants are: ",restaurants)

      All of the restaurants are:  ['Burger King', "Wendy's", "McDonald's", 'Red Robin', 'Olive Garden', "PF. Chang's"]
Clearly, adding arrays of strings together just concatanates the arrays.

Now, let's try making an array of numbers. I'm going to use both integers and floats in the array.

      >dog_weights = [60,13,20,71,45,10.6,87]
      >print("\nThe dogs weights are: ",dog_weights)

      The dogs weights are:  [60, 13, 20, 71, 45, 10.6, 87]
An array of booleans looks like this

      >bool_array = [True, False, False, False, True, False]
      >print("\n",bool_array)

      [True, False, False, False, True, False]
We can even have arrays that contain multiple types

      >misc = [68,"blueberries",True,9.5,False,"chair"]
      >print("\nMy miscellaneous array contains:",misc)

      My miscellaneous array contains: [68, 'blueberries', True, 9.5, False, 'chair']
We can even add lists of different types together
      >print("\nAn array of numbers + an array of strings: ",restaurants+dog_weights)

      An array of numbers + an array of strings:  ['Burger King', "Wendy's", "McDonald's", 'Red Robin', 'Olive Garden', "PF. Chang's", 60, 13, 20, 71, 45, 10.6, 87]
Or make an array of arrays!

      >matrix = [
          >[42,7,8],
          >[90,82,4],
          >[32,41,98]
      >]
      >for element in matrix:
          >print(element)

      My matrix is
      [42, 7, 8]
      [90, 82, 4]
      [32, 41, 98]

### Dictionaries
I'll use a dictionary to model the functionality of a Hash Table. The code below demonstrates how to create a dictionary, and how to access one of the elements

      >car = {
          >"make": "Lexus",
          >"model": "CT200H",
          >"year": "2011",
          >"color": "red"
      >}
      
      >color = car["color"]
      >print("\nThe car is ",color)

      The car is  red

## Type conversions

An integer can be cast as a float and vice versa, an integer or float can both be cast as strings, and a string containing numbers can be cast as a float or an int, as demonstrated below.

      >num_int = 12
      >num_str = str(num_int)
      >print("The ",num_int, " was ",type(num_int)," is now ",type(num_str))
      The  12  was  <class 'int'>  is now  <class 'str'>

      >num_float = 23.4
      >num_str = str(num_float)
      >print("The ",num_float, " was ",type(num_float)," is now ",type(num_str))
      The  23.4  was  <class 'float'>  is now  <class 'str'>
      
      >num_str = "70"
      >num_int = int(num_str)
      >print("The ",num_str, " was ",type(num_str)," is now ",type(num_int))
      The  70  was  <class 'str'>  is now  <class 'int'>

# Conclusions
Coding in Python offers a lot of flexibility. Data types do not need to be declared, and they can change over time. This can lead to errors if you accidentally change a variable to the wrong type, but the interpreter will make sure you don't use any undefined methods on a data type.

# Sources
* Python.org https://www.python.org/dev/peps/pep-0008/, Accessed September 23, 2020.
* RealPython.com https://realpython.com/python-variables/#:~:text=Officially%2C%20variable%20names%20in%20Python,name%20cannot%20be%20a%20digit Accessed September 23, 2020.
* Wiki.python.org https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language#:~:text=Python%20is%20strongly%20typed%20as,variable%20types%20and%20correct%20usage Accessed September 23, 2020.
