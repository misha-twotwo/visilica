import random

def choose_word():
    words = ['чмо', 'лох', 'соска', 'ruby', 'html', 'css', 'programming']
    return random.choice(words)

def display(word, guessed_letters):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display_word

def play():
    word = choose_word()
    guessed_letters = []
    tries = 6
    print("Добро пожаловать в игру Виселица!")
    print("Угадайте слово!")

    while tries > 0:
        print("\nТекущий статус слова: " + display(word, guessed_letters))
        print(f"Осталось попыток: {tries}")
        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Правильно! Буква '{guess}' есть в слове.")
        else:
            tries -= 1
            print(f"Неверно! Буква '{guess}' нет в слове.")

        if set(word) <= set(guessed_letters):
            print(f"\nПоздравляем! Вы угадали слово: {word}")
            break
    else:
        print(f"\nВы проиграли! Загаданное слово было: {word}")

if __name__ == "__main__":
    play()