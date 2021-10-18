def rad(n):
    wynik = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            wynik *= i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        wynik *= n
    return wynik

s=0
for i in range(0,255):
    
    x=(rad(i))
    if x==10:
        s=s+1
print(s)


def rad(n):
    wynik =1
    i=2
    while i * i <= n:
        if n % i == 0:
            wynik *= i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        wynik *= n
    return wynik

o = 0
for i in range(0, 255):
    x = (rad(i))
    if x == 10:
        o += 1
print(o)