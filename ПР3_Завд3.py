sentence = input("Введіть речення: ")

words = sentence.split()

for word in words:
    if words.count(word) == 2:
        print("Знайдене слово, яке повторюється:", word)
        break
    else:
        print("Повторюваних слів немає")
        break