import re
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not bool(re.match('^[A-D]+$', skus)):
        return -1
    
    sku_dict = defaultdict(int)
    for item in skus:
        if item == 'A':
            sku_dict[item] += 50
            eligible = sku_dict[item]//150
            if eligible >= 1:
                sku_dict[item] -= eligible * 20
        if item == 'B':
            sku_dict[item] += 30
            eligible = sku_dict[item]//60
            if eligible >= 1:
                sku_dict[item] -= eligible *15
        if item == 'C':
            sku_dict[item] += 20
        if item == 'D':
            sku_dict[item] += 15

    sum = 0
    for value in sku_dict.values():
        sum += value

    return sum
        

    

