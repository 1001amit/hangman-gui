# Hangman Game

A simple hangman game implemented in Python using Pygame. The game fetches random words from an API and allows the user to guess the word by inputting letters.

## Features

- Fetches random words from an API
- Displays the word with guessed and unguessed letters
- Draws a hangman figure as the player makes incorrect guesses
- Ends the game when the player either guesses the word correctly or runs out of attempts

## Requirements

- Python 3.x
- Pygame library
- Requests library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/1001amit/hangman-gui.git
    cd hangman-game
    ```

2. Install the required libraries:
    ```sh
    pip install pygame requests
    ```

3. Run the game:
    ```sh
    python main.py
    ```

## How to Play

1. The game fetches a random word from an API.
2. You have 6 attempts to guess the word by inputting letters.
3. Each correct guess reveals the letter in the word.
4. Each incorrect guess draws a part of the hangman figure and decreases the number of attempts left.
6. The game ends when you either guess the word correctly or run out of attempts.
