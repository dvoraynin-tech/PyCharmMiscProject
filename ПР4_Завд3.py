def delete():
    A = input("Введіть елементи списку: ").split()

    print("Початковий список:", A)

    value = input("Інформаційний атрибут елемента для видалення: ")

    result = []
    for x in A:
        if x != value:
            result.append(x)

    print("Список після видалення:", result)
    return result

delete()