# 2. Напишите цикл `while`, который просит пользователя ввести `два` числа. Числа должны
# быть `сложены`, и показана `сумма`. Цикл должен запрашивать у пользователя, `желает ли` он
# выполнить операцию еще раз. Если да, то цикл должен повториться, в противном случае
# он должен завершиться .

again = 1
while again == 1:
    num_1 = int(input('Введите число: '))
    num_2 = int(input('введите число: '))
    sum = num_1 + num_2 
    print(sum)
    survey = input('хоттите повтарит цикл: ')
    if survey == 'да':
        num_1 = int(input('Введите число: '))
        num_2 = int(input('введите число: '))
        sum = num_1 + num_2
        print(sum)
    else:
        print('ok')
        again = False