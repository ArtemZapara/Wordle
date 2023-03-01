def main():
    secret_word = "WORLD"
    for guess_num in range(1,7):
        guess = input("Guess the word: ").upper()
        if guess == secret_word:
            print("Correct")
            break

        correct_letters = {letter for letter, correct in zip(guess, secret_word) if letter == correct}
        misplaced_letters = set(guess) & set(secret_word) - correct_letters
        wrong_letters = set(guess) - set(secret_word)

        print("Correct letters:", ", ".join(correct_letters))
        print("Misplaced letters:", ", ".join(misplaced_letters))
        print("Wrong letters:", ", ".join(wrong_letters))

if __name__ == "__main__":
    main()