def element(lst):
    new_list = []
    for i in range(2, len(lst), 3):
        new_list.append(lst[i])
    print("Новий список з кожного третього елемента:", new_list)

user_input = input("Введіть елементи списку: ")
my_list = user_input.split()

print("Початковий список:", my_list)

element(my_list)