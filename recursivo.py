###suma recursiva de los primeros n números naturales###

def suma(n):
    r = 0
    for k in range(1, n + 1):
        r = r + k
    return r

n = 10
print(f"Suma de los primeros {n} = {suma(n)}")

###suma recursiva###

def sumaRecursiva(n):
    if n == 1:
        return 1
    else:
        return n + sumaRecursiva(n - 1)

n = 15
print(f"\nSuma de los primeros {n} numeros = {sumaRecursiva(n)}")