gamers = []

def add_gamer(gamer, gamers_list): 
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)

#signing up gamers with their availability using function add_gamer
kimberly = {"name": "Kimberly Warner", "availability": ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


#create an empty dictionary to hold all of the frequency sums 
daily_frequency = {"Monday": 0 , "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, 'Saturday': 0, 'Sunday': 0}

#loop through the list of gamers and then each gamers list of availability to update the dictionary with availabilities
#outputs the updated dictionary
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1
    return available_frequency

calculate_availability(gamers, daily_frequency)


#finds the night with the highest availability count and updates variables, best_nigh and highest_frequency with the night that corresponds with the highest availability
def find_best_night(available_frequency):
    highest_frequency = float("-inf")
    for night, frequency in available_frequency.items():
        if (frequency > highest_frequency):
            highest_frequency = frequency
            best_night = night
    return best_night

best_night = find_best_night(daily_frequency)


def available_on_night(gamers_list, day):
    available_people = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            available_people.append(gamer['name']) 
    return available_people

attending_game_night = available_on_night(gamers, best_night)


form_email = "Hello {}, On {} we will be playing {}."

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(gamer, day, game))
    
send_email(attending_game_night, best_night, "Abruptly Goblins")



#many weren't able to attend the game so we are setting up a second night
#reusing many of the same functions to do so
 find the best night for those through frequencies, and then formulate email notifications for all of those available
second_night_availability = {"Monday": 0 , "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, 'Saturday': 0, 'Sunday': 0}

#going through everyone who isn't available to attend to first game night
def unable_to_attend_best_night(gamers_list, attending_best_night): 
    unable_to_attend_best_night = []
    for gamer in gamers_list:
        if gamer["name"] not in attending_best_night:
            unable_to_attend_best_night.append(gamer)
    return unable_to_attend_best_night

#saving those who couldn't attend to a variable unable_to_attend_best_night
unable_to_attend_best_night = unable_to_attend_best_night(gamers, attending_game_night)

#calling calculate_availability to update second_night_availability frequency list
calculate_availability(unable_to_attend_best_night, second_night_availability)

#find the day with the highest frequency of available gamers from the subset of gamers
second_night = find_best_night(second_night_availability)

#create a list of all players available only for the second game night
attending_second_night = available_on_night(gamers, "Monday")

send_email(attending_second_night, second_night, "Abruptly Goblins")

