countries = {
    "Україна": (41, 603),
    "Польща": (38, 313),
    "Німеччина": (83, 357),
    "Франція": (65, 551),
    "Іспанія": (47, 505)
}

def show_all(data):
    if not data:
        print("Словник порожній.")
    else:
        for country, info in data.items():
            print(f"{country}: населення {info[0]} млн, площа {info[1]} тис.км²")

def add_country(data):
    try:
        name = input("Введіть назву держави: ").strip()
        if not name.isalpha():
            raise ValueError("Назва країни повинна містити лише букви!")

        if name in data:
            raise KeyError("Така держава вже є у словнику!")

        population = float(input("Введіть чисельність населення (млн): "))
        area = float(input("Введіть площу (тис.км²): "))

        if population <= 0 or area <= 0:
            raise ValueError("Населення і площа мають бути додатніми числами!")

        '''if (population, area) in data.values():
            raise ValueError("Такі ж дані вже існують у словнику!")'''

        data[name] = (population, area)
        print("Держава успішно додана!")

    except ValueError as ve:
        print("Помилка:", ve)
    except KeyError as ke:
        print("Помилка:", ke)

def delete_country(data):
    try:
        name = input("Введіть назву держави для видалення: ").strip()
        if name not in data:
            raise KeyError("Такої держави немає у словнику!")
        del data[name]
        print("Держава успішно видалена!")
    except KeyError as ke:
        print("Помилка:", ke)

def show_sorted(data):
    if not data:
        print("Словник порожній.")
    else:
        for country in sorted(data.keys()):
            population, area = data[country]
            print(f"{country}: населення {population} млн, площа {area} тис.км²")

def population_density(item):
    country, data = item
    population = data[0]
    area = data[1]
    return population / area


def max_density(data):
    if not data:
        print("Словник порожній.")
        return

    max_country = max(data.items(), key=population_density)
    density = population_density(max_country)

    print(f"{max_country[0]} має найбільшу щільність населення — {density:.2f} млн/тис.км²")


def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Вивести всі значення словника")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Переглянути словник за відсортованими ключами")
        print("5. Знайти державу з максимальною щільністю населення")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_all(countries)
        elif choice == "2":
            add_country(countries)
        elif choice == "3":
            delete_country(countries)
        elif choice == "4":
            show_sorted(countries)
        elif choice == "5":
            max_density(countries)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз!")

main()