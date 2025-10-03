import json
import random
from utils.shopping_list import make_shopping_list

def pretty_print_shopping_list(shopping_list):
    lines = []
    for item, units in shopping_list.items():
        for unit, qty in units.items():
            if isinstance(qty, float) and qty.is_integer():
                qty = int(qty)
            else:
                qty = round(qty, 2)

            if unit == "n/a" or unit == "unit(s)":
                lines.append(item + " - " + str(qty))
            else:
                lines.append(item + " - " + str(qty) + " " + unit)
    return lines

def display_shopping_list(meal_plan):
    generate_list_check = input("Would you like to generate a shopping list for the meal plan? (y/n): ")
    if generate_list_check.lower() == "y":
        shopping_list = make_shopping_list(meal_plan)
        pretty_list = pretty_print_shopping_list(shopping_list)
        print("\n".join(pretty_list))
    else:
        print("Okay! See ya.")

def pick_meals():
    filename = "recipes.json"

    with open(filename, "r", encoding="utf-8") as f:
        recipes = json.load(f)

    meal_plan = random.sample(recipes, 3)

    for recipe in meal_plan:
        print(f"- {recipe['name']}")

    display_shopping_list(meal_plan)

