
class card():

	suite_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	
	def __init__(self, rank=0,suite=2):
		self.rank = rank
		self.suite = suit

	def __str__():
		return f "The rank is {card.rank_names[self.rank]} and the suit is {card.suit_name[self.suit]}"


	def __lt__(self, other):
		#check suits
		if self.suit < other.suit: return true
		if self,suit > other.suit: return false

	def __eq__(self,other)
		return self,rank == other.rank and self.suit == other.suit

ace_of_spade = card(1,3)
print (ace_of_spade)

def __




