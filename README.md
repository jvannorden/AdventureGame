# AdventureGame (Python)

This project is focused on Translate requirements to solve problems computationally. Involved creating a storyBoard, desigin a map, and creating psuedocode. 
(This is created for a course in Python).

## Story Board (Created)

![image storyboard description](https://user-images.githubusercontent.com/75600338/113322870-3935f100-92e3-11eb-833e-86a3e2943a6c.png)

![image storyboard map](https://user-images.githubusercontent.com/75600338/113322925-510d7500-92e3-11eb-865e-99ec97350e71.png)

## Psuedocode (Created)

``` py 
Create a class move():

	define initialiser(self, north, south, east, west):
	# add constructors
self.north = north
	self.south = south
	self.east = east
	self.west = west
 
	define choice(self):
		provide user with available directions. 

define north(self):
		-l in list index, if can’t move north one prompt user to make another selection.
		output to user(message to user, call the rooms function/class)
		
	define south(self):
+ l in list index, if cant move north one prompt user to make another selection.
moves through rooms list + 1 through index values
		output to user(message to user, call the rooms function/class)

	define east(self):
		+ l in list index, if cant move north one prompt user to make another selection.
		output to user(message to user, call the rooms function/class)

	define west(self):
		-l in list index, if cant move north one prompt user to make another selection.
		output to user(message to user, call the rooms function/class)

#instances
room_list_verticle = [room3, room1, start_room1, room4, room2]
room_list2_horizontal = [room6, room5, start_room2, room7, room]

Create class rooms(move):
	
Define initialiser(self, start_room, room1, room2, room3, room4, room5, room6, room7,        
room8): #set boolen values at True for all rooms is not equal to kill room (room2)
		# add instance attributes
		self.start_room = start_room = True
		self.room1 = room1= True
		self.room2 = room2 = False
		self.room3 = room3 = True
		self.room4 = room4 = True
		self.room5 = room5 = True
		self.room6 = room6 = True
		self.room7 = room7 = True
		self.room8 = room8 = True

	define start_room(self, playes_name, room_name, choice, greeting):
create if statement for starting. Force lowercase user input. If no kill game if yes,	start game and output to user the greeting. 

	define room1(self, room_name, item):
this function will output to user message informing player of room name and add item1 to the plays bag.
return bag
	
	define room2(self, room_name, villian):
this room is the kill room. Outputs to users kill message, informing player they have encountered the villain and kills the game.
Return kill

define room3(self, room_name, item):
this function will output to user message informing player of room name and add item2 to the plays bag.
return bag

define room4(self, room_name, item):
this function will output to user message informing player of room name and add item3 to the plays bag.
return bag

define room5(self, room_name, item):
this function will output to user message informing player of room name and add item4 to the plays bag.
return bag

define room6(self, room_name, item):
this function will output to user message informing player of room name and add item5 to the plays bag.
return bag

define room7(self, room_name, item):
this function will output to user message informing player of room name and add item4 to the plays bag.
return bag

define room8(self, room_name, item):
this function will output to user message informing player of room name.
return bag

Create a class player(room): #Should probably use set and get dunder methods to add bag items.
	
	define initialiser(self, name. current_bag, new_bag, items):
		# add constructors
		self.name = name
		self.current_bad = current_bag
		self.new_bag = new_bag
		self.items = items
	
	define current_bag(self):
		if current bag is in room w/ item[]: 
			add item to new bag it now becomes new bag
			output to user(player_bag)
		else:
			pass/do nothing
		return current_bag

	define new_bag(self):
		output to user(player_bag[])
		return(new_bag)
	define items():
		# this is a list of all items in game.
		items: 
		return len(items)

#instance
player.items = [item1, item2, item3, item4, item5, item6]

User input
#Prompt player for name.
Player.name = str(input())

#Prompt player to start game. 
rooms.start_room(functions message and user prompts)

#While loop, will loop until player reaches room 2 set at false. 

While True:
While start_room equals yes: 
	prompt user to choice a direction move.choice(functions message and user prompts)
	If move.choice () equals north:
		move.north(room_list_verticle)
			if  room_name is equivilent start_room1:
				room_name equals room_list_horizontal[2]
				output to user(room6(functions message and user prompts),  
message.)
				prompt user for another choice (W or E)
			else if room_name is not equal to start_room1:
				room_name is equal to room_list_verticle[2]
				room_name is equal to room_list_verticle[-1]
				if -1 index is not possible
					output to user(please choose another direction: S)
				else if :
					next_room is equal to room_list[index]’s value
					call the corresponding rooms function.
`	else if move.choice () is equal to south:
		move.south(room_list_verticle)
			if the room_name is  equivilent to start_room1:
				room_name is equal to room_list_horizontal[2]
				output to user(start_room(functions message and user  
prompts))
prompt user for another choice (W or E)
			else if the room_name is not equal to start_room1:
				room_name is equal to room_list_verticle[2]
				room_name is equal to room_list_verticle[+1]
				if -1 index is not possible
					output to user(please choose another direction: N)
				else if :
					next_room is equal to room_list[index]’s value
					call the corresponding rooms function.
	If move.choice () is equal to west:
		move.north(room_list_verticle)
			if the room_name is  equivilent to start_room2:
				room_name is equal to room_list_horizontal[2]
				output to user(start_room(functions message and user  
prompts))
prompt user for another choice (N or S)
			else if the room_name is not equal to start_room2:
				room_name is equal to room_list_verticle[2]
				room_name is equal to room_list_verticle[-1]
				if -1 index is not possible
					output to user(please choose another direction: N or  
S)
				else if :
					next_room is equal to room_list[index]’s value
				call the corresponding rooms function.
If move.choice () is equal to East:
		move.north(room_list_verticle)
			if the room_name is  equivilent to start_room2:
				room_name is equal to room_list_horizontal[2]
				output to user(start_room(functions message and user  
prompts))
prompt user for another choice (N or S)
			else if the room_name is not equal to start_room2:
				room_name is equal to room_list_verticle[2]
				room_name is equal to room_list_verticle[-1]
				if -1 index is not possible
					output to user(please choose another direction: N or  
S)
				else if :
					next_room is equal to room_list[index]’s value
					call the corresponding rooms function.

```
