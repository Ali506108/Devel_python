def main():
    print('введите именна трех друзей: ')
    name_1 = input('введите имя друго: ')
    name_2 = input('введите имя друго: ')
    name_3 = input('введите имя друго: ')

    my_file =  open('C:\\Users\\Acer\\Desktop\\A4game-site\\ali.txt','w')

    my_file.write(name_1 + '\n')
    my_file.write(name_2 + '\n')
    my_file.write(name_3 + '\n')

    my_file.close()
    print('ваше файлы сохранились')


main()