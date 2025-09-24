n = int(input("Задайте розмір масиву "))

print(f"Введіть {n} натуральних елементів у масив:")

arr = []

for i in range(n):
    x = float(input())
    arr.append(x)

print("Ненульові елементи в зворотному порядку:")

for i in range(n-1, -1, -1):
    if arr[i] != 0:
        print(arr[i])