import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry", 
            "blueberry", "kiwi", "mango", "peach", "pear", "cherry", "blackberry", 
            "apricot", "fig", "date", "lemon", "lime", "dragonfruit" ]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            print("Sorry, that letter is not in the word.")
            attempts -= 1
            print("Attempts left:", attempts)
    else:
        print("\nSorry, you ran out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
