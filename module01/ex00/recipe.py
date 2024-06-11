class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type




	def __str__(self) -> str:
		txt = (f"Nom de la recette : {self.name}, Niveau : {self.cooking_lvl}")
		return txt
	def get_recipe_by_name(self, name):
		return name.