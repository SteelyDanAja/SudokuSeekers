import pygame.font

class Cell:
    def __init__(self, value, row, col, screen):
        self.screen = screen
        self.col = col
        self.row = row
        self.value = value

    def set_cell_value(self, value):
        if value == None: ## if value has no true value, return None
            return
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        if self.value == 0:
            pass
        elif self.value > 0:
            sing_num = pygame.font.Font(None,100)
            num = str(self.value)
            draw_num = sing_num.render(num, 1, (000, 000, 000))
            self.screen.blit(draw_num, ((self.col*80)+22, (self.row*80)+9))



