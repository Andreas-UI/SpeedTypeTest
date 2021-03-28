class Score:
    def __init__(self, screen, color, font):
        self.screen = screen
        self.base_font = font
        self.text_color = color
        self.score_value = 0
        # self.pos_x = 0
        # self.pos_y = 20


    def updateScore(self):

        # Render score to the screen
        score = self.base_font.render("Score : " + str(self.score_value), True, self.text_color)
        score_rect = score.get_rect(center=(400, 40))
        self.screen.blit(score, score_rect)  