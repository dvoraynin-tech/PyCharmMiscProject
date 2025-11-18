import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("comptagevelo2017.csv")

print("Перші рядки:")
print(df.head())

print("\nІнформація про DataFrame:")
print(df.info())

print("\nОписова статистика:")
print(df.describe())

numeric_cols = df.select_dtypes("number")

total_year_all = numeric_cols.sum().sum()

print("\nЗагальна кількість велосипедистів за рік на всіх велодоріжках:")
print(total_year_all)

total_by_lane = numeric_cols.sum()

print("\nЗагальна кількість велосипедистів за рік на кожній велодоріжці:")
print(total_by_lane)

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

df["Month"] = df["Date"].dt.month_name(locale="uk_UA")

lanes = ["Berri1", "Maisonneuve_3", "Rachel / Papineau"]

print("\nНайпопулярніший місяць на 3 вибраних велодоріжках:")
for lane in lanes:
    monthly = df.groupby(df["Date"].dt.month)[lane].sum()
    best_month_num = monthly.idxmax()
    best_month_name = pd.to_datetime(str(best_month_num), format="%m").month_name(locale="uk_UA")
    print(f"{lane}: найпопулярніший місяць — {best_month_name}")

lane_to_plot = "Berri1"

monthly_counts = df.groupby(df["Date"].dt.month)[lane_to_plot].sum()

month_names = pd.to_datetime(monthly_counts.index, format="%m").month_name(locale="uk_UA")

plt.figure(figsize=(10, 5))
plt.plot(month_names, monthly_counts.values)

plt.title(f"Завантаженість велодоріжки {lane_to_plot} по місяцях у 2017р.")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)

plt.show()
