import re
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    if not bool(re.match('^[A-F]+$', skus)):
        return -1

    price_A = 50
    price_B = 30
    price_C = 20
    price_D = 15
    price_E = 40
    price_F = 10

    disc_A = 50
    disc_B = 15
    disc_F = price_F

    eligible_A = 250
    eligible_B = 60
    eligible_E = 80
    eligible_F = 30
    
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
        if item == 'E':
            sku_dict[item] += price_E
        if item == 'F':
            sku_dict[item] += price_F

    disc_fac = sku_dict['A'] // eligible_A
    sku_dict['A'] -= disc_fac * disc_A
    temp = sku_dict['A'] - ( 200 * disc_fac )
    if temp >= 150:
        additional_disc_fac = temp // 150
        sku_dict['A'] -= additional_disc_fac * 20
    
    if sku_dict['B'] > 0:
        disc_fac = sku_dict['E'] // eligible_E
        additional_disc = disc_fac * price_B
        sku_dict['B'] -= additional_disc
        if sku_dict['B'] > 0:
            disc_fac = sku_dict['B'] // eligible_B
            sku_dict['B'] -= disc_fac * disc_B
    
    disc_fac = sku_dict['F'] // eligible_F
    sku_dict['F'] -= disc_fac * price_F
    
    sum = 0
    for value in sku_dict.values():
        sum += value

    return sum
        

    


