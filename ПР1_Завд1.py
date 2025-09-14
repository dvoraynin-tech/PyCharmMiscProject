a = int(input ("Введіть а: "))
while (a < 1 or a > 100):
    a = int(input ("Введіть а повторно: "))
b = int(input ("Введіть b: "))
while (b < 1 or b > 100):
    b = int(input ("Введіть b повторно: "))
if a < b:
    X = ((a * 3) - 5) / b
elif a == b:
    X = -4
else:
    X = (a**4 + b) / a
print("Результат обчислення виразу Х =" , X)