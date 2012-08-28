the_store = PotionStore(['gatorade', 'water', 'coffee'])
the_store.describe()
print "Do you take potion 1, 2, or 3?"
    
potion_number = int(raw_input(">"))

potion = the_store.pick_potion(potion_number)

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