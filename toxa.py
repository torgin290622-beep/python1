
import random
import numpy as np
import matplotlib.pyplot as plt

class Sportshy:
    def __init__(self, at, uakyt, zhas):
        self.at = at
        self.uakyt = uakyt
        self.zhas = zhas

    def info(self):
        return f"{self.at} - Жасы: {self.zhas}, Уақыты: {self.uakyt} сек"


class NatizhelerManager:
    def __init__(self):
        self.natizheler = {}


    def add_sportshy(self):
        try:
            at = input("Жаңа спортшы аты: ")
            uakyt = round(random.uniform(10, 100), 2)
            zhas = int(input("Жасы: "))
            self.natizheler[at] = Sportshy(at, uakyt, zhas)
            print(at, "қосылды.")
        except ValueError:
            print("Қате енгізу! Уақыт пен жасты дұрыс енгізіңіз.")


    def show_results(self):
        if not self.natizheler:
            print("Мәліметтер жоқ!")
            return

        print("Барлық спортшылар")
        for s in self.natizheler.values():
            print(s.info())

        ortasha_uakyt = sum(s.uakyt for s in self.natizheler.values()) / len(self.natizheler)
        print("Орташа уақыт:", int(ortasha_uakyt * 10) / 10, "секунд")


        results = []
        for s in self.natizheler.values():
            results.append((s.at, s.uakyt, s.zhas))

        for i in range(len(results)):
            for j in range(i + 1, len(results)):
                if results[i][1] > results[j][1]:
                    results[i], results[j] = results[j], results[i]


        print("Топ-3 үздік спортшы:")
        for i in range(min(3, len(results))):
            name, uakyt, zhas = results[i]
            print(i + 1, ".", name, "-", uakyt, "сек,", "Жасы:", zhas)

        print("График түрінде нәтижелер:")
        max_time = max(s.uakyt for s in self.natizheler.values())
        for s in self.natizheler.values():
            uzun = int((s.uakyt / max_time) * 40)
            print(s.at.ljust(10) + ": " + "█" * uzun + " " + str(s.uakyt) + " сек")


    def find_sportshy(self):
        izdeu = input("Қай спортшыны іздегіңіз келеді? ")
        for name in self.natizheler:
            if name.lower() == izdeu.lower():
                print(izdeu, "жарысқа қатысады!")
                return
        print(izdeu, "тізімде жоқ.")


    def save_to_file(self, filename="natizheler.txt"):
        try:
            with open(filename, "w") as f:
                for s in self.natizheler.values():
                    f.write(f"{s.at},{s.uakyt},{s.zhas}\n")
            print("Мәліметтер файлға сақталды.")
        except Exception as e:
            print("Файлға сақтау кезінде қате:", e)


    def load_from_file(self, filename="natizheler.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    at, uakyt, zhas = line.strip().split(",")
                    self.natizheler[at] = Sportshy(at, float(uakyt), int(zhas))
            print("Файлдан мәліметтер жүктелді.")
        except FileNotFoundError:
            print("Файл табылмады, жаңа файл жасалады.")


    def statistika_numpy(self):
        if not self.natizheler:
            print("Статистика жасау үшін мәлімет жоқ!")
            return

        vals = np.array([s.uakyt for s in self.natizheler.values()])
        print("\nNumPy статистикасы:")
        print("Барлық уақыттың қосындысы:", np.sum(vals))
        print("Орташа уақыт:", np.mean(vals))
        print("Максимум уақыт:", np.max(vals))
        print("Минимум уақыт:", np.min(vals))


    def grafik_salu(self):
        if not self.natizheler:
            print("График салу үшін мәлімет жоқ!")
            return
        categories = list(self.natizheler.keys())
        values = [s.uakyt for s in self.natizheler.values()]
        plt.figure(figsize=(8, 5))
        plt.bar(categories, values, edgecolor='black', color='yellow')
        plt.title("Спортшылардың жүзу уақыты")
        plt.xlabel("Спортшылар")
        plt.ylabel("Уақыты (сек)")
        plt.grid(True)
        plt.show()
