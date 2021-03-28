# https://www.pygame.org/wiki/TextWrapping?parent=CookBook

import pygame as pg

class Input:
    def __init__(self, screen, color, font, inputText, boxColor):
        self.screen = screen
        self.text_color = color
        self.base_font = font
        self.input_text = inputText
        self.input_box_color = boxColor

        self.leftRect = 50
        self.topRect = 400
        self.widthRect = 700
        self.heightRect = 30
        self.input_rect = pg.Rect(self.leftRect, self.topRect, self.widthRect, self.heightRect)
        

    def updateInput(self):

        # Draw input rectangle
        pg.draw.rect(self.screen, self.input_box_color, self.input_rect, 2)

        # Render input_text to the screeen
        input_surface = self.base_font.render(self.input_text, True, self.text_color)
        self.screen.blit(input_surface, (self.input_rect.x + 5, self.input_rect.y + 5))


        