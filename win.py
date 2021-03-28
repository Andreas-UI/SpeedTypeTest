import pygame as pg
import random

class Win:
    def __init__(self, score, total, screen, color, font, total_question):
        self.total = total
        self.score = score
        self.screen = screen
        self.text_color = color
        self.correct = 0
        self.base_font = font
        self.box_color = (206, 219, 55)
        self.input_rect = pg.Rect(50, 50, 700, 400)
        self.total_question = total_question

    def updateWin(self):
        if self.total == self.total_question:
            return True

    def drawWin(self):
            pg.draw.rect(self.screen, self.box_color, self.input_rect)

            # Render gameover to the screeen
            input_surface = self.base_font.render("Correct Answer " + str(self.correct) + "/" + str(self.total) , True, self.text_color)
            self.screen.blit(input_surface, (340, 170))

            # Render Correct Answer to the screeen
            input_surface = self.base_font.render("Game Over, Press C or Q", True, self.text_color)
            self.screen.blit(input_surface, (340, 210))

            # Render score to the screeen
            input_surface = self.base_font.render("Score : " + str(self.score), True, self.text_color)
            self.screen.blit(input_surface, (340, 250))

            pg.display.update()