N = int(input("Введіть N (1 < N < 9): "))

if N <= 1 or N >= 9:
    print("Помилка: N має бути від 2 до 8")
else:
    for i in range(1, N + 1):
        for k in range(N - i):
            print(" ", end="")
        start = N - i + 1
        for j in range(start, N + 1):
            print(j, end="")
        print()