class Forest(object):
	def __init__(self, food_list):
		self.foods = food_list
		
	def pick_food(self, food_item):
		return(self.foods[food_item])
		
	def describe(self):
		print "The Forest is dark and full of trees and poisonus food and anmimals"
		
	