import pygame
from constants import *
import sys

# Initialize pygame
pygame.init()

# Set up display

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sukoku!")

# Fonts
font = pygame.font.Font(None, 48)
title_font = pygame.font.Font(None, 80)

# Text elements
title_text = title_font.render("Welcome to Sudoku!", True, TITLE_COLOR)
title_rect = title_text.get_rect(center=(WIDTH // 2, 100))

question_text = font.render("Select Game Mode:", True, TITLE_COLOR)
question_rect = question_text.get_rect(center=(WIDTH // 2, 250))

option_texts = [
    font.render("EASY", True, BG_COLOR),
    font.render("MEDIUM", True, BG_COLOR),
    font.render("HARD", True, BG_COLOR)
]

total_button_width = len(option_texts) * BUTTON_WIDTH + (len(option_texts) - 1) * BUTTON_BUFFER
button_start_x = (WIDTH - total_button_width) // 2
option_rects = [
    pygame.Rect(button_start_x + (BUTTON_WIDTH + BUTTON_BUFFER) * i, 400, BUTTON_WIDTH, BUTTON_HEIGHT )
    for i in range(len(option_texts))
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, rect in enumerate(option_rects):
                if rect.collidepoint(mouse_pos):
                    if i == 0:
                        print("Option 1 clicked!")
                        # Perform action for Option 1
                    elif i == 1:
                        print("Option 2 clicked!")
                        # Perform action for Option 2
                    elif i == 2:
                        print("Option 3 clicked!")
                        # Perform action for Option 3

    # Clear the screen
    screen.fill(BG_COLOR)

    # Draw text elements
    screen.blit(title_text, title_rect)
    screen.blit(question_text, question_rect)
    for i, text in enumerate(option_texts):
        button_rect = option_rects[i]
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect, border_radius=15)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
