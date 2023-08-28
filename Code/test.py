import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Willkommen bei 'Errate die Zahl'!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

    while True:
        guess = int(input("Dein Tipp: "))
        attempts += 1

        if guess < secret_number:
            print("Zu niedrig! Versuche es erneut.")
        elif guess > secret_number:
            print("Zu hoch! Versuche es erneut.")
        else:
            print(f"Glückwunsch! Du hast die Zahl {secret_number} in {attempts} Versuchen erraten.")
            break

if __name__ == "__main__":
    guess_the_number()
