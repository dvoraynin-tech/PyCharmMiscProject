import json

filename = "countries.json"

countries = {
    "Україна": [41, 603],
    "Польща": [38, 313],
    "Німеччина": [83, 357],
    "Франція": [65, 551],
    "Іспанія": [47, 505]
}

with open(filename, "w", encoding="utf-8") as f:
    json.dump(countries, f, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except:
        print("Не вдалося відкрити файл!")
        return {}

def save_data(data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def show_all():
    data = load_data()
    if not data:
        print("Файл порожній або не знайдено!")
    else:
        for k, v in data.items():
            print(f"{k}: населення {v[0]} млн, площа {v[1]} тис.км²")

def add_country():
    data = load_data()
    name = input("Введіть назву держави: ").strip()
    if name in data:
        print("Така держава вже існує!")
        return
    try:
        population = float(input("Введіть чисельність населення (млн): "))
        area = float(input("Введіть площу (тис.км²): "))
        if population <= 0 or area <= 0:
            print("Населення і площа мають бути додатніми!")
            return
        data[name] = [population, area]
        save_data(data)
        print("Додано успішно!")
    except:
        print("Помилка введення даних!")

def delete_country():
    data = load_data()
    name = input("Введіть назву держави для видалення: ").strip()
    if name in data:
        del data[name]
        save_data(data)
        print("Держава видалена.")
    else:
        print("Такої держави немає!")

def search_country():
    data = load_data()
    word = input("Введіть частину назви для пошуку: ").strip().lower()
    found = False
    for k, v in data.items():
        if word in k.lower():
            print(f"{k}: населення {v[0]} млн, площа {v[1]} тис.км²")
            found = True
    if not found:
        print("Нічого не знайдено!")

def max_density():
    data = load_data()
    if not data:
        print("Файл порожній!")
        return

    max_country = None
    max_density_value = 0
    for name, info in data.items():
        density = info[0] / info[1]
        if density > max_density_value:
            max_density_value = density
            max_country = name

    print(f"Найбільша щільність населення у {max_country}: {max_density_value:.2f} млн/тис.км²")

    result = {"country": max_country, "density": round(max_density_value, 2)}
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print("Результат записано у result.json")

def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Показати всі дані")
        print("2. Додати нову державу")
        print("3. Видалити державу")
        print("4. Пошук держави")
        print("5. Знайти державу з найбільшою щільністю населення")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            add_country()
        elif choice == "3":
            delete_country()
        elif choice == "4":
            search_country()
        elif choice == "5":
            max_density()
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір!")

main()
