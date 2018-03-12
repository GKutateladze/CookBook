# -*- coding: utf8 -*-

# cook_book = {
#   'яйчница': [
#     {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#   'стейк': [
#     {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#     {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#   'салат': [
#     {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#     {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#     {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
#   }

import pprint

def get_products(filename):
    with open(filename) as recipes:
        cook_book = dict()

        for line in recipes:
            dish_name = line.strip().lower()
            cook_book[dish_name] = list()

            ingridients_count = int(recipes.readline().strip())

            for i in range(ingridients_count):
                ingridient = recipes.readline().strip().split(' | ')

                ingridient_name = ingridient[0].lower()
                ingridient_quantity = int(ingridient[1])
                ingridient_measure = ingridient[2]

                ingridient = {
                    'ингредиент': ingridient_name,
                    'количество': ingridient_quantity,
                    'мера': ingridient_measure
                }

                cook_book[dish_name].append(ingridient)

            recipes.readline()
    pprint.pprint(cook_book)
    return cook_book

products = get_products("recipe.txt")

# def get_shop_list_by_dishes(dishes, person_count):
#   shop_list = {}
#   for dish in dishes:
#     for ingridient in cook_book[dish]:
#       new_shop_list_item = dict(ingridient)
#
#       new_shop_list_item['quantity'] *= person_count
#       if new_shop_list_item['ingridient_name'] not in shop_list:
#         shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#       else:
#         shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
#   return shop_list
#
# def print_shop_list(shop_list):
#   for shop_list_item in shop_list.values():
#     print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
#                             shop_list_item['measure']))
#
# def create_shop_list():
#   person_count = int(input('Введите количество человек: '))
#   dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
#     .lower().split(', ')
#   shop_list = get_shop_list_by_dishes(dishes, person_count)
#   print_shop_list(shop_list)




