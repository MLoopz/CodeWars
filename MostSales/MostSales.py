def top3(products, amounts, prices):
    listOfProducts=list()
    listOfAmounts=list()
    for i in range(0,len(products)):
        listOfAmounts.append([amounts[i]*prices[i],i])

    listOfAmounts.sort(key = sortFirst, reverse=True)  
    for i in range(0,len(products)):
        listOfProducts.append(products[listOfAmounts[i][1]])
    return listOfProducts[:3]

def sortFirst(val): 
    return val[0]

print(top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3,24,8], [199,299,399]))# ["Cell Phones", "Vacuum Cleaner", "Computer"]
print(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [5, 25, 2, 7, 10, 3, 2, 24], [51, 225, 22, 47, 510, 83, 82, 124]))# ['Vacuum Cleaner', 'Gold', ' Speakers']
print(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [0, 12, 24, 17, 19, 23, 120, 8], [9, 24, 29, 31, 51, 8, 120, 14]))# ['Lego', 'Gold', 'Computer']