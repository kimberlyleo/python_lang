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
# Arithmetic operators: +, -, *, /, %, **, // (floor division)
def floor_division(num):
    quotient_rounded_down = num//2
    return quotient_rounded_down

assert 2 ** 3 == 8
assert 6 % 2 == 0
assert 7 % 2 != 0

# Assignment Operators: =, +=, -=, *=, /=, //=, etc.
def assignment_actions(num_input):
    num = num_input
    print(num) # >> 2
    num *= num
    print(num) # >> 4
    num /= num 
    print(num) # >> 1.0 
    num += num 
    print(num) # >> 2.0
    num **= num
    print(num) # >> 4.0
    num //= num #this does NOT cause type conversion from int to a float
    print(num) # >> 1.0
    num -= num
    print(num) # >> 0.0
    
    # * notice that division operation always creates a float quotient (more on ints and floats next)
#assignment_actions(2)

# Comparison Operators: ==, !=, >, >=, <,<= used to create boolean value/ also referred to as bool operators
assert 2 + 2 == 4 
    #assert is used to ensure that a comparison operation returns True (nothing will happen if True); if False an AsserionAError is raised
assert True != False
#comparison operators function the same way as they do in other languages 


# Identity operators: 
    # in / not in : used to see if it is member or subtype of a given class 
    # is / is not ; used to evaluate if memorty location is the same; returns True/False
    # https://www.tutorialspoint.com/python3/python_basic_operators.htm
var1 = 6
var2 = 6
assert var1 is 6
assert var1 is var2

dance_count = [ 5, 6, 7 , 8]
assert var1 in dance_count
if "and" not in dance_count:
    dance_count.append("and")
    #print(dance_count)
# can use 'in' or 'not in' to quickly check if something exists within a given list and return a boolean val


# Mathematical Functions
# Integers and floats
#examples showing python's built in number/float functions inc. type conversions 
#https://www.tutorialspoint.com/python/python_numbers.htm
assert int(3.0) == 3
assert float(3) == 3.0
assert complex(3.0) == (3 + 0j)
assert complex(3.0, 3) == (3 + 3j)
    # a complex number is a real number plus an imaginary number (identififed by the j operator)
    # complex() can take up to two arguments (real_number, imaginary_number) used for complex calcs that can be solved with numbers that are square roots of negative numbers
    # complex numbers are used in electric engineering

assert abs(-1) == 1
assert round(3.5) == 4
assert round(3.4) == 3

import math 
assert math.floor(5.9) == 5
assert math.ceil(3.2) == 4
assert math.exp(2) == 7.38905609893065
#math.exp(x) calculates e to the power of x; can be written as (e^x)


# Lists

list_of_animals = ["Gorilla" , "Panda", "Tarsier"]
list_of_animals.append("Leopard Gecko")
    #appends "Leopard Gecko" to the end of the list 
    #append takes only one argument; argument can be a list but that list will be a single item on the outputted list

second_list_of_animals = ["Fennec Fox", "Sonoran Desert Toad"]
list_of_animals += second_list_of_animals 
#print(list_of_animals)
list_of_animals.sort()
#print(list_of_animals)
#sort mutates the list 

#can use zip to pair list items by index position
list1 = [1, 2, 3]
list2 = ['pie' , 'ice cream', 'Irish Coffee']
list3 = ['$3.20', '$2.00', '$4.20']
menu_items = zip(list1, list2, list3)
#print(menu_items) # >>> <zip object at mEmOrY_LoCaTiOn>
#print(list(menu_items)) #>>> [(1, 'pie', '$3.20'), (2, 'ice cream', '$2.00'), (3, 'Irish Coffee', '$4.20')]
# Caution* if (len(list1) != len(list2)) and (len(list3) != len(list1)): the unmatched list items are trimmed and no error is raised

#len() returns the length of the list
assert len(list1) == 3
assert list3[2] == '$4.20'

# list_name.count("value") >> counts the number of occurences of "value" in list_name
new_list = [1, 0, 1, 0, 0]
assert new_list.count(1) == 2

#range takes 1, 2 ,or 3 arguments: (end), (start, end), or (start, end, increment), respectively
#range end is not inclusive
#object created by range() needs to be unpacked with list() to be read
assert list(range(5)) == [0, 1, 2, 3, 4]
assert list(range(1, 30, 10)) == [1, 11, 21]
assert list(range(0, 30, 10)) == [0, 10, 20]

#slicing
#Slice end value index position is not inclusive
oreo_flavors = ['Mint Chocolate', 'Birthday Cake', 'Peanut Butter', 'Original']
assert oreo_flavors[-2:] == ['Peanut Butter', 'Original']
assert oreo_flavors[0:2] == ['Mint Chocolate', 'Birthday Cake']
assert oreo_flavors[3] == "Original"

#.pop(index_position) removes and returns value at given index position from list 
#.pop() mutates the list oreo_flavors
assert oreo_flavors.pop(2) == "Peanut Butter"
assert oreo_flavors == ['Mint Chocolate', 'Birthday Cake', 'Original']

# Tuples
# unmutable lists
tuple_name = ("kim", 28, "San Diego")
#can unpack a tuple and name all simulataneouslyvariables simulataneously
name, age, city = tuple_name
assert name == 'kim'
assert city == "San Diego"

# Dictionaries
#create a new dictionary using the following syntax
dictionary_name = {"key": "value", "key2": "value2"}
empty_dictionary = {}

#adding a new key:value pair to dictionary using the following syntax
dictionary_name["new key"] = "new value"
#print(dictionary_name)

accumulated_rain = {'Carlsbad': 2, 'Cloud Forest': 44}
#print(accumulated_rain['Death Valley']) will return KeyError: 'Death Valley'
#can set a custom return value for non-existant keys to avoid KeyError (does not mutate the dictionary)
assert accumulated_rain.get('Death Valley', 0) == 0

assert list(accumulated_rain) == ['Carlsbad', 'Cloud Forest']
#list() used on dictionaries will return a list of keys
assert list(accumulated_rain.values()) == [2, 44]
#.values() returns a read-only dict-object of values that must be unpacked with list() to access items
#print( accumulated_rain.items()) # console: dict_items([('Carlsbad', 2), ('Cloud Forest', 44)])
assert list(accumulated_rain.items()) == [('Carlsbad', 2), ('Cloud Forest', 44)]



# Functions
# illustrated with examples below

def dew_point_calc(temp_celsius, relative_humidity_percent):
    dew_point_temperature = temp_celsius - ((100 - relative_humidity_percent)/5)
    return dew_point_temperature

def submit_to_overlord_Goodburger():
    user_response = input("Welcome to Goodburger, home of the Goodburger. Would you like a Goodburger? \n\'y\' OR \'n\'\n")
    if (user_response != "y"):
        submit_to_overlord_Goodburger()

#submit_to_overlord_Goodburger()

# Loops

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
