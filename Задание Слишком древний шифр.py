n = int(input('Введите число выпавшее в первом поле: '))
result = []
for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)
print(''.join(map(str, result)))