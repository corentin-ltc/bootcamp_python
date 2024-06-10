cookbook = {
	'Sandwich' : ('ham', 'bread', 'cheese', 'tomatoes', 10, 'lunch'),
	'Cake' : ('flour', 'sugar', 'eggs', 60, 'dessert'),
	'Salad' : ('avocado' , 'arugula', 'tomatoes', 'spinach', 15, 'dinner or lunch'),
}

def print_recipes_names():
	for meal in cookbook.keys():
		print(f'{meal}')

def print_recipe():
	print("Please enter a recipe name to get its details:")
	meal = input()
	if meal in cookbook:
		ingredients = cookbook[meal][:-2]
		prep_time = cookbook[meal][-2]
		meal_type = cookbook[meal][-1]
		print(f"Recipe for {meal}:")
		print(f"Ingredients list: {', '.join(ingredients)}")
		print(f"To be eaten for {meal_type}.")
		print(f"Takes {prep_time} minutes of cooking.")
	else:
		print('This recipe does not exists.')

def delete_recipe():

	print("Please enter the recipe to delete:")
	meal = input()
	if meal in cookbook:
		del cookbook[meal]
		print(f"The recipe for a {meal} was successfully deleted")
	else:
		print('This recipe does not exists.')

def add_recipe():
	print("Enter recipe's name:")
	meal = input()
	if meal in cookbook:
		print('This recipe already exists.')
		return
	print("Enter ingredients:")
	ingredients = []
	while True:
		ingredient = input()
		if not ingredient:
			break
		ingredients.append(ingredient)
	print("Enter a meal type")
	meal_type = input()
	print("Enter a preparation time in minutes")
	prep_time = int(input())
	cookbook[meal] = (*ingredients, prep_time, meal_type)
	print(f"The recipe of a {meal} was successfully added to the cookbook !")

def main():
	print("Welcome to the Python Cookbook !")
	print("\nList of available option:", end='\n\n')
	print("1: Add a new recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit", end='\n\n')
	while (1):
		print("Please select an option")
		option = input()
		if option == '1':
			add_recipe()
		elif option == '2':
			delete_recipe()
		elif option == '3':
			print_recipe()
		elif option == '4':
			for meal in cookbook.keys():
				ingredients = cookbook[meal][:-2]
				prep_time = cookbook[meal][-2]
				meal_type = cookbook[meal][-1]
				print(f"\nRecipe for {meal}:")
				print(f"Ingredients list: {', '.join(ingredients)}")
				print(f"To be eaten for {meal_type}.")
				print(f"Takes {prep_time} minutes of cooking.\n")
		elif option == '5':
			print("Cookbook closed. Goodbye !")
			return
		else: 
			print("Wrong option, please select between 1 and 5.")
			print("\nList of available option:", end='\n\n')
			print("1: Add a new recipe")
			print("2: Delete a recipe")
			print("3: Print a recipe")
			print("4: Print the cookbook")
			print("5: Quit", end='\n\n')
main()
		



	


		