

def polish_calc(data1):
    try:
        oper1 = (data1[0])
        a = int(data1[1])
        b = int(data1[2])
        assert oper1 in ["+", "-", "/", "*"]
    except AssertionError:
        print("Неизвестная операция")
        return
    if oper1 == "+":
        return a + b
    elif oper1 == "-":
        return a - b
    elif oper1 == "*":
        return a * b
    else:
        try:
            return a / b
        except (ZeroDivisionError):
           print("Деление на ноль")

user_input = input("Введите операцию и два числа через пробел: ")
input_list = user_input.split(" ")

# print(len(input_list))
try:
    if len(input_list) != 3:
        print("Неверное количество аргументов")
    else:
        print(f"Результат вычислений: {polish_calc(input_list)}")
except (UnboundLocalError, Exception):
    print("Неверные параметры")

