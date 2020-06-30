
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

#for in looping 
def catch_em_all(): 
    pokemans = ["pikachu", "squirtle", "charzar", "bulbosaur"]
    message = "My pokeball has: "
    for pokemon in pokemans:
        if pokemon == pokemans[-2]:
            message += pokemon + ", and "
        elif pokemon == pokemans[-1]:
            message += pokemon
        else:
            message += pokemon + ", "
    return message

#print(catch_em_all())

# for temporary_loop_variable in listName: above temp variable was pokemon which represents each value of the list pokemans 
#this will print: My pokeball has: pikachu, squirtle, charzar, and bulbosaur
#using if elif and else for grammatic structuring

#double for in loop (can call a loop on a temporary varianble within scope) which is exemplified in /dictionary_loops.py


#loops and operations on dictionaries:
shop_inventory = { "sashes": 3, "feather boas": 22, "pairs go-go boots": 4, "kaleidoscope shades": 12}

def operate_on_keys_only():
    for item in shop_inventory:
        print(item)
#this will print keys ('feather boas', 'pairs go-go boot', 'kaleidoscope')

def operate_on_keys_and_values():
    for item, count in shop_inventory.items():
        print("We have {} {}.".format(count, item))
#here .items() is used on dictionary name to allow handling both keys and values in a function 

# operate_on_keys_and_values() 

def operate_on_values_only():
    total_inventory = 0
    for value in shop_inventory.values():
        total_inventory += value
    print("Shop-Wide inventory today: {}".format(total_inventory) )

# operate_on_values_only()


def add_ten(my_dictionary):
  for key, value in my_dictionary.items():
    # value += 10
    # my_dictionary[key] = value
    # the code below does the same thing as the commented code, but is written more concisely
    my_dictionary[key] += 10
  return my_dictionary

def values_that_are_keys(my_dictionary):
  values_match = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      values_match.append(value)
  return values_match
  #returns a list of values that can also be found as keys
  #you can treat my_dictionary as a list, using "in" even though it is a dict object

def while_counter_runs():
    counter = 0
    while (counter < 5):
        print("Counter value is {}".format(counter))
        counter += 1
        #because the counter increases after print statement, counter values printed range from 0 to 4
        #if the counter increase was above print statement range printed would be 1 to 4

while_counter_runs()

cat_names = ["Fyodor", "Reggie", "Socks", "Yarnell"]

def list_loop(names):
    cat_number = 1
    for cat in names: 
        print("{}. {} ".format(cat_number, cat))
        cat_number += 1

list_loop(cat_names)

#returns the key of the largest value from a given list
def max_key(my_dictionary):
  largest_value = float("-inf") #starting value is as small as possible (-infinity)
  largest_key = "" #empty string to host the keys that represent the current winner in the loop
  for key, value in my_dictionary.items(): #iterating over keys and values
    if value > largest_value: 
      largest_value = value
      largest_key = key
  return largest_key

#takes in a list of words, creates new_dictionary (which is a dictionary where the keys are unique word in words and the values are the frequencies of each word's occurence)
def frequency_dictionary(words):
  new_dictionary = {}
  for word in words:
    if word not in new_dictionary:
      new_dictionary[word] = words.count(word)
  return new_dictionary