import csv
import matplotlib.pyplot as plt

years = []
countries_data = {}

with open("Infl.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    years = [h.split()[0] for h in header[5:]]

    for row in reader:
        country = row[3]
        data = []
        for value in row[5:]:
            try:
                data.append(float(value))
            except ValueError:
                data.append(0.0)
        if len(data) > len(years):
            data = data[:len(years)]
        countries_data[country] = data

ukraine = countries_data["Ukraine"]
poland = countries_data["Poland"]

plt.figure(figsize=(10, 5))
plt.plot(years, ukraine, color="blue", linewidth=2, linestyle='-', label="Ukraine")
plt.plot(years, poland, color="yellow", linewidth=2, linestyle='-', label="Poland")
plt.xlabel("Рік")
plt.ylabel("Інфляція, %")
plt.title("Динаміка інфляції (Україна vs Польща)")
plt.legend()
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()

country_name = input("Введіть назву країни: ")
if country_name in countries_data:
    data = countries_data[country_name]
    if len(data) > len(years):
        data = data[:len(years)]
    plt.figure(figsize=(10, 5))
    plt.bar(years, data, color="green")
    plt.xlabel("Рік")
    plt.ylabel("Інфляція, %")
    plt.title(f"Показники інфляції – {country_name}")
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()
else:
    print("Такої країни немає у файлі.")
