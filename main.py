from sudoku_generator import SudokuGenerator
import pygame
from constants import *
import sys
from cell import Cell
from board import Board

def start_game():
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
        pygame.Rect(button_start_x + (BUTTON_WIDTH + BUTTON_BUFFER) * i, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
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
                            Board.draw(pygame)
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

if __name__ == "__main__":
    
    start_game()

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
        pygame.Rect(button_start_x + (BUTTON_WIDTH + BUTTON_BUFFER) * i, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
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

def draw_board(screen, sudoku, solved, original):
    font = pygame.font.SysFont("Arial", 35)
@@ -139,6 +139,84 @@ def draw_board(screen, sudoku, solved, original):
        pygame.display.update()


def check_board_full(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def insert_num(screen, pos, sudoku, original):
    if check_board_full(sudoku) is True:
        draw_game_over(screen, sudoku, original)
    x, y = pos[1], pos[0]
    font = pygame.font.SysFont("Arial", 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if original[x - 1][y - 1] != 0:
                    return

                if event.type == 48:
                    sudoku[x - 1][y - 1] = event.key - 48
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (pos[0] * 50 + 5, pos[1] * 50 + 5, 50 - 2 * 5, 50 - 2 * 5))
                    pygame.display.update()
                    return

                if 0 < event.key - 48 < 10:
                    pygame.draw.rect(screen, background_color,
                                     (pos[0] * 50 + 5, pos[1] * 50 + 5, 50 - 2 * 5, 50 - 2 * 5))
                    num = font.render(str(event.key - 48), True, (0, 0, 0))
                    screen.blit(num, (pos[0] * 50 + 15, pos[1] * 50))
                    sudoku[x - 1][y - 1] = event.key - 48
                    pygame.display.update()
                    return
                return


def draw_game_over(screen, sudoku, solved):
    is_over = False
    if sudoku == solved and len(sudoku) == len(solved) and 0 not in sudoku:
        is_over = True
    else:
        is_over = False

    if is_over is True:
        game_over_font = pygame.font.Font(None, 40)
        screen.fill(BG_COLOR)
        text = "You won!"
        game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)
        restart_surf = game_over_font.render("Restart", 0, LINE_COLOR)
        restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(restart_surf, restart_rect)
    else:
        game_over_font = pygame.font.Font(None, 40)
        screen.fill(BG_COLOR)
        text = "You lost."
        game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
        game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(game_over_surf, game_over_rect)
        restart_surf = game_over_font.render("Restart", 0, LINE_COLOR)
        restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(restart_surf, restart_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    main()
        pygame.display.update()
# Quit pygame
pygame.quit()
sys.exit()
