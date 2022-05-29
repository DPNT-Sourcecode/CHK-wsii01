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
        if item == 'B':
            sku_dict[item] += 30
        if item == 'C':
            sku_dict[item] += 20
        if item == 'D':
            sku_dict[item] += 15

    disc_fac = sku_dict['A'] // 150
    sku_dict['A'] -= disc_fac * 20
    disc_fac = sku_dict['B'] // 60
    sku_dict['B'] -= disc_fac * 15
    
    sum = 0
    for value in sku_dict.values():
        sum += value

    return sum
        

    



