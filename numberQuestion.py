import random
import pygame as pg
from essential_generators import DocumentGenerator

class numberQuestion():

    def __init__(self, screen, color, font):
        self.screen = screen
        # self.pos_x = 0
        # self.pos_y = 40
        self.text_color = color
        self.base_font = font
        self.question_value = random.choice([str(random.randint(10000000000000000000, 99999999999999999999)), DocumentGenerator().sentence()[:29] + "."])

    def updateQuestion(self):
        
        # Render question to the screen
        question = self.base_font.render("Question : " + str(self.question_value), True, self.text_color)
        question_rect = question.get_rect(center=(400, 60))
        self.screen.blit(question, question_rect)

    def generateQuestion(self):

        # Generate random question
        return random.choice([str(random.randint(10000000000000000000, 99999999999999999999)), DocumentGenerator().sentence()[:29] + "."])