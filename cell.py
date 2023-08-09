import pygame.font
from constants import *
class Cell:
    def __init__(self, value, row, col, screen):
        self.screen = screen
        self.col = col
        self.row = row
        self.value = value
        self.sketch = 0

    def set_cell_value(self, value):
        if value == None: ## if value has no true value, return None
            return
        self.value = value

    def set_sketched_value(self, sketch):
        self.value = 0
        self.sketch = sketch

    def draw(self):
        num_font = pygame.font.Font(None, 50)
        center_x_value = 50 + self.row * 100
        center_y_value = 50 + self.col * 100
        if self.value != 0:
            number = num_font.render(str(self.value), True, NUMBER_COLOR)
            number_rectangle = number.get_rect(center=(center_x_value, center_y_value))
            self.screen.blit(number, number_rectangle)
        if self.sketch != 0:
            sketched_number = num_font.render(str(self.sketch), True, SKETCHED_COLOR)
            number_rectangle = sketched_number.get_rect(center=(center_x_value, center_y_value))
            self.screen.blit(sketched_number, number_rectangle)