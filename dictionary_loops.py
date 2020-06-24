letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letter:point for letter, point in zip(letters, points)}

letter_to_points[" "] = 0
print(letter_to_points)

def score_word(word):
  point_total = 0
  for letter in word:
    point = letter_to_points.get(letter, 0)
    point_total += point
  return point_total


brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {'player1': ["BLUE", "TENNIS", "EXIT"], 'wordNerd': ["EARTH", "EYES", 'MACHINE'], "Lexi Con":[ "ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", 'COMA', 'PERIOD']}


player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points



def play_word(player, word):
  word_list = player_to_words[player] 
  word_list.append(word)
  player_to_words[player] = word_list 
   

def update_point_totals(player, word):
  new_word_score = score_word(word)
  player_score = player_to_points[player] 
  player_to_points[player] = player_score + new_word_score


def player_turn(player, word):
  word = word.lower()
  play_word(player, word)
  update_point_totals(player, word)

player_turn("Lexi Con", "AAAA")
player_turn("player1", "butterpie")
print(player_to_words)
print(player_to_points)
