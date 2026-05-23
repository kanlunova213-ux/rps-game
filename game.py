import random
import os

choices = ["камень", "ножницы", "бумага"]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def determine_winner(player, computer):
    if player == computer:
        return "Ничья!"
    elif (
        (player == "камень" and computer == "ножницы") or
        (player == "ножницы" and computer == "бумага") or
        (player == "бумага" and computer == "камень")
    ):
        return "Ты победил!"
    else:
        return "Компьютер победил!"

while True:
    clear()
    print("=== Камень Ножницы Бумага ===")
    print("Варианты: камень, ножницы, бумага")

    player = input("Твой выбор: ").strip().lower()

    if player not in choices:
        print("Неверный выбор!")
        input("Нажми Enter...")
        continue

    computer = random.choice(choices)

    print(f"Компьютер выбрал: {computer}")
    print(determine_winner(player, computer))

    again = input("Сыграть ещё? (да/нет): ").strip().lower()
    if again != "да":
        print("Спасибо за игру!")
        break
