equation = input('Введите пример, все знаки вводяься через пробел  или 0 для выхода:\n')
while equation != '0':
    eq = list(equation.split())
    a = float(eq[0])
    b = float(eq[2])
    answer = "нет решения"
    if eq[1] == '+':
        answer = a + b
    elif eq[1] == '-':
        answer = a - b
    elif eq[1] == '*':
        answer = a * b
    elif eq[1] == '/':
        if b != 0:
            answer = a / b
        else:
            print('На ноль делить нельзя')
    else:
        print('Неверный формат ввода')
    print(f'{equation} = {answer}')
    equation = input('Введите пример или 0 для выхода:\n')
print('До свидания')