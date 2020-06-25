
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
        print("We have {} {}.".format(str(count), item))
#here .items() is used on dictionary name to allow handling both keys and values in a function 

#operate_on_keys_and_values() 


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

#list_loop(cat_names)11