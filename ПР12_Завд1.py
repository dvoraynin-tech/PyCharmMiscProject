import csv
import math
import os
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource, HoverTool

CSV_FILENAME = "Infl.csv"
OUTPUT_HTML = "inflation_report.html"
BAR_HTML = "inflation_bar.html"
RESULT_CSV = "selected_country.csv"

#   ФУНКЦІЇ ДЛЯ CSV
def load_csv(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            data = list(reader)
        print(f"Файл '{filename}' успішно зчитано. Знайдено {len(data)} рядків.")
        return header, data
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None, None
    except Exception as e:
        print("Помилка при читанні файлу:", e)
        return None, None


def parse_years(header):
    if not header or len(header) < 5:
        return []
    return [h.split()[0] for h in header[4:]]


def get_country_row(data, country_name):
    if data is None:
        return None
    name = country_name.strip().lower()
    for row in data:
        if len(row) > 3 and row[3].lower() == name:
            return row
    return None


def row_to_values(row):
    values = []
    for v in row[4:]:
        try:
            values.append(float(v))
        except (ValueError, TypeError):
            values.append(None)
    return values

# ЛІНІЙНИЙ ГРАФІК
def build_line_chart(years, values1, label1, values2, label2, out_html):
    x = []
    y1 = []
    y2 = []

    for i, yr in enumerate(years):
        v1 = values1[i] if i < len(values1) else None
        v2 = values2[i] if i < len(values2) else None
        if v1 is None and v2 is None:
            continue
        x.append(int(yr))
        y1.append(v1 if v1 is not None else float("nan"))
        y2.append(v2 if v2 is not None else float("nan"))

    source = ColumnDataSource(dict(x=x, y1=y1, y2=y2))

    p = figure(
        title=f"Inflation (consumer prices, annual %) — {label1} vs {label2}",
        x_axis_label="Year",
        y_axis_label="Inflation (%)",
        tools="pan,wheel_zoom,box_zoom,reset,save",
        sizing_mode="stretch_width",
        height=400
    )

    # Лінія + точки для першої країни
    line1 = p.line("x", "y1", source=source, legend_label=label1, line_width=2, line_color="blue")
    scatter1 = p.scatter("x", "y1", source=source, size=6, fill_color="white", line_color="blue")

    # Лінія + точки для другої країни
    line2 = p.line("x", "y2", source=source, legend_label=label2, line_width=2, line_color="red")
    scatter2 = p.scatter("x", "y2", source=source, size=6, fill_color="white", line_color="red")

    # Hover для кожної серії окремо
    hover1 = HoverTool(renderers=[scatter1], tooltips=[("Year", "@x"), (label1, "@y1")])
    hover2 = HoverTool(renderers=[scatter2], tooltips=[("Year", "@x"), (label2, "@y2")])
    p.add_tools(hover1)
    p.add_tools(hover2)

    p.grid.grid_line_dash = [6, 4]

    output_file(out_html)
    save(p)
    del p
    print(f"Лінійний графік збережено у '{out_html}'.")
    return True

# СТОВПЧАСТА ДІАГРАМА
def build_bar_chart(years, values, country_name, out_html):
    values = (values or [])[:len(years)]
    values += [None] * (len(years) - len(values))

    x_str = [str(int(y)) for y in years]
    y_vals = [v if v is not None else 0 for v in values]

    source = ColumnDataSource(dict(year=x_str, val=y_vals))

    p = figure(
        title=f"Inflation (%) — {country_name}",
        x_axis_label="Year",
        y_axis_label="Inflation (%)",
        x_range=x_str,
        tools="pan,wheel_zoom,reset,save",
        sizing_mode="stretch_width",
        height=400
    )

    p.vbar(x='year', top='val', width=0.6, source=source,
           legend_label=country_name, color="green")

    p.xaxis.major_label_orientation = math.pi / 4
    p.add_tools(HoverTool(tooltips=[("Year", "@year"), ("Inflation", "@val")]))
    p.grid.grid_line_dash = [6, 4]

    output_file(out_html)
    save(p)
    del p
    print(f"Стовпчаста діаграма збережена у '{out_html}'.")
    return True

# ЗБЕРЕЖЕННЯ CSV З ОБРАНОЮ КРАЇНОЮ
def save_selected_country_csv(header, row, out_filename):
    try:
        with open(out_filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(row)
        print(f"Дані для вибраної країни збережено у '{out_filename}'.")
    except Exception as e:
        print("Помилка запису CSV:", e)

# ГОЛОВНА ФУНКЦІЯ
def main():
    print("Інтерактивна візуалізація за допомогою бібліотеки Bokeh")

    header, data = load_csv(CSV_FILENAME)
    if header is None:
        print("Завершення програми через помилку з файлом.")
        return

    years = parse_years(header)
    if not years:
        print("Не вдалося знайти роки у файлі.")
        return

    print("Роки:", years)
    print("Доступні країни: Ukraine, Poland, Afghanistan, Germany, France та інші")

    country1 = input("Введіть назву першої країни для графіка: ").strip()
    country2 = input("Введіть назву другої країни для графіка: ").strip()

    row1 = get_country_row(data, country1)
    row2 = get_country_row(data, country2)

    if row1 is None:
        print(f"Увага: дані для {country1} не знайдені.")
    if row2 is None:
        print(f"Увага: дані для {country2} не знайдені.")

    vals1 = row_to_values(row1) if row1 else [None] * len(years)
    vals2 = row_to_values(row2) if row2 else [None] * len(years)

    print(f"Будуємо лінійний графік для {country1} та {country2}...")
    try:
        build_line_chart(years, vals1, country1, vals2, country2, OUTPUT_HTML)
    except Exception as e:
        print("Помилка під час побудови лінійного графіка:", e)

    country = input("\nВведіть назву країни для стовпчастої діаграми (наприклад, Ukraine): ").strip()
    if not country:
        print("Країна не введена, стовпчаста діаграма буде пустою.")
    else:
        row = get_country_row(data, country)
        if row is None:
            print(f"Дані для країни '{country}' не знайдено.")
        else:
            vals = row_to_values(row)
            save_selected_country_csv(header, row, RESULT_CSV)
            try:
                build_bar_chart(years, vals, country, BAR_HTML)
            except Exception as e:
                print("Помилка під час побудови стовпчастої діаграми:", e)

    print("\nЗбережені файли:")
    print(" - Лінійний графік (HTML):", os.path.abspath(OUTPUT_HTML))
    print(" - Стовпчаста діаграма (HTML):", os.path.abspath(BAR_HTML))
    print(" - CSV з обраною країною:", os.path.abspath(RESULT_CSV))
    print("\nДля перегляду HTML-файлів їх необхідно відкрити у браузері.")


if __name__ == "__main__":
    main()
