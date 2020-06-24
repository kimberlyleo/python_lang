# table of contents
# syntax- - arithmetic operators, comparison operators, is not is, assignment operators
# language basics- read top down...
# dictionaries
# lists, range(start, end, increment), list() functions for manipulation( del, pop, sort/sorted, count...), slicing [-3:]
# loops 
# recursive function example

# SYNTAX 
# Language Basics: PYTHON is an interpretted (not compiled), object oriented, high level, language. their site also says it has dynamic semantics which means how the program's code is executed changes with new information... need to learn more about this and how it works!!

# OPERATORS (will add bitwise operators)
# arithmetic operators: +, -, *, /, %, **, // (floor division)
# assignment operators: =, +=, -=, *=, /=, //=, etc.
# comparison operators: ==, !=, >, >=, <,<= used to create boolean value/ also referred to as bool operators
# identity operators: in : used to see if it is member or subtype of a given class is / is not ; used to evaluate if identity is identical (same object occupying the same place in memory)


# functions
# illustrated with exapmples below

def dew_point_calc(temp_celsius, relative_humidity_percent):
    dew_point_temperature = temp_celsius - ((100 - relative_humidity_percent)/5)
    return dew_point_temperature

def submit_to_overlord_Goodburger():
    user_response = input("Welcome to Goodburger, home of the Goodburger. Would you like a Goodburger? \n\'y\' OR \'n\'\n")
    if (user_response != "y"):
        submit_to_overlord_Goodburger()

#submit_to_overlord_Goodburger()

# loops

def while_loop():
    while True:
        print("This will continue to loop until break conditions are met")
        user_response = int(input("Pick a number between 1 and 5\n"))
        if (user_response in [1, 2, 3, 4, 5]):
            break
    if (user_response % 2 == 0):
        return "Great job with {}, Even Steven".format(str(user_response))
    elif (user_response == 1) and (user_response != 5):
        return "winner winner second place"
    elif user_response != 5 or user_response != 3:
        return "this is a pointless conditional to show \'or\' comparison operator"

#print(while_loop())

def while_counter_runs():
    counter = 0
    while (counter < 5):
        print("Counter value is {}".format(str(counter)))
        counter += 1
        #because the counter increases after print statement, counter values printed range from 0 to 4
        #if the counter increase was above print statement range printed would be 1 to 4

# while_counter_runs()

cat_names = ["Fyodor", "Reggie", "Socks", "Yarnell"]

def list_loop(names):
    cat_number = 1
    for cat in names: 
        print("{}. {} ".format(cat_number, cat))
        cat_number += 1

#list_loop(cat_names)
