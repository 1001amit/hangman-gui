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
    base = pygame.Rect(100, 450, 400, 30)
    pole = pygame.Rect(240, 100, 30, 350)
    beam = pygame.Rect(100, 100, 300, 30)
    rope = pygame.Rect(370, 100, 5, 75)

    parts = [
        pygame.Rect(345, 175, 50, 50),  # Head
        pygame.Rect(365, 225, 5, 100),  # Body
        pygame.Rect(365, 225, 75, 5),   # Right Arm
        pygame.Rect(290, 225, 75, 5),   # Left Arm
        pygame.Rect(365, 325, 5, 75),   # Right Leg
        pygame.Rect(365, 325, -5, 75)   # Left Leg
    ]

    pygame.draw.rect(screen, (0, 0, 0), base)
    pygame.draw.rect(screen, (0, 0, 0), pole)
    pygame.draw.rect(screen, (0, 0, 0), beam)
    pygame.draw.rect(screen, (0, 0, 0), rope)

    for i in range(6 - attempts):
        pygame.draw.rect(screen, (0, 0, 0), parts[i])

def hangman():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hangman")

    global word, guessed_letters, attempts, game_over, round_counter

    def reset_game():
        global word, guessed_letters, attempts, game_over, round_counter
        word = fetch_random_word()
        if word is None:
            print("Failed to fetch a random word. Please try again.")
            return
        guessed_letters = []
        attempts = 6
        game_over = False
        round_counter += 1

    round_counter = 0
    reset_game()

    font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        reset_game()
                else:
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
        screen.blit(text, (100, 500))

        round_text = font.render(f"Round: {round_counter}", True, (0, 0, 0))
        screen.blit(round_text, (100, 50))

        draw_hangman(screen, attempts)

        if '_' not in display_word(word, guessed_letters):
            game_over = True
            end_text = font.render("Congratulations, you won! Press R to restart.", True, (0, 255, 0))
            screen.blit(end_text, (100, 100))
        elif attempts == 0:
            game_over = True
            end_text = font.render(f"The word was '{word}'. Press R to restart.", True, (255, 0, 0))
            screen.blit(end_text, (100, 100))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    hangman()
