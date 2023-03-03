from utils import get_secret_word, guess_word, show_guesses, game_over, refresh_page
from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def main():
    secret_word = get_secret_word()
    guesses = ["_" * 5] * 6

    for idx in range(6):
        headline = f"Guess {idx + 1}"
        refresh_page(headline, console)
        show_guesses(guesses, secret_word, console)

        guesses[idx] = guess_word(guesses[:idx], console)
        if guesses[idx] == secret_word:
            break

    game_over(guesses, secret_word, console, guessed_correctly=guesses[idx] == secret_word)

if __name__ == "__main__":
    main()