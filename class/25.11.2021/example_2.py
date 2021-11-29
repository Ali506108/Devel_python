def main():
    my_file =  open('C:\\Users\\Acer\\Desktop\\A4game-site\\ali.txt','r')

    line_1 = my_file.readline()
    line_2 = my_file.readline()
    line_3 = my_file.readline()

    line1 = line_1.rstrip('\n')
    line2 = line_2.rstrip('\n')
    line3 = line_3.rstrip('\n')

    my_file.close()
    print(line1)
    print(line2)
    print(line3)


main()