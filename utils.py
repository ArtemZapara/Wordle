
import random
from string import ascii_letters, ascii_uppercase

def get_secret_word():
    wordList = []
    with open("wordList.txt") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip().upper()
            if len(word) == 5 and all(letter in ascii_letters for letter in word):
                wordList.append(word)

    return random.choice(wordList)

def guess_word(previous_guesses, console):
    guess = console.input("\nGuess word: ").upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning")
        return guess_word(previous_guesses, console)

    if len(guess) != 5:
        console.print(f"Your guess must be 5 letters.", style="warning")
        return guess_word(previous_guesses, console)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(f"Invalid letter: '{invalid}'. Please use English letters only.", style="warning")
        return guess_word(previous_guesses, console)

    return guess

def show_guesses(guesses, secret_word, console):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, secret_word):
            if letter == correct:
                style = "bold white on green"
            elif letter in secret_word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"

        console.print("".join(styled_guess), justify="center")
    console.print("\n" + "".join(letter_status.values()), justify="center")

def refresh_page(headline, console):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def game_over(guesses, word, console, guessed_correctly):
    headline = "Game Over"
    refresh_page(headline, console)
    show_guesses(guesses, word, console)

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the secret word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]The secret word was {word}[/]")