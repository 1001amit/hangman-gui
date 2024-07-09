import random
import requests
import pygame
import sys

def fetch_random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def draw_hangman(screen, attempts):
    base = pygame.Rect(50, 300, 200, 20)
    pole = pygame.Rect(140, 50, 20, 250)
    beam = pygame.Rect(50, 50, 150, 20)
    rope = pygame.Rect(180, 50, 2, 50)

    parts = [
        pygame.Rect(160, 100, 40, 40),  # Head
        pygame.Rect(180, 140, 2, 60),   # Body
        pygame.Rect(180, 140, 50, 2),   # Right Arm
        pygame.Rect(130, 140, 50, 2),   # Left Arm
        pygame.Rect(180, 200, 2, 50),   # Right Leg
        pygame.Rect(180, 200, -2, 50)   # Left Leg
    ]

    pygame.draw.rect(screen, (0, 0, 0), base)
    pygame.draw.rect(screen, (0, 0, 0), pole)
    pygame.draw.rect(screen, (0, 0, 0), beam)
    pygame.draw.rect(screen, (0, 0, 0), rope)

    for i in range(6 - attempts):
        pygame.draw.rect(screen, (0, 0, 0), parts[i])

# Main function for the game
def hangman():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Hangman")

    word = fetch_random_word()
    if word is None:
        print("Failed to fetch a random word. Please try again.")
        return

    guessed_letters = []
    attempts = 6
    font = pygame.font.Font(None, 36)
    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                guess = pygame.key.name(event.key)
                if guess.isalpha() and len(guess) == 1:
                    if guess in guessed_letters:
                        print("You already guessed that letter.")
                    elif guess in word:
                        guessed_letters.append(guess)
                        print("Good guess!")
                    else:
                        guessed_letters.append(guess)
                        attempts -= 1
                        print("Wrong guess. Attempts left:", attempts)

        word_display = display_word(word, guessed_letters)
        text = font.render(word_display, True, (0, 0, 0))
        screen.blit(text, (50, 350))

        draw_hangman(screen, attempts)

        if '_' not in display_word(word, guessed_letters):
            game_over = True
            print("Congratulations, you won!")
        elif attempts == 0:
            game_over = True
            print("Sorry, you lost. The word was:", word)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    hangman()