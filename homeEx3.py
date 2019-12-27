

def polish_calc(data1):
    try:
        oper1 = (data1[0])
        a = int(data1[1])
        b = int(data1[2])
        assert oper1 in ["+", "-", "/", "*"]
    except (ValueError, AssertionError):
        print("Неизвестная операция или введены не числа")
        return ""
    if oper1 == "+":
        return a + b
    elif oper1 == "-":
        return a - b
    elif oper1 == "*":
        return a * b
    elif oper1 == "/":
        try:
            return a / b
        except ZeroDivisionError:
           print("Деление на ноль")

if __name__ == '__main__':
    user_input = input("Введите операцию и два числа через пробел: ")
    input_list = user_input.split(" ")

    if len(input_list) != 3:
        print("Неверное количество аргументов")
    elif polish_calc(input_list) != None:
        print(f"Результат вычислений: {polish_calc(input_list)}")


