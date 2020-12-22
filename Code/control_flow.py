# This is my code!
# It's purpose is to demonstrate how many different control structures can be utilized in Python

# Consider a one-condition if/else statement.
lottery_ticket = 10
if lottery_ticket == 10:
    print("You win!\n") 
else:
    print("Try again.\n")

students = ["Jessica","Bella","Sam","Juan"]
if "Jessica" in students: 
    print("Jessica is registered for classes.")
print("Done with the if, even if Jessica isn't in the list, this statement will print.\n")

at_capacity = False
if ~ at_capacity: print("We can seat you now.\n")

temp = 89
if temp > 80:
    print("We could go to the beach!")
if temp > 70:
    print("We could go for a walk.")
elif temp > 60:
    print("We could go for a run")
elif temp > 65:
    print("We could bike.")
else:
    print("It's too cold.")

print("")
month = 11 
if month == 12: print("It's December"); print("It's still December"); print("It's really still December\n")
if month == 11: print("It's November"); print("It's still November"); print("It's really still November\n")

# Consider a multi-condition if/else statement
age = 14
if lottery_ticket == 10 and age >= 18:
    print("You win!\n")
elif lottery_ticket == 10:
    print("You won, but you're too young to collect your prize :(\n")
else:
    print("Try again.\n")

has_guardian = True
if lottery_ticket == 10 and (age >= 18 or has_guardian):
    print("You win!\n")
elif lottery_ticket == 10:
    print("You won, but you either need a guardian or you need to come back when you're older.\n")
else:
    print("Try again.\n")

age = 22
if age == 22 or 1/0 == 2345:
    print("You win! (and thankfully didn't divide by zero!)\n")
else:
    print("Try again.\n")

if age == 16 and 1/0 == 2345:
    print("You win! (but actually, this is impossible.)\n")
else:
    print("Try again. (but at least you didn't divide by zero!)\n")

# Consider nested conditional expressions
weight = 12.3
height = 5
if (weight > 10):
    if (height > 5.5):
        print("Your dog is tall and heavy.\n")
    else:
        print("Your dog is very short and stocky.\n")
else:
    if (height > 5.5):
        print("Your dog is thin and tall.\n")
    else:
        print("Your dog is thin and short.\n")

# Consider other conditional expressions - the ternary operator of Python.
num_items = 14
print("Please proceed to the", "express lane.\n" if not (num_items > 15) else "regular lane.\n")
print("Please proceed to the", "regular lane.\n" if (num_items > 15) else "express lane.\n")

# Using conditional expressions for assignment.
x = 12 if (42==42) else 14
print("x is %d.\n" %x)

y = -15
z = (-y if (y < 0) else y) + (-x if (x < 0) else x)
print("|%d|+|%d| = %d.\n" %(x,y,z) )

# Consider while loops.
factorial = 1
n = 5
while n > 1:
    factorial *= n
    n -= 1
print("The factorial of 5 is %d\n" %factorial)

num_buckets = 0
while num_buckets >= 1:
    num_buckets -= 1      # Will this loop ever be executed?
print("There are %d buckets left\n" %num_buckets)

#while num_buckets >= 0:
    #num_buckets += 1      # Will this loop ever end?
#print("There are %d buckets left\n" % num_buckets)

# Consider for loops.
sum_of_squares = 0
for i in range(1,15):
    sum_of_squares += i**2
print("The sum of the squares up to 14^2 is: %d\n" %(sum_of_squares))

print("My favorite Christmas movies are:")
christmas_movies = ["The Grinch", "Home Alone", "Elf"]
for movie in christmas_movies:
    print(" %s" %movie)
print("")

word = "dog"
for letter in word:
    print(letter)

print("")

for i in range(len(word)):
    print("Letter %d is %s" %(i,word[i]))

# Consider a nested for loop
for col in range (5):
    stars = ""
    for row in range(col):
        stars += "*"
    print(stars)

print("\nMy car details are as follows:")
car = {
    "Make": "Lexus",
    "Model": "CT200H",
    "Year": "2011",
    "Color": "red"
}
for trait in car:
    print(" %s: %s" %(trait, car[trait]))

# Consider switch-case statements
grade = 7
switch = {
    "1" : "F",
    "2" : "F",
    "3" : "F",
    "4" : "F",
    "5" : "F",
    "6" : "D",
    "7" : "C",
    "8" : "B",
    "9" : "A",
    "10" : "A+"
}
letter_grade = switch[str(grade)]
print("\nMinnie's grade this quarter is %s.\n" %letter_grade)

season = ("spring" if (3 <= month <= 5) else
            "summer" if (6 <= month <= 8) else
            "fall" if (9 <= month <= 11) else
            "winter"
            )
print("Welcome to the", season, "season.\n")

# Consider break and continue statements
y = 0
for x in range(2,8):
    if x % 4 == 1:
        print("About to break...\n")
        break
    else:
        y += x
        print("x = %d, y = %d" %(x, y))

curr_year = 1980
future_year = 2020
while curr_year <= future_year:
    curr_year += 1
    if curr_year % 4 == 0:
        if curr_year % 100 == 0 and curr_year % 400 == 0:
            print("%d is a leap year.\n" %curr_year)
            break
        elif curr_year % 100 != 0:
            print("%d is a leap year.\n" %curr_year)
    else:
        continue
        print("This will never run")


# Consider pass statements
x = 15
sum_of_evens = 0
while (x > 1):
    if (x%2 == 1):
        pass
        print("Pass %d" %x)
    else:
        sum_of_evens += x
    x -= 1
print("\nThe sum of even numbers less than or equal to 15 is: %d" %sum_of_evens)

#x = 15
#sum_of_evens = 0
#while (x > 1):
    #if (x%2 == 1):
    #else:
        #sum_of_evens += x
    #x -= 1
#print("\nThe sum of even numbers less than or equal to 15 is:", sum_of_evens)
