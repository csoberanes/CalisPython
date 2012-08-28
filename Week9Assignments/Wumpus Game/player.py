import slex

class Player(object):
	def __init__(self, location):
	self.location = location
	self.location.here.append(self)
	self.playing = True
	
	def get_input(self):
		return raw_input(">")
		
	def process_input(self, input):
		parts = shlex.split(input)
		if len(parts) == 0:
			return []
		if len(parts) == 1:
			parts.append("")
		verb = parts[0]
		noun = " ".join(parts[1:])
		
		handler = self.find_handler(verb, noun)
		if handler is None:
			return [input +
					"? I don't know how to do that!"]
			return handler(self, noun)
			
	def find_handler(self, verb, noun):
		if noun != "":
			object = [x for x in self.location.here
						if x is not self and
							x.name == noun and
							verb in x.actions]
							
			if len(object) > 0:
				return getattr(object[0], verb)
		if verb.lower() in self.actions:
			return getattr(self, verb)
		elif verb.lower() in self.location.actions:
			return getattr(self.location, verb)
			
	def look(self, player, noun):
		return [self.location.name,
				self.location.description]
				
	def quit(self, player, noun):
		self.playing = False
		return ["bye bye!"]
		
	actions = ['look', 'quit']
