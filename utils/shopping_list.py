def make_shopping_list(curr_meal_plan):
    shopping_list = {}
    for meals in curr_meal_plan:
        meal_ingreds = meals['ingredients']
        meal_scale = 4 / meals['servings'] # scales all recipes to 4 portions

        for ingred in meal_ingreds:
            name = ingred["item"]
            quantity = ingred["quantity"] * meal_scale
            unit = ingred["unit"]
            
            if name not in shopping_list:
                shopping_list[name] = {unit: quantity}
            else:
                if unit in shopping_list[name]:
                    shopping_list[name][unit] += quantity
                else:
                    shopping_list[name][unit] = quantity

    return shopping_list