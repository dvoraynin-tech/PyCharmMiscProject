def systema(x, y):
    if x > 8:
        z = 3 + y
    else:
        z = 9 * x * y
    return z

def factorial(n):
    Z = 1
    i = 1
    while i <= n:
        Z = Z * i
        i = i + 1
    return Z

x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
print("Результат обчислення системи =", systema(x, y))

n = int(input("Введіть число для факторіала: "))
print("Факторіал числа", n, "=", factorial(n))
