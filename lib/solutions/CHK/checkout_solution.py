import re
from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    if not bool(re.match('^[A-Z]+$', skus)):
        return -1

    price = defaultdict(int)
    price['A'] = 50
    price['B'] = 30
    price['C'] = 20
    price['D'] = 15
    price['E'] = 40
    price['F'] = 10
    price['G'] = 20
    price['H'] = 10
    price['I'] = 35
    price['J'] = 60
    price['K'] = 80
    price['L'] = 90
    price['M'] = 15
    price['N'] = 40
    price['O'] = 10
    price['P'] = 50
    price['Q'] = 30
    price['R'] = 50
    price['S'] = 30
    price['T'] = 20
    price['U'] = 40
    price['V'] = 50
    price['W'] = 20
    price['X'] = 90
    price['Y'] = 10
    price['Z'] = 50

    disc_A = 50
    disc_B = 15
    disc_F = price['F']
    disc_H = 20
    disc_K = 10
    disc_P = 50
    disc_Q = 10
    disc_U = price['U']
    disc_V = 20

    eligible_A = 250
    eligible_B = 60
    eligible_E = 80
    eligible_F = 30
    eligible_H = 100
    eligible_K = 160
    eligible_N = 120
    eligible_P = 250
    eligible_Q = 90
    eligible_R = 150
    eligible_U = 160
    eligible_V = 150
    
    sku_dict = defaultdict(int)
    for item in skus:
        sku_dict[item] += price[item]

    disc_fac = sku_dict['A'] // eligible_A
    sku_dict['A'] -= disc_fac * disc_A
    temp = sku_dict['A'] - ( 200 * disc_fac )
    if temp >= 150:
        additional_disc_fac = temp // 150
        sku_dict['A'] -= additional_disc_fac * 20
    
    if sku_dict['B'] > 0:
        disc_fac = sku_dict['E'] // eligible_E
        additional_disc = disc_fac * price['B']
        sku_dict['B'] -= additional_disc
        if sku_dict['B'] < 0:
            sku_dict['B'] = 0
        if sku_dict['B'] > 0:
            disc_fac = sku_dict['B'] // eligible_B
            sku_dict['B'] -= disc_fac * disc_B
    
    disc_fac = sku_dict['F'] // eligible_F
    sku_dict['F'] -= disc_fac * price['F']

    disc_fac = sku_dict['H'] // eligible_H
    sku_dict['H'] -= disc_fac * disc_H
    temp = sku_dict['H'] - ( 80 * disc_fac )
    if temp >= 50:
        additional_disc_fac = temp // 50
        sku_dict['H'] -= additional_disc_fac * 5

    disc_fac = sku_dict['K'] // eligible_K
    sku_dict['K'] -= disc_fac * disc_K

    if sku_dict['M'] > 0:
        disc_fac = sku_dict['N'] // eligible_N
        additional_disc = disc_fac * price['M']
        sku_dict['M'] -= additional_disc
        if sku_dict['M'] < 0:
            sku_dict['M'] = 0

    disc_fac = sku_dict['P'] // eligible_P
    sku_dict['P'] -= disc_fac * disc_P

    if sku_dict['Q'] > 0:
        disc_fac = sku_dict['R'] // eligible_R
        additional_disc = disc_fac * price['Q']
        sku_dict['Q'] -= additional_disc
        if sku_dict['Q'] < 0:
            sku_dict['Q'] = 0
        if sku_dict['Q'] > 0:
            disc_fac = sku_dict['Q'] // eligible_Q
            sku_dict['Q'] -= disc_fac * disc_Q

    disc_fac = sku_dict['U'] // eligible_U
    sku_dict['U'] -= disc_fac * price['U']

    disc_fac = sku_dict['V'] // eligible_V
    sku_dict['V'] -= disc_fac * disc_V
    temp = sku_dict['V'] - ( 130 * disc_fac )
    if temp >= 100:
        additional_disc_fac = temp // 100
        sku_dict['V'] -= additional_disc_fac * 10
    
    sum = 0
    for value in sku_dict.values():
        sum += value

    return sum
        

    

