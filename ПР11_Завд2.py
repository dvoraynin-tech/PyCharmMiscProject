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

df["Month"] = df["Date"].dt.month

lanes = ["Berri1", "Maisonneuve_3", "Rachel / Papineau"]

print("\nНайпопулярніший місяць на 3 вибраних велодоріжках:")
for lane in lanes:
    monthly = df.groupby("Month")[lane].sum()
    best_month = monthly.idxmax()
    print(f"{lane}: найпопулярніший місяць — {best_month}")

lane_to_plot = "Berri1"

monthly_counts = df.groupby("Month")[lane_to_plot].sum()

plt.figure(figsize=(10, 5))
plt.plot(monthly_counts.index, monthly_counts.values)

plt.title(f"Завантаженість велодоріжки {lane_to_plot} по місяцях у 2017р.")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)

plt.show()
