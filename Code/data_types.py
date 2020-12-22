# Experimentation with Data Types

# Can we change the type of a variable?
x = 7
print("\n",x)
x = "rain"
print(x)

# Can we add an integer to an integer?
fall_goals = 14
spring_goals = 19
total_goals = fall_goals + spring_goals

print ("\nIn the fall, the soccer team scored ",fall_goals," goals. In the spring, they scored ",spring_goals, " for a total of ",total_goals," goals.")

# Consider two floats
oz_honey = 1/3
oz_agave = 2.1
oz_sweetener = oz_honey + oz_agave

print("\nThere are ",oz_sweetener," ounces of sweetener.")

# Can we narrow the float and make it an integer?
oz_sweetener_rounded = round(oz_sweetener)
print("\nOr ",oz_sweetener_rounded," ounces, rounded.")


# What happens when we add a float to an integer?
weight = 12
weight_gain = 2.2
final_weight = weight + weight_gain

print ("\nThe penguin's initial weight was ",weight, " lbs. She gained ",weight_gain," pounds to weight a total of ",final_weight," lbs.\n")

# Can we add strings together?
greeting_1 = "Hello."
greeting_2 = "Hi!"
greeting_3 = greeting_1+" "+greeting_2

print(greeting_3)

# Can we add a string to a numerical value?
#sentence = "The quick brown fox jumps over the lazy dog."
#int_value = 16
#x = sentence + int_value

#float_value = 16.5
#y = sentence + float_value

# How can we represent Booleans (True or False)?
won_game = True
if won_game:
    print("\nCongratulations! You won the game.\n")
else:
    print("\nYou lost the game. Play again soon!\n")

paid_in_advance = False
print("It is ",paid_in_advance," that you have paid in advance.")

# Can we add Booleans?
print("\nTrue or False is ", won_game + paid_in_advance, " (True)")
print("\nTrue and False is ", won_game * paid_in_advance," (False)")

# Can we add Booleans to other values?
int_value = 10
float_value = 12.2
bool_value = True

print("\n",int_value," + True gives ", int_value + bool_value)
print("\n",float_value," + True gives", float_value + bool_value)
#print(sentence + bool_value)

# Can we represent arrays of strings? 
fast_food = ["Burger King","Wendy\'s","McDonald\'s"]
print("\nThe fast food restaurants are: ",fast_food)

sit_down = ["Red Robin", "Olive Garden", "PF. Chang\'s"]
print("\nThe sit down restaurants are: ",sit_down)

restaurants = fast_food + sit_down
print("\nAll of the restaurants are: ",restaurants)

# How about arrays of numbers? (I'll use both integers and floating point numbers)
dog_weights = [60,13,20,71,45,10.6,87]
print("\nThe dogs weights are: ",dog_weights)

# Can we make an array of booleans?
bool_array = [True, False, False, False, True, False]
print("\n",bool_array)

# What about an array of multiple types?
misc = [68,"blueberries",True,9.5,False,"chair"]
print("\nMy miscellaneous array contains:",misc)

print("\nAn array of numbers + an array of strings: ",restaurants+dog_weights)

# How about a list of lists?
print("\nMy matrix is")
matrix = [
    [42,7,8],
    [90,82,4],
    [32,41,98]
]
for element in matrix:
    print(element)

# How about a hash table? (I will be using dictionary as a hash table)
car = {
    "make": "Lexus",
    "model": "CT200H",
    "year": "2011",
    "color": "red"
}

color = car["color"]
print("\nThe car is ",color)

# Type conversion
num_int = 12
num_str = str(num_int)
print("The ",num_int, " was ",type(num_int)," is now ",type(num_str))

num_float = 23.4
num_str = str(num_float)
print("The ",num_float, " was ",type(num_float)," is now ",type(num_str))

num_str = "70"
num_int = int(num_str)
print("The ",num_str, " was ",type(num_str)," is now ",type(num_int))
