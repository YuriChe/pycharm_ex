# читаем построчно
# 1 = ключ(блюдо)
# 2 = ингридиентов
# цикл сколько ингридиентов и берем из каждой сплитом

cook_book = {}

with open('recipes.txt', encoding='utf8') as f:
    while True:
        try:
            dish_name = f.readline().strip()
            num_ingrid = f.readline().strip()
            print(num_ingrid)
            composition = []
            counter = 0
            while True:
                        ingrid_list = [var1 for var1 in f.readline().split(' | ')]
                        ingridients_ = {'ingridient_name': ingrid_list[0], 'quantity': int(ingrid_list[1]), 'measure': ingrid_list[2].strip()}
                        composition.append(ingridients_)
                        counter += 1
                        if counter == num_ingrid:
                            break
        except IndexError:
           break
        cook_book[dish_name] = composition
        f.readline().strip()
        print(cook_book)




