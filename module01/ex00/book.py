
import recipe.py

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		self.name =  name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipes_list



	def __str__(self) -> str:
		return (f"Book(name={self.name}, last_update={self.last_update}, "
		f"creation_date={self.creation_date}, recipes_list={self.recipes_list})")
	
	def get_recipe_by_name(self, name):
		return self.recipes_list.get(name)
	def get_recipe_by_type(self, type):
		return self.recipe_ytpe


def main():
	harrypotter = Book('Harry Potter', 14/17/1989, 15/25/1985, 'test')
	print(harrypotter)
main()


