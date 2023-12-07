filelines = open("input.txt").read().split("\n")
allergen_dict = {}


for foods in filelines:
    food = foods.split("(")[0].rstrip().split(" ")  # List with all the ingriediants
    allergens = "".join(foods.split("(")[1].split(" ")[1:]).rstrip(")").split(",")  # List with all the allergens

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

# Get Dangerous List
dangerousList = []
allergens = list(allergen_dict.keys())
allergens.sort()
for allergen in allergens:
    dangerousList.append([allergen, allergen_dict.get(allergen)])

# Remove Possible Multiple Occurencens of Allegen Encodings
removeList = []
for i in range(len(dangerousList)):
    for dangerousItem in dangerousList:
        if len(dangerousItem[1]) == 1:
            removeList.append(dangerousItem[1][0])
        else:
            for dangerousAllergen in removeList:
                if dangerousAllergen in dangerousItem[1]:
                    dangerousItem[1].remove(dangerousAllergen)

# Print nicley
printstr = ""
for dangerousItem in dangerousList:
    printstr += dangerousItem[1][0]
    printstr += ","
printstr = printstr.rstrip(",")
print(printstr)
