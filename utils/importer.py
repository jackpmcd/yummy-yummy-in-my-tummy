# TODO: Write recipe importer for common websites
#   - Hello Fresh
#   - BBC Good Food
#   - Mob

# TODO: Write recipe importer for general websites

# TODO: Write recipe importer for typed recipes

from bs4 import BeautifulSoup
import unicodedata
import requests
import json
import re

def to_num(number):
    match = re.match(r"(\d+)?([\u00bc-\u00be])?", number)
    if not match:
        return float(number)

    whole = match.group(1)
    frac = match.group(2)

    value = 0
    if whole:
        value += int(whole)
    if frac:
        value += float(unicodedata.numeric(frac))
    return value

def parse_ingredient(full_ingredient):
    ingredient_arr = full_ingredient.split()
    quantity = to_num(ingredient_arr[0])
    if len(ingredient_arr) == 2:
        return quantity, ingredient_arr[1]
    else:
        return quantity, "n/a"

def hello_fresh_import():
    website_url = input("Please enter the recipe URL: ")

    page = requests.get(website_url).text

    soup = BeautifulSoup(page, "html.parser")

    recipe_title = soup.find("h1").get_text(strip=True)

    ingredient_divs = soup.find_all(
        "div",
        {"data-test-id": ["ingredient-item-shipped", "ingredient-item-not-shipped"]}
    )

    ingredients = []

    for div in ingredient_divs:
        p_tags = div.find_all("p")
        
        quantity, units = parse_ingredient(p_tags[0].get_text(strip=True))
        name = p_tags[1].get_text(strip=True)

        ingredients.append({
            "item": name,
            "quantity": quantity,
            "unit": units
        })
    
    instructions_div = soup.find(
        "div",
        {"data-test-id": "instructions"}
    )

    method = []
    instructions_p_tags = instructions_div.find_all("p")
    for p_tag in instructions_p_tags:
        method.append(p_tag.get_text(strip=True))

    full_recipe = {
        "name": recipe_title,
        "servings": 2,
        "ingredients": ingredients,
        "method": method
    } 

    return(full_recipe)

def website_import():
    options = ["Hello Fresh", "Mob", "BBC Good Food", "Other"]
    for i in range(len(options)):
        print(str(i+1) + ": " + options[i])

    import_method = int(input("Please enter the relevant number to select what website you'd like to import a recipe from: "))

    match import_method:
        case 1:
            recipe_json = hello_fresh_import()
        # case 2:
        #     recipe_json = mob_import()
        # case 3:
        #     recipe_json = good_food_import()
        # case 4:
        #     recipe_json = general_website_import()
    
    return recipe_json

def import_recipe():
    options = ["From website", "Manually"]
    for i in range(len(options)):
        print(str(i+1) + ": " + options[i])

    import_method = int(input("Please enter the relevant number to select what method you'd like to use to import your recipe: "))

    match import_method:
        case 1:
            output = website_import()
        case 2:
            output = manual_import()

    filename = "recipes.json"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            recipes = json.load(f)
    except FileNotFoundError:
        recipes = []

    recipes.append(output)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(recipes, f, indent=2)