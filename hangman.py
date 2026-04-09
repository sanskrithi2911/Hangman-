import random

words = ["python", "data", "science", "chatbot", "internship"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed:
    print("🎉 You won! Word was:", word)
else:
    print("💀 You lost! Word was:", word)
