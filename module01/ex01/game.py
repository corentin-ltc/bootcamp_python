class GotCharacter:
	def __init__(self, first_name=None, is_alive=True) -> None:
		self.first_name = first_name
		# self.family_name = family_name
		# self.house_words = house_words
		self.is_alive = is_alive

class Stark(GotCharacter):
	def __init__( self, first_name=None, is_alive=True ) -> None:
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is coming"

	def die(self):
		self.is_alive = False
	
	def print_house_words(self):
		print(self.house_words)