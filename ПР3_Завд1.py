text = input("Введіть рядок: ")

if len(text) >= 3:
    result = text[2::3]
    print("Кожна третя літера у слові:", result)
else:
    print("Слово закоротке для зрізу.")