def san(n = int(1e6 + 7)):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = True
    i = 2
    while i * i <= n:
        if primes[i] == True:
            for j in range(i * i, n + 1, i):
                primes[j] = True
        i += 1
    primes_numbers = []
    for x in range(0, n + 1):
        if primes[x]:
            primes_numbers.append(x)
    return primes_numbers
import math
def check(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    can = int(math.sqrt(n))
    for i in range(2, can + 1):
        if n % i == 0:
            return False
    return True

def san_max_uoc_nt(n = int(1e6 + 7)): #?? 
    snt = [0] * (n + 1)
    for i in range(n + 1):
        snt[i] = i
    i = 2
    while i * i <= n:
        if snt[i] == i:
            for j in range(2*i, n + 1, i):
                snt[j] = i
        i += 1
    return snt

ans = san_max_uoc_nt(20)
for i in range(len(ans)):
    print(i, ans[i])