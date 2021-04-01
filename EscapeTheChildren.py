import time
# Jamila Van Norden 7-3 Project Two IT-140-H3635 21EW3
# Implemented very differntly than written psudocode due to course requirment, ao dictionaries were used instead of classes. 
delay = 0.5

# Function to output welcome message prompt and collect user name.
def welcome_message(player_name):
   message = "Hi {}, Welcome to Escape the Children. This is a text-based\n" \
                     "adventure game. You must successfully navigate through the home,\n" \
                     "without encountering the children. If the children see you its game over.\n" \
                     "In order to win, you must make it back to the front door, with all six items.".format(player_name)
   print(message)

# Function to output game instructions
def game_instructions(player_name):
   instructions = "In order to move through the rooms of the home, type in chosen\n" \
                       "direction. You can choose to go north (n), south (s), east (e), west (w).\n" \
                       "{}, enter quit (q) at any time to exit the game.\n".format(player_name)
   print(instructions)


# This dict gives each room a string, that informs user of room. I used integers for readability
player_location = {0: "You are at the Front Door.",
                   1: "You are in the Living Room.",
                   2: "You are in the Bathroom.",
                   3: "You are in the Kitchen.",
                   4: "The children have you spotted you in the Dining Room. \nGAME OVER!",
                   5: "You are in the Master Bedroom.",
                   6: "You are in the Playroom.",
                   7: "You are in the Mudroom.",
                   8: "You are in the Second Bedroom.",
                   9: "You have Quit the game. See you next time."}

#This dictionary links each room (using a number) to original location and available directions and
# links to next room
rooms = {0: {"N": 1, "S": 2, "W": 5, "E":7, "Q": 9},
         1: {"N": 3, "S": 0, "Q": 9},
         2: {"N":0, "S": 4, "Q": 9},
         3: {"S": 1, "Q": 9},
         4: {"I'm Sorry! \n": 4},
         5: {"E": 0, "W":6, "Q": 9},
         6: {"E": 5, "Q": 9},
         7: {"W": 0, "E": 8, "Q": 9},
         8: {"W": 7, "Q": 9},
         9: {"Q": 9} }

# dict of vocabulary player can enter, into game.
vocab = {"QUIT":  "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST":  "E",
         "WEST":  "W"}
# dict of bag items
items_bag = {0: "",
              1: "Keys",
              2: "Wallet",
              3: "Phone",
              4: "",
              5: "Glasses",
              6: "Laptop",
              7: "Coffee",
              8: "",
              9: ""}



# collect user data, Validates user input
#validate user input name, making sure only letters are used

name = input("Please Create a Username: ").capitalize()
welcome_message(name)
time.sleep(delay)
print("~" * 40)
time.sleep(delay)
game_instructions(name)
print("~" * 40)

b = []

current_location = 0
while True:
   # Joins the room dict keys and concatenates a string to loop through the available_exits and
   # add direction and a "'".
   available_exits = ", ".join(rooms[current_location].keys())
   time.sleep(delay)
   print(player_location[current_location]) # Calls the current location key's value, from the locations.
   # If the current_location is 4 (Dining room w/ villains) terminate loop.
   if current_location == 4:
      break
   # If current location is 9 (Quit game) terminate loop.
   if current_location == 9:
      break
   #if the length of the items list is 7 it means the user has all 6 items (includes "" key items)
   # This is so the user can win the game once all items are collected and inside the users bag.
   if len(b) == 7:
      print("{}, Congrats! You have collected all of the items.\nYou have won the game!.".format(name))
      break


# Prompt player to input desired direction into game. Provide player with available_exits (line 37). Force upper-case.
   direction = input("Available directions are: " + available_exits + " \n").upper()
   time.sleep(delay)

# if the player input is longer than 1 character, split it into a list. Then parse list through vocab dict. For speed.
   if len(direction) > 1:
      words = direction.split()
      for word in words:
         if word in vocab:
            direction = vocab[word]
            break
# if the players chosen direction is in the rooms dict it will print out the room dicts key, value along with
# providing the player wit ha prompt to chose another direction and allowing input.
   if direction in rooms[current_location]:
      current_location = rooms[current_location][direction]
      # If the items are not in b, add them to the list b. then join the list into a string and print to user.
      # This removes duplicates. It also takes out the "" dict keys from the items_bag in the printed statement.
      if items_bag[current_location] not in b:
         b.append(items_bag[current_location])
         seperator = " "
         print("{}, your bag contains the following items:\n{}".format(name, seperator.join(b)))

   else:
      print("Choose a valid direction")

