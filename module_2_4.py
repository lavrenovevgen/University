numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = {}
for i in numbers:
    if i == 2:
        primes.append(i)
        continue
    for j in range(2,i//2 + 2): # i разделил на 2 и прибавил 2 для оптимизации так как если делить число на число, которое больше половины делимого, целое число не получится
        if i % j != 0:
            is_primes.setdefault(i, []).append(True)
        else:
            is_primes.setdefault(i, []).append(False)
            break
for key, values in is_primes.items():
    if all(values):
        primes.append(key)
    else:
        not_primes.append(key)

print(primes)
print(not_primes)