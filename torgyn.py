
from toxa import add_sportshy, show_results, find_sportshy, save_to_file, load_from_file

def countdown(n):
    if n == 0:
        print("Бітті!")
    else:
        print(n)
        countdown(n - 1)


def main():
    print("=== ЖҮЗУ ЖАРЫСЫ БАҒДАРЛАМАСЫ ===")
    natizheler = load_from_file()

    while True:
        print("\nМәзір:")
        print("1. Спортшы қосу")
        print("2. Барлық нәтижелерді көру")
        print("3. Спортшы іздеу")
        print("4. Мәліметтерді файлға сақтау")
        print("5. Шығу")

        tandau = input("Таңдаңыз: ")

        if not tandau:
            print("Таңдау бос болмауы керек! Қайта енгізіңіз.")
            continue

        if tandau == "1":
            natizheler = add_sportshy(natizheler)
        elif tandau == "2":
            show_results(natizheler)
        elif tandau == "3":
            find_sportshy(natizheler)
        elif tandau == "4":
            save_to_file(natizheler)
        elif tandau == "5":
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате таңдау! Қайта көріңіз.")

if __name__ == "__main__":
    main()
