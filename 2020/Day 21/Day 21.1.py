filelines = open("input.txt").read().split("\n")
all_allergens = []
all_food = []
allergen_dict = {}
num_foods = len(filelines)


for foods in filelines:
    food = foods.split("(")[0].rstrip().split(" ")  # List with all the ingriediants
    allergens = "".join(foods.split("(")[1].split(" ")[1:]).rstrip(")").split(",")  # List with all the allergens

    all_allergens = list(set(all_allergens + allergens))  # Add all new allergens to allergens list
    all_food = all_food + food  # Add all foods to food list

    for allergen in allergens:  # Loop through all ingriediants in food
        if allergen_dict.get(allergen) is None:  # Initialize List
            allergen_dict[allergen] = food

        # Get all duplicats and set them as new List
        newList = []
        for ingridient1 in allergen_dict.get(allergen):
            for ingridient2 in food:
                if ingridient1 == ingridient2:
                    newList.append(ingridient1)
        allergen_dict[allergen] = newList

# Count allergen free food
food_no_allergen = all_food
for allergen in allergen_dict.keys():
    for ingridient in allergen_dict.get(allergen):
        while ingridient in food_no_allergen:
            food_no_allergen.remove(ingridient)

print(len(food_no_allergen))