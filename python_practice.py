
#COFFEE ORDER IN THE TERMINAL

#FINISH ***************************************************************
# to record orders with multiple coffees i will add them as JSON type obj and and push them into an order array and the final print read, off will map through the array of obj
#order = []
    
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n>")
  if res == "a":
    drink_type = "Brewed Coffee"
  elif res == 'b':
    drink_type = "Mocha"
  elif res == "c":
    drink_type = 'Latte'
  else:
    print_message()
    return get_drink_type()
  return drink_type

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n>")
  if res == "a":
    milk_type = "2% milk"
  elif res == 'b':
    milk_type = "Non-fat milk"
  elif res == "c":
    milk_type = 'Soy milk'
  else:
    print_message()
    return order_latte()
  return milk_type

def follow_up():
  res = input("Would you like to order any more beverages? \n[a] Yes \n[b] No")
  if res == "a":
    return coffee_bot()
  else:
    return print("Great thanks")
  
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()

  if (drink_type == "Latte"):
    milk_type = order_latte()
    print("Alright, that's a {} {} with {}!".format(size, drink_type, milk_type))
  else: 
    print("Alright, that's a {} {}!".format(size, drink_type))
  
  follow_up()

    name = input("Can I get your name please? \n>")
    print("Thanks, {}! Your drink will be ready shortly.".format(name))
  

coffee_bot()

