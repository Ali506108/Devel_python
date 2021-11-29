a = ["Banana" , "Mango" , "pizza" , "apple"]

print(a)
print(type(a))

print("Списек покуаек: ", end=' ')
for i in a:
    print(i, end=' ')

a.append('Doner')
print(a)

a.sort()
print(a)

print('hey bro', a[0])

del a[0]
print(a)

num = [1 , 2 , 3 , 7 , 4/6 ,0.02]
num.sort()
print(num)