import random

words = ["python", "java", "computer", "programming", "developer"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)