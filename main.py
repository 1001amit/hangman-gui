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
