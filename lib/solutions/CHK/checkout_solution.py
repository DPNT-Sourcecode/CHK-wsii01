import re
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    if not bool(re.match('^[A-D]+$', skus)):
        return -1

    price_A = 50
    price_B = 30
    price_C = 20
    price_D = 15

    disc_A = 20
    disc_B = 15

    eligible_A = 150
    eligible_B = 60
    
    sku_dict = defaultdict(int)
    for item in skus:
        if item == 'A':
            sku_dict[item] += price_A
        if item == 'B':
            sku_dict[item] += price_B
        if item == 'C':
            sku_dict[item] += price_C
        if item == 'D':
            sku_dict[item] += price_D

    disc_fac = sku_dict['A'] // eligible_A
    sku_dict['A'] -= disc_fac * disc_A
    disc_fac = sku_dict['B'] // eligible_B
    sku_dict['B'] -= disc_fac * disc_B
    
    sum = 0
    for value in sku_dict.values():
        sum += value

    return sum
        

    





