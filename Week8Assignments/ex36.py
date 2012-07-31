from sys import exit

def potion_store():
    print "The store is full of potions. Do you take potion 1, 2, or 3?"

    next = raw_input("> ")
   
    if potion_number == "1":
        print "You turn into a frog. You lose.  Who knows, maybe a princess will kiss you...maybe"
        exit(0)
    elif potion_number == "2":
        print "Wrong potion, you chose a death potion"
        dead("life sucks and then you die")
    elif  potion_number == "3":
    	print " You chose correctly, You win the game!"
    	exit(0)
    else:
        dead("That's not a valid number choice...1, 2, or 3! If only you could have followed directions!")

def cross_river():
    print "There is a dragon on the bridge that crosses the river."
    print "There is a goblin under the bridge"
    print "There is a ferry on the river banks that costs 5 gold coins to cross"
    print "How are you going to cross the river?"
    river_crossed = False

    while True:
        next = raw_input("> ")

        if next == "slay the dragon":
            dead("Your toast, the dragon chared you to a crisp.")
        elif next == "kill the goblin" and not river_crossed:
            print "You killed the goblin and took his gold.  Looks like you can take the ferry now"
            print "What do you want to do?"
            river_crosed = True
        elif next == "take the ferry" and not river_crossed:
            dead("Looks like you don't have any gold coins.  Come back when you can afford it sonny. ")
        elif next == "swim" and river_crossed:
        	print "swimming is always a good solution.  you avoided the dragons, goblins and ferrry fare. "
        potion_store()
        else:
            print "speak english dummy"
            
def soup_time():
	print "The soup looks good but there is a dirty spoon."
	print "Do you use the spoon or slurp from the bowl?"
	print "spoon or slurp?"
    
    next = raw_input("> ")     
    
    if next == "spoon":
    	print "that's gross, you just got samonella or something similar. You had better get a potion from the potion store."
    	print "but first you need to cross the river."
    	cross_river():
    elif next == "slurp":
    	print = "that a boy slurp that soup! umm..You Win!"
    	exit(0)
    else:
    	print "no soup for you!"
    	dead ("Guess you starve to death!")
            
def dead(why):
    print why, "You're dead now...on the bright side maybe you will reincarnate as a cat"
    exit(0)
    

def start():
    print "You're starving and come across a table of food in the forest."
    print "There is fruit, soup, and a pizza"
    print "What do you eat?"

    next = raw_input("> ")

    if next == "fruit":
    	print "That fruit was bad. you better get to the potion store across the river!"
        cross_river()
    elif next == "soup":
        soup_time()
        elif next == "pizza":
        print "That pizza had poisonus mushrooms on it. you better get to the potion store across the river!"
        cross_river()
    else:
        dead("You stumble around the forest until you starve to death.")


start()
	