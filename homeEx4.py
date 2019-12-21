# читаем построчно
# 1 = ключ(блюдо)
# 2 = ингридиентов
# цикл сколько ингридиентов и берем из каждой сплитом

cook_book = {}
y = []
def get_shop_list_by_dishes(dishes, person_count):
    list_ingridients = {}
    list_1 = {}
    para = {}
    for ingridient in cook_book[dishes]:
        # print(ingridient)
        # ingridient['quantity'] = ingridient['quantity'] * person_count
        name_ing = ingridient['ingridient_name']
        count_ingrid = ingridient['quantity'] * person_count
        ingridient['quantity'] = count_ingrid

        list_ingridients.update(ingridient)
        list_ingridients.pop('ingridient_name')
        # print(list_ingridients)
        para = dict.fromkeys([name_ing], list_ingridients)
        # print(para)
        list_1.update(para)
        print(list_1)
        # list_ingridients.clear()
        # list_ingridients['quantity'] = ingridients_['quantity'] * person_count
        # print(list_ingridients)
        # list_1.update[list_ingridients]
    # print(list_1)
    # try:
    # except KeyError:
    #     h.popitem(ingridient_1)



    # def list_ingrid(dish1):

            # current_ingrid = list(list_1.keys())
            # print(list_ingridients)
            # print(current_ingrid)
            # print(ingridients_['ingridient_name'])
            # print(current_ingrid.count(ingridients_['ingridient_name']))
            # print(ingridients_['quantity'])
            # if current_ingrid.count(ingridients_['ingridient_name']) == 0:
            #     list_ingridients['quantity'] = ingridients_['quantity'] * person_count
            # else:
            #     new_list_quantity = list_1[ingridients_['ingridient_name']]
            #
            #     print(new_list_quantity, ingridients_['ingridient_name'])
            #     print(list_1)

                # print(t1)
                # print(ingridients_['quantity'])

                # new_list_quantity['quantity'].update(new_list_quantity['quantity'] + (ingridients_['quantity'] * person_count))
                # print(t1)

                # list_1[ingridients_['ingridient_name']].update(new_list_quantity)

            # print(ingridients_['ingridient_name'])
            # list_1[ingridients_['ingridient_name']] = list_ingridients
            # print(list_1)
    # if type(dishes) == type(y):
    #     for dish in dishes:
    #         list_ingrid(dish)
    # else:
    #     list_ingrid(dishes)
    # return list_1

with open('recipes.txt', encoding='utf8') as f:
    while True:
        try:
            dish_name = f.readline().strip()
            if dish_name == '':
                break
            num_ingrid = f.readline().strip()
            composition = []

            for i in range(int(num_ingrid)):
                ingrid_list = [var1 for var1 in f.readline().split(' | ')]
                ingridients_ = {'ingridient_name': ingrid_list[0], 'quantity': int(ingrid_list[1]), 'measure': ingrid_list[2].strip()}
                composition.append(ingridients_)
            cook_book[dish_name] = composition
            f.readline()
        except (EOFError, ValueError):
            break
    # for x in cook_book:
    #     print(x)
    #     for y in cook_book[x]:
    #         print(y)
print(get_shop_list_by_dishes('Омлет', 2))






