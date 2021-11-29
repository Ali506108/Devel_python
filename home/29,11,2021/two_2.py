from random import randint
arr = []
y = 0
p = int(input('введите ваш балл 1 / 10 : '))
while y <= 10:
    arr.append(randint(1,10))
    arr.append(p)
    y += 1
    max_a = max(arr)
print(max_a)
print(arr)