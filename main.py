from utils.meal_plan import pick_meals
from utils.importer import import_recipe

options = ["Generate a meal plan", "Import a recipe"]
for i in range(len(options)):
    print(str(i+1) + ": " + options[i])
    
command = int(input("Please enter the relevant number to select what you'd like to do: "))

match command:
    case 1:
        pick_meals()
    case 2:
        import_recipe()
