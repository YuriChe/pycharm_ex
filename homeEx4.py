# читаем построчно
# 1 = ключ(блюдо)
# 2 = ингридиентов
# цикл сколько ингридиентов и берем из каждой сплитом

cook_book = {}

def get_shop_list_by_dishes(dishes, person_count):
    list_ingridients = {}
    for dish in dishes:
        list_one_dish_ingridients = cook_book[dish] #получил список из ингридиентов блюда
        for ing_1 in list_one_dish_ingridients:
            # print(f'Первыйй {ing_1}')
            # ing_1['quantity'] = ing_1['quantity'] * person_count
            # print(ing_1)
            list_all_ing = list(list_ingridients.keys())
            if list_all_ing.count(ing_1['ingridient_name']) == 0:

                list_ingridients[ing_1['ingridient_name']] = {'measure': ing_1['measure'], 'quantity': int(ing_1['quantity'] * person_count)}
                # print(f'Прямой {list_ingridients}')
            else:
                list_ingridients[ing_1['ingridient_name']]['quantity'] = (ing_1['quantity'] * person_count) + list_ingridients[ing_1['ingridient_name']]['quantity']
                # print(f'после еслз {list_ingridients}')

    return list_ingridients


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
    # print(cook_book)

print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))






