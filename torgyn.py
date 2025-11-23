from toxa import NatizhelerManager

def main():
    print("ЖҮЗУ ЖАРЫСЫ БАҒДАРЛАМАСЫ")
    natizheler= NatizhelerManager()
    natizheler.load_from_file()

    while True:
        print("\nМәзір:")
        print("1. Спортшы қосу")
        print("2. Барлық нәтижелерді көру")
        print("3. Спортшы іздеу")
        print("4. Мәліметтерді файлға сақтау")
        print("5. NumPy статистикасы")
        print("6. График салу (Matplotlib)")
        print("7. Шығу")

        tandau = input("Таңдаңыз: ").strip()

        if not tandau:
            print("Таңдау бос болмауы керек! Қайта енгізіңіз.")
            continue

        if tandau == "1":
            natizheler.add_sportshy()

        elif tandau == "2":
            natizheler.show_results()

        elif tandau == "3":
            natizheler.find_sportshy()

        elif tandau == "4":
            natizheler.save_to_file()

        elif tandau == "5":
            natizheler.statistika_numpy()

        elif tandau == "6":
            natizheler.grafik_salu()

        elif tandau == "7":
            print("Бағдарлама аяқталды.")
            break

        else:
            print("Қате таңдау! Қайта көріңіз.")


if __name__ == "__main__":
    main()
 

