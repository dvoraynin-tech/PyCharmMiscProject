num = str(input("Введіть шестизначне натуральне число: "))

while len(num) < 6 or len(num) > 6 or num.isdigit() == 0:

    num = str(input("Введіть число ще раз, так як воно не шестизначне або це не число: "))

sum = 0

for i in range (len(num)):

    sum += int(num[i])

print("Сума усіх чисел у шестизначному числі = ", sum)