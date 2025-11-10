
def add_sportshy(natizheler):
    try:
        at = input("Жаңа спортшы аты: ")
        uakyt = float(input("Жүзу уақыты (секунд): "))
        zhas = int(input("Жасы: "))
        natizheler[at] = {"uakyt": uakyt, "zhas": zhas}
        print(at, "қосылды.")
    except ValueError:
        print("Қате енгізу! Уақыт пен жасты дұрыс енгізіңіз.")
    return natizheler


def show_results(natizheler):
    if not natizheler:
        print("Мәліметтер жоқ!")
        return

    print("Барлық спортшылар")
    for name, info in natizheler.items():
        print(name + " - Жасы: " + str(info['zhas']) + ", Уақыты: " + str(info['uakyt']) + " сек")

    ortasha_uakyt = sum(i["uakyt"] for i in natizheler.values()) / len(natizheler)
    print("Орташа уақыт:", int(ortasha_uakyt * 10) / 10, "секунд")

    results = []
    for name, info in natizheler.items():
        results.append((name, info["uakyt"], info["zhas"]))

    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            if results[i][1] > results[j][1]:
                results[i], results[j] = results[j], results[i]

    print("Топ-3 үздік спортшы:")
    for i in range(min(3, len(results))):
        name, uakyt, zhas = results[i]
        print(i + 1, ".", name, "-", uakyt, "сек,", "Жасы:", zhas)


    # График түрінде
    print("График түрінде нәтижелер:")
    max_time = max(i["uakyt"] for i in natizheler.values())
    for at, info in natizheler.items():
        uzun = int((info["uakyt"] / max_time) * 40)
        print(at.ljust(10) + ": " + "█" * uzun + " " + str(info['uakyt']) + " сек")


def find_sportshy(natizheler):
    izdeu = input("Қай спортшыны іздегіңіз келеді? ")
    if izdeu.lower() in [a.lower() for a in natizheler.keys()]:
        print(izdeu, "жарысқа қатысады!")
    else:
        print(izdeu, "тізімде жоқ.")


def save_to_file(natizheler, filename="natizheler.txt"):
    try:
        with open(filename, "w") as f:
            for name, info in natizheler.items():
                f.write(f"{name},{info['uakyt']},{info['zhas']}\n")
        print("Мәліметтер файлға сақталды.")
    except Exception as e:
        print("Файлға сақтау кезінде қате:", e)


def load_from_file(filename="natizheler.txt"):
    natizheler = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                name, uakyt, zhas = line.strip().split(",")
                natizheler[name] = {"uakyt": float(uakyt), "zhas": int(zhas)}
        print("Файлдан мәліметтер жүктелді.")
    except FileNotFoundError:
        print("Файл табылмады, жаңа файл жасалады.")
    return natizheler
