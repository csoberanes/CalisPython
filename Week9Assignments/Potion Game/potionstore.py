from sys import exit

class PotionStore(object):
	def_init_(self,number):
	
    print "The store is full of potions. Do you take potion 1, 2, or 3?"
    
    potion_number = int(raw_input(">"))

    if self.number == 1:
        print "You turn into a frog. You lose.  Who knows, maybe a princess will kiss you...maybe"
        exit(0)
    elif self.number == 2:
        print "Wrong potion, you chose a death potion"
        dead("life sucks and then you die")
    elif  self.number == 3:
    	print " You chose correctly, You win the game!"
    	exit(0)
    else:
        dead("That's not a valid number choice...1, 2, or 3! If only you could have followed directions!")