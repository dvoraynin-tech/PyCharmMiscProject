import csv
import matplotlib.pyplot as plt

countries_data = {}
with open("Infl.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    year_index = header.index("2024 [YR2024]")

    for row in reader:
        country = row[3]
        try:
            value_2024 = float(row[year_index])
        except Exception:
            value_2024 = 0.0
        countries_data[country] = value_2024

selected_countries = ["Ukraine", "Poland", "Germany", "France"]
values = [countries_data.get(c, 0.0) for c in selected_countries]

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = pct * total / 100.0
        return f"{pct:.1f}% ({val:.1f})"
    return my_autopct

fig, ax = plt.subplots(figsize=(7, 7))

wedges, texts, autotexts = ax.pie(
    values,
    labels=selected_countries,
    autopct=make_autopct(values),
    startangle=140,
    colors=["cornflowerblue", "orange", "lightgreen", "red"],
    wedgeprops={'edgecolor': 'white', 'linewidth': 1},
    shadow=False
)

for txt in texts + autotexts:
    txt.set_fontsize(10)

ax.legend(wedges, selected_countries, title="Назви країн", loc="center left",
          bbox_to_anchor=(1.05, 0.5))

plt.title("Відсоток інфляції за 2024 рік")

plt.subplots_adjust(right=0.75)

plt.show()
