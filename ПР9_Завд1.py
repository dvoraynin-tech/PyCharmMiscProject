import csv

try:
    with open("Inflation.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        print("Вміст файлу Inflation.csv:\n")
        print(header)

        data = []
        for row in reader:
            print(row)
            data.append(row)

except FileNotFoundError:
    print("Помилка: файл Inflation.csv не знайдено")
    exit()
except Exception as e:
    print("Виникла помилка при відкритті файлу:", e)
    exit()

print("\nВведіть назви країн через пробіл:")

countries_input = input("Пошук за наступними країнами: ")
countries = [c.strip() for c in countries_input.split(" ")]

found = []

for row in data:
    country_name = row[3]
    if country_name in countries:
        found.append(row)

if not found:
    print("Не знайдено всіх країн із вказаних")
else:
    print("\nЗнайдені дані:")
    for row in found:
        print(row)

    try:
        with open("result.csv", "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            writer.writerows(found)
        print("\nРезультати збережено у файл result.csv")
    except Exception as e:
        print("Помилка при записі у файл:", e)
