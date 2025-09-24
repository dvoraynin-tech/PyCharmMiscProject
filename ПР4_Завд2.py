n = 7
arr = []

for i in range(n):
    row = []
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            row.append(1)
        else:
            row.append(0)
    arr.append(row)

for r in arr:
    print(*r)
