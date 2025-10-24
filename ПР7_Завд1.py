try:
    f1 = open("TF18_1.txt", "w", encoding="utf-8")
    f1.write("Текст з файлу TF18_1")
    f1.close()
except:
    print("Помилка при створенні TF18_1")

try:
    f2 = open("TF18_2.txt", "w", encoding="utf-8")
    f2.write("Це текст з файлу TF18_2")
    f2.close()
except:
    print("Помилка при створенні TF18_2")

try:
    f1 = open("TF18_1.txt", "r", encoding="utf-8")
    f3 = open("TF18_3.txt", "w", encoding="utf-8")
    while True:
        chunk = f1.read(20)
        if not chunk:
            break
        f3.write(chunk + "\n")
    f1.close()
    f3.close()
except:
    print("Помилка при копіюванні TF18_1 у TF18_3")

try:
    f2 = open("TF18_2.txt", "r", encoding="utf-8")
    f1 = open("TF18_1.txt", "w", encoding="utf-8")
    while True:
        chunk = f2.read(20)
        if not chunk:
            break
        f1.write(chunk + "\n")
    f2.close()
    f1.close()
except:
    print("Помилка при копіюванні TF18_2 у TF18_1")

try:
    f3 = open("TF18_3.txt", "r", encoding="utf-8")
    f2 = open("TF18_2.txt", "w", encoding="utf-8")
    while True:
        chunk = f3.read(20)
        if not chunk:
            break
        f2.write(chunk + "")
    f3.close()
    f2.close()
except:
    print("Помилка при копіюванні TF18_3 у TF18_2")

try:
    print("\nВміст TF18_1:")
    f1 = open("TF18_1.txt", "r", encoding="utf-8")
    for line in f1:
        print(line, end="")
    f1.close()
except:
    print("Помилка при читанні TF18_1")

try:
    print("\nВміст TF18_2:")
    f2 = open("TF18_2.txt", "r", encoding="utf-8")
    for line in f2:
        print(line, end="")
    f2.close()
except:
    print("Помилка при читанні TF18_2")
