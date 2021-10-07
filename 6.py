a = int(input('Введите длину массива'))
Delta = int(input('Введите Delta'))
minim = 1000
b = 0
c = []
for d in range(a):
    c.append(int(input('Введите элемент массива')))
    minim = min(minim, c[d])
for d in range(a):
    if (c[d]) == minim + Delta or (c[d] == minim - Delta):
        b += 1
print(b)
