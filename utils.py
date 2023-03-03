
import random
from string import ascii_letters

def get_secret_word():
    wordList = []
    with open("wordList.txt") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip().upper()
            if len(word) == 5 and all(letter in ascii_letters for letter in word):
                wordList.append(word)

    return random.choice(wordList)

def show_guesses(guesses, secret_word, console):
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

        console.print("".join(styled_guess), justify="center")

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