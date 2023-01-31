def cakes(recipe, available):
    spent = {}
    for demanded in recipe:
        if demanded in available:
            qty = calculate_quantities(recipe[demanded], available[demanded])
            if  qty < 1:
                return 0
            else:
                spent[demanded] = qty
        else: return 0
    return math.floor(min(spent.values()))    


def calculate_quantities(demanded, current):
    return current / demanded 

recipe = {'flour': 41, 'cocoa': 28, 'pears': 4}
available = {'oil': 7592, 'sugar': 9631, 'pears': 2392, 'eggs': 8115, 'flour': 3222, 'cocoa': 5021, 'apples': 5995, 'cream': 8527, 'crumbles': 9983, 'chocolate': 2792}
print(cakes(recipe, available))